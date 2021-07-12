# EOS mTLS Configuration

## Overview

EOS supports the use of mutual TLS (mTLS) for gRPC, RESTCONF and eAPI services.  This allows the use of certificates,
signed by a recognized and trusted CA, for authentication to gNMI and other gRPC based services.

By default only certificates signed with Arista's CA are trusted.  In order to generate and sign certificates for mTLS
authentication, an operator will need to install and configure a certifying authority (CA) that is used for signing
certificates that are generated on network elements as well as the servers that will be interacting with the gRPC
services.  The necessary certificates for establishing the chain of trust will need to be imported into the switches and
tools interacting with the switches.

This document outlines the necessary steps to generate certificate signing requests (CSR) on arista devices, sign the
certificates and import these into the switches.

## Process Overview

- Setup a private certificate authority (CA).  This document uses [easy-rsa](https://github.com/OpenVPN/easy-rsa)
- Generate CSRs from the switch as well as for the host that will be initiating connections to the switch using mTLS as
  the authentication mechanism.
- Sign the CSRs using the CA tools.
- Copy the relevant elements to the switch (signed server certificate and CA certificate).
- Configure the switch to use the certificates and the associated CA certificate to perform mTLS authentication.
- Initiate connections from the clients to the switch to execute gNMI RPCs.

## Easy-RSA Setup

The simple installation of Easy-RSA is well documented in the Easy RSA [quick start
guide](https://github.com/OpenVPN/easy-rsa/blob/master/README.quickstart.md).  For a more durable installation you're
encouraged to review the Easy-RSA documentation and customize the settings to your environment.

### Easy-RSA CA parameters

**easy RSA version:** 3.0.8

As of this writing EOS only supports RSA certificates, this differs from the default configuration of Easy-RSA.  The
following variable in the `vars` file will need to be set in order to generate the appropriate certificate type.

```bash
set_var EASYRSA_ALGO "rsa"
```

Use the `easyrsa build-ca` command to create the necessary certificate signing infrastructure within easyrsa.  This will
generate a `ca.crt` certificate which can be imported into the PKI validation chain of the switches and other hosts in
your PKI domain.  This can also be used in a standalone manner with most gnmi clients.

In our case, this CA certificate resides in: `${HOME}/easy-rsa/pki/ca.crt`

This will need to be imported into the network elements where you're using mTLS for authentication.

## Generate a Local Client Certificate

This will be used by local clients (gnmi, gnoi, gribi, etc.) connecting to the switches in order to authenticate.

Note the `gnmi-client.cnf` configuration file provided in the following `openssl` command is used to create the Subject
Alternate Name IP address entry associated with the client certificate.  This is optional and is not required for
certificates.

```text
mkdir ~/gnmi-client-cert
cd ~/gnmi-client-cert
openssl req -out gnmi-client.csr -newkey rsa:2048 -nodes -keyout gnmi-client.key -config gnmi-client.cnf
```

The above commands will generate a private key as well as the Certificate Signing Request (CSR)

### Sign the Local Client Certificate with Easy-RSA

Note, that this is going to be a _client_ certificate.  As our gnmi client will be talking to the gnmi server on the
switch.

```text
cd ~/easy-rsa
./easyrsa import-req ../gnmi-client-cert gnmi-client.csr gnmi-client
./easyrsa sign-req client gnmi-client
Using SSL: openssl OpenSSL 1.1.1f  31 Mar 2020

... snipped ...

subject=
    countryName               = us
    stateOrProvinceName       = mn
    localityName              = minneapolis
    organizationName          = arista-lab
    commonName                = sulrich@arista.com

X509v3 Subject Alternative Name:
    IP:192.168.1.11


Type the word 'yes' to continue, or any other input to abort.
  Confirm request details: yes
Using configuration from /home/sulrich/easy-rsa/pki/easy-rsa-3625384.5yQThV/tmp.kaJhk0
Check that the request matches the signature
Signature ok
The Subject's Distinguished Name is as follows
countryName           :PRINTABLE:'us'
stateOrProvinceName   :ASN.1 12:'mn'
localityName          :ASN.1 12:'minneapolis'
organizationName      :ASN.1 12:'arista-lab'
commonName            :ASN.1 12:'sulrich@arista.com'
Certificate is to be certified until Oct 10 19:45:42 2023 GMT (825 days)

Write out database with 1 new entries
Data Base Updated

Certificate created at: /home/sulrich/easy-rsa/pki/issued/gnmi-client.crt
```

## Switch Side Actions

- Generate a key pair on the switch the key will be named `v1.key`

```text
security pki key generate rsa 4096 v1.key
```

- Generate the CSR

```text
security pki certificate generate signing-request key v1.key

```

- Capture the CSR text into a file and copy this to the CA server.

## Sign the Switch CSR with Easy-RSA

Note that in this case we're generating a _server_ certificate.

```shell
cd ~/easy-rsa
./easyrsa import-req ../v1.csr v1
./easyrsa sign-req server v1
```

This will generate the signed certificate and place it into the easy-rsa local store.

`${HOME}/easy-rsa/pki/issued/v1.crt`

- Copy this to the switch and import it into the switch's certificate store.

`copy file:/mnt/flash/v1.crt certificate:v1.crt`

## Copy the Private CA Certificate to the Switch

You will need to copy the `CA.crt` (commonly in `<easyrsa_root>/pki/ca.crt`) to the switch and add it to the list of
certificates.  In the following example the file has been copied to the switch as `demo-ca.crt`.

```text
copy flash:demo-ca.crt certificate:
```

## SSL Profile Configuration

Configure the necessary `ssl profile` and include the `demo-ca.crt` in the list of trusted CAs.

```text
management security
   ssl profile test-arista
      certificate v1.crt key v1.key
      trust certificate demo-ca.crt
!
```

## gNMI Configuration

The following configuration associates the gnmi service withthe associated ssl profile and enables it for use with mTLS
for authentication.

```text
management api gnmi
   transport grpc default
      ssl profile test-arista
   provider eos-native
!
```

At this point the switch is configured to accept connections from clients with valid, signed certificates.

## Useful Troubleshooting Commands

`show management api gnmi`

This command enables you to determine the operational state of the gnmi process as well as whether or not the ssl profile
is considered valid.

`show management security ssl profile`

This command enables you to see the state of the ssl profiles and whether there are issues with the validation chain.

### Clocks and Certificate Lifetime

Certificates should be created with a finite lifetime and rotated within that lifetime.  However, if the clocks on the
switch are grossly off this may impact certificate operation.  Make sure that the clock on the switch is set correctly
and synchronized to a reliable time source.

## Client Examples

### gnmi (Arista Client)

```shell
gnmi -addr 192.168.1.21:6030                    \
  -username admin -password arista              \
  -cafile easy-rsa/pki/ca.crt                   \
  -certfile easy-rsa/pki/issued/gnmi-client.crt \
  -keyfile gnmi-client/gnmi-client.key capabilities
```

### gnmic

```shell
gnmic -a 192.168.1.21:6030 -u admin -p arista    \
  --tls-ca easy-rsa/pki/ca.crt                   \
  --tls-cert easy-rsa/pki/issued/gnmi-client.crt \
  --tls-key gnmi-client/gnmi-client.key capabilities
```

## Additional References

- [EOS central: Working with Certificates](steps://eos.arista.com/working-with-certificates/)
