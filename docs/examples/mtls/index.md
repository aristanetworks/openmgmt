# EOS mTLS configuration

## overview

EOS supports the use of mTLS for gRPC services.  This allows the use of  certificates, signed by a recognized and
trusted CA, for authentication to gNMI and other gRPC based services.

By default only certificates signed with Arista's CA are trusted.  In order to generate and sign certificates for mTLS
an operator will need to install and configure a certifying authority (CA) that is used for signing certificates that
are generated on network elements as well as the servers that will be interacting with the gRPC services.  the necessary
certificates for establishing the chain of trust will need to be imported into the switches and tools interacting with
the switches.

This document outlines the necessary steps to generate certificate signing requests (CSR) on arista devices, sign the
certificates and import these into the switches.

## process overview

- setup a private certificate authority (CA). this document uses easy-rsa
  - <https://github.com/OpenVPN/easy-rsa>
- generate CSRs from the switch as well as from a host that will be initiating connections to the switch using mTLS as
  the authentication mechanism.
- sign the CSRs using the CA tools
- copy the relevant elements to the switch (signed server certificate and CA certificate)
- configure the switch to use the certificates and the associated CA certificate to perform mTLS authentication.

## easy-rsa CA parameters

**easy RSA version:** 3.0.8

```bash
set_var EASYRSA_REQ_COUNTRY  "us"
set_var EASYRSA_REQ_PROVINCE "mn"
set_var EASYRSA_REQ_CITY     "minneapolis"
set_var EASYRSA_REQ_ORG      "arista-lab"
set_var EASYRSA_REQ_EMAIL    "sulrich@arista.com"
set_var EASYRSA_REQ_OU       "dork-squad"
set_var EASYRSA_ALGO         "rsa"
set_var EASYRSA_DIGEST       "sha256"
```

Use the `build-ca` command to create the necessary certificate signing infrastructure.  This will generate a `ca.crt`
certificate which can be imported into the PKI validation chain of the switches and other hosts in your PKI domain.

In our case, this CA certificate resides in: `${HOME}/easy-rsa/pki/ca.crt`

This will need to be imported into the network elements you're using mTLS with.

## generate a local client certificate (u20)

This will be used for various grpc actions to the switch.

Note the `gnmi-client.cnf` configuration file provided is used to create the Subject Alternate Name IP address entry
associated with the client certificate.  This is optional and not required for client certificates.

```
mkdir ~/gnmi-client-cert
cd ~/gnmi-client-cert
openssl req -out gnmi-client.csr -newkey rsa:2048 -nodes -keyout gnmi-client.key -config gnmi-client.cnf
```

### sign the local client certificate with easy-rsa

Note, that this is going to be a _client_ certificate.  As our gnmi client will be talking to the gnmi server on the
switch.

```
cd ~/easy-rsa
./easyrsa import-req ../gnmi-client-cert gnmi-client.csr u20-gnmi
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

## switch side actions

- Generate a key pair on the switch the key will be named `v1.key`

```text
security pki key generate rsa 4096 v1.key
```

- Generate the CSR

```text
security pki certificate generate signing-request key v1.key

```

- Capture the CSR text into a file and copy this to the CA server. (u20)

## sign the switch CSR with easy-rsa

Note that in this case we're generating a _server_ certificate.

```shell
cd ~/easy-rsa
./easyrsa import-req ../v1.csr v1
./easyrsa sign-req server v1

```

This will generate the signed certificate and place it into the easy-rsa local store.

`/home/sulrich/easy-rsa/pki/issued/v1.crt`

- Copy this to the switch and import it into the switch's certificate store.

`copy file:/mnt/flash/v1.crt certificate:v1.crt`

## ssl profile configuration

configure the necessary ssl profile and associate it w/grpc and the gnmi service.

```text
management api gnmi
   transport grpc default
      ssl profile test-arista
   provider eos-native
!
management security
   ssl profile test-arista
      certificate v1.crt key v1.key
      trust certificate demo-ca.crt
!
```

## references

- <https://www.digitalocean.com/community/tutorials/how-to-set-up-and-configure-a-certificate-authority-ca-on-ubuntu-20-04>
- <https://eos.arista.com/working-with-certificates/>
