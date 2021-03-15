---
layout: page
title: "Device Configuration"
date: 2021-03-02 12:17:00 --0600
categories:
---
- [overview](#overview)
- [CLI](#cli)
- [## OpenConfig (configuration)](#-openconfig-configuration)
  - [Platform compatibility](#platform-compatibility)
  - [GNMI](#gnmi)
  - [OCTA](#octa)
    - [How to enable Octa](#how-to-enable-octa)
    - [API models](#api-models)
    - [Certificate based authentication for gNMI](#certificate-based-authentication-for-gnmi)
    - [Test example](#test-example)
  - [NETCONF](#netconf)
  - [RESTCONF](#restconf)
- [A note on changing ports](#a-note-on-changing-ports)
- [gRPC](#grpc)
  - [RPC role authorizations](#rpc-role-authorizations)
- [Enable AFT mapping](#enable-aft-mapping)
- [Troubleshooting](#troubleshooting)
- [Limitations](#limitations)
- [Supported OpenConfig paths](#supported-openconfig-paths)
- [References / Resources](#references--resources)

## overview

## CLI

## OpenConfig (configuration)

---

### Platform compatibility

All EOS flavors support OpenConfig (phyiscal, virtual, containerized, cloud).

### GNMI

To start the gNMI server, which listens by default on TCP/6030 configured the gRPC transport
under `management api gnmi` in the global config mode:

Default VRF

```text
management api gnmi
  transport grpc openmgmt
```

Non-default VRF

```text
management api gnmi
   transport grpc openmgmt
     vrf management
```

Changing the port:

```text
management api gnmi
   transport grpc openmgmt
      port 5900
```

Apply ACL

```text
management api gnmi
   transport grpc openmgmt
      ip access-group ACCESS_GROUP
```

>Note The ACL should be a standard ACL allowing hosts or subnets.

Authenticate the connection with TLS

```text
management api gnmi
   transport grpc openmgmt
      ssl profile PROFILE
```

Enable authorization of incoming requests

```text
management api gnmi
   transport grpc openmgmt
      authorization requests
```

Status check

```text
#show management api gnmi
Octa:               No
Enabled:            Yes
Server:             running on port 6030, in default VRF
SSL Profile:        none
QoS DSCP:           none
```

### OCTA

The OpenConfing agent (gNMI API) can leverage the EOS state streaming agent's (TerminAttr)
libraries, thus exposing EOS native paths. If Octa (OpenConfig+TerminAttr) is enabled then
OpenConfig, in addition to accepting OpenConfig paths in gNMI get/subscribe requests, will also
support EOS native paths (e.g. Sysdb/Smash paths). This feature was introduced in `4.22.1F`.

gNMI requests received by Octa are interpreted as either OpenConfig or TerminAttr requests, as follows.

- gNMI requests containing an origin of `eos_native` are processed as TerminAttr requests.
- Requests lacking an origin of `eos_native` are treated as OpenConfig requests.

A gNMI client that supports specification of an origin as part of the associated RPC is a requirement.

> Note Support for sending GET/SUBSCRIBE requests to both an openconfig and an eos-native
> path in the same call is not yet supported.

#### How to enable Octa

Octa can be enable by adding `provider eos-native` under `management api gnmi`

`SW(config-mgmt-api-gnmi)#provider eos-native`

Status check

```text
#show management api gnmi
Octa:               enabled
Enabled:            Yes
Server:             running on port 6030, in default VRF
SSL Profile:        none
QoS DSCP:           none
```

#### API models

Starting in EOS 4.24.0F it is possible to configure the Smash paths that Octa has
access to. Under the `management api models` mode, the provider smash submode allows
for enabling or disabling a Smash path with the `[no] path <Smash path> [disbaled]` command.

```text
SW(config)#management api models
SW(config-mgmt-api-models)#provider smash
SW(config-provider-smash)#path forwarding/status
SW(config-provider-smash)#path routing/status disabled
SW(config-provider-smash)#path routing/isis/lsdb
SW(config-provider-smash)#exit
```

> Note that every time a new path is added the Octa agent has to be restarted.
> EOS CLI:
>
> ```text
> (config)#management api gnmi
> (config-mgmt-api-gnmi)#transport grpc <NAME>
> (config-gnmi-transport-def)#shut
> (config-gnmi-transport-def)#no shut
> ```
>
> Bash:
> `$ sudo killall Octa`

`show management api models` will list the Smash paths enabled/disabled

e.g.:

```text
#show management api models
provider smash
  path /Smash/bridging
  path /Smash/forwarding/status
  path /Smash/routing/isis/lsdb
  path /Smash/routing
  path /Smash/routing/status disabled
provider sysdb
```

#### Certificate based authentication for gNMI

The following example shows how to create a Root CA cert and key, the server cert
and key and the client cert and key.

On the switch side:

1\. Generate the private key for the CA:

`openssl genrsa -out rootCA.key 2048`

2\. Generate the CA certificate:

`openssl req -x509 -new -nodes -key rootCA.key -out rootCA.pem`

3\. Generate the server key:

`openssl genrsa -out gnmi_server.key 2048`

4\. Generate the server's ceritifcate signing request:

`openssl req -new -key gnmi_server.key -out gnmi_server.csr`

5\. Generate the server's cert:

 `openssl x509 -req -in gnmi_server.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out gnmi_server.crt`

6\. copy `rootCA.key` and `rootCA.pem` to the gNMI collector

7\. Exit from bash and copy `rootCA.key` and `gnmi_server.key` to sslkey directory. e.g.:

`copy flash:gnmi_server.key sslkey:`)

8\. copy `rootCA.pem` and  `gnmi_server.crt` to certificate directory, e.g.:

`copy  flash:scripts/rootCA.pem certificate:`)

9\. Create the SSL profile

```text
management security
   ssl profile gnmi
      certificate gnmi_server.crt key gnmi_server.key
      trust certificate rootCA.pem
```

10\. Apply the profile

```text
management api gnmi
   transport grpc def
      ssl profile gnmi
   provider eos-native

```

On the remote machine which runs the gNMI queries:

1\. Generate the client key:

`openssl genrsa -out gnmi_client.key 2048`

2\. Generate the certificate signing request:

`openssl req -new -key gnmi_client.key -out gnmi_client.csr`

3\. Sign the cert and generate the .crt file:

`openssl x509 -req -in gnmi_client.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out gnmi_client.crt`

4\. Make sure that `rootCA.key`  and `rootCA.pem` are in same directory as `gnmi_client.key` and `gnmi_client.crt`

#### Test example

```bash
gnmi -tls -addr 172.28.161.138:6030 -keyfile gnmi_client.key -certfile gnmi_client.crt get '/interfaces/interface[name=*]/state/counters'


/interfaces/interface[name=Management1]/state/counters:
{
  "openconfig-interfaces:in-broadcast-pkts": "14498549",
  "openconfig-interfaces:in-discards": "0",
  "openconfig-interfaces:in-errors": "0",
  "openconfig-interfaces:in-fcs-errors": "0",
  "openconfig-interfaces:in-multicast-pkts": "20571",
  "openconfig-interfaces:in-octets": "1042742343",
  "openconfig-interfaces:in-unicast-pkts": "61135",
  "openconfig-interfaces:out-broadcast-pkts": "20",
  "openconfig-interfaces:out-discards": "0",
  "openconfig-interfaces:out-errors": "0",
  "openconfig-interfaces:out-multicast-pkts": "20232",
  "openconfig-interfaces:out-octets": "12004699",
  "openconfig-interfaces:out-unicast-pkts": "49070"
}

```

### NETCONF

[NETCONF](https://tools.ietf.org/html/rfc6241) provides mechanisms to install,
manipulate and delete the configuration of network devices. It uses eXtensible
Markup Language (XML) based data encoding for the configuration data as well as
protocol messages. The NETCONF protocol operations are realized as RPCs over ssh transport.

Currently supported NETCONF operations: get, get-config, get-schema, edit-config, lock, unlock, close-session, kill-session.

To configure NETCONF in default VRF we can enable the ssh transport under `management api netconf`:

Default VRF

```text
management api netconf
   transport ssh test
```

Non-default VRF

```text
management api netconf
   transport ssh test
      vrf management
```

Changing the port:

```text
management api netconf
   transport ssh test
      port 830
```

Apply ACL

```text
management api netconf
   transport ssh test
      ip access-group ACCESS_GROUP
```

>Note The ACL should be a standard ACL allowing hosts or subnets.

Status check:

```text
#show management api netconf

Enabled:            Yes
Server:             running on port 830, in management VRF
```

### RESTCONF

TLS authentication is required for RESTCONF to operate.

This Cli command generates a self-signed cert:

```security pki certificate generate self-signed restconf.crt key restconf.key generate rsa 2048 parameters common-name restconf```

Create ssl profile:

```text
management security
   ssl profile restconf
   certificate restconf.crt key restconf.key
```

Configure RESTCONF:

Default VRF:

```text
management api restconf
   transport https test
   ssl profile restconf
```

Non-default VRF

```text
management api restconf
   transport https test
   ssl profile restconf
   vrf management
```

Changing the port:

```text
management api restconf
   transport https test
      port 5900
```

Apply ACL

```text
management api restconf
   transport https test
      ip access-group ACCESS_GROUP
```

>Note The ACL should be a standard ACL allowing hosts or subnets.

Status check

```text
#show management api restconf
Enabled:            Yes
Server:             running on port 6020, in management VRF
SSL Profile:        restconf
QoS DSCP:           none
```

## A note on changing ports

When changing the default ports one has to make sure they are also allowed in
the control-plane ACL. The default control-plane ACL cannot be modified, so a
new one has to be created and applied under `system control-plane` (EOS 4.23+)
or `control-plane` (pre-EOS 4.23). The fastest way to do this is to clone the existing control-plane and add new permit rules.

e.g.:

1\. Reading the default CP ACL can be done with `show ip access-lists default-control-plane-acl`

```text
#show ip access-lists default-control-plane-acl
IP Access List default-control-plane-acl [readonly]
        counters per-entry
        10 permit icmp any any [match 7172 packets, 1 day, 20:46:09 ago]
        20 permit ip any any tracked [match 98544013 packets, 0:00:36 ago]
        30 permit udp any any eq bfd ttl eq 255
        40 permit udp any any eq bfd-echo ttl eq 254
        50 permit udp any any eq multihop-bfd
        60 permit udp any any eq micro-bfd
        70 permit udp any any eq sbfd
        80 permit udp any eq sbfd any eq sbfd-initiator
        90 permit ospf any any
        100 permit tcp any any eq ssh telnet www snmp bgp https msdp ldp netconf-ssh gnmi [match 873 packets, 1 day, 20:43:39 ago]
        110 permit udp any any eq bootps bootpc snmp rip ntp ldp [match 970 packets, 1:43:38 ago]
        120 permit tcp any any eq mlag ttl eq 255
        130 permit udp any any eq mlag ttl eq 255
        140 permit vrrp any any
        150 permit ahp any any
        160 permit pim any any
        170 permit igmp any any
        180 permit tcp any any range 5900 5910
        190 permit tcp any any range 50000 50100 [match 1480505 packets, 1 day, 20:43:16 ago]
        200 permit udp any any range 51000 51100
        210 permit tcp any any eq 3333
        220 permit tcp any any eq nat ttl eq 255
        230 permit tcp any eq bgp any
        240 permit rsvp any any
        250 permit tcp any any eq 6040
        260 permit tcp any any eq 5541 ttl eq 255
        270 permit tcp any any eq 5542 ttl eq 255
```

2\. There are multiple ways to quickly edit and remove the unnecessary match outputs,
 in this example we'll use `sed` on EOS. Save the file to `/mnt/flash`:

`show ip access-lists  default-control-plane-acl | redirect flash:cpacl.txt`

3\. Drop down to bash:

`#bash`

4\. Go to /mnt/flash and remove the match outputs

`cd /mnt/flash`
`sudo sed -i  "s/\[.*//g" cpacl.txt`

5\. Reading the file now should be clean without all the match outputs like below:

```text
cat cpacl.txt
IP Access List default-control-plane-acl
        counters per-entry
        10 permit icmp any any
        20 permit ip any any tracked
        30 permit udp any any eq bfd ttl eq 255
        40 permit udp any any eq bfd-echo ttl eq 254
        50 permit udp any any eq multihop-bfd
        60 permit udp any any eq micro-bfd
        70 permit udp any any eq sbfd
        80 permit udp any eq sbfd any eq sbfd-initiator
        90 permit ospf any any
        100 permit tcp any any eq ssh telnet www snmp bgp https msdp ldp netconf-ssh gnmi
        110 permit udp any any eq bootps bootpc snmp rip ntp ldp
        120 permit tcp any any eq mlag ttl eq 255
        130 permit udp any any eq mlag ttl eq 255
        140 permit vrrp any any
        150 permit ahp any any
        160 permit pim any any
        170 permit igmp any any
        180 permit tcp any any range 5900 5910
        190 permit tcp any any range 50000 50100
        200 permit udp any any range 51000 51100
        210 permit tcp any any eq 3333
        220 permit tcp any any eq nat ttl eq 255
        230 permit tcp any eq bgp any
        240 permit rsvp any any
        250 permit tcp any any eq 6040
        260 permit tcp any any eq 5541 ttl eq 255
        270 permit tcp any any eq 5542 ttl eq 255
```

6\. Now we can just copy that ACLs content into a new ACL, add our new rules and
apply it on the control-plane

```text
$ exit
logout
(config)# ip access-list custom-cp
(config)#
<paste the content of the default CP from the file created>
(config)# 280 permit tcp any any eq 5900
```

7\. Apply the new ACL

Default VRF

```text
sysem control-plane
   ip access-group custom-cp in
```

Non-default VRF

```text
sysem control-plane
   ip access-group custom-cp vrf management in
```

## gRPC

gRPC is a Remote Procedure Call (RPC) framework that OpenConfig utilizes as a transport.
Services built with gRPC are defined in `.proto` files.
They describe the RPCs supported by the service and the data types exchanged in those RPCs.

The OpenConfig group originally published [openconfig.proto](https://github.com/openconfig/reference/blob/master/rpc/openconfig/openconfig.proto),
but have since deprecated it in favor of [gnmi.proto](https://github.com/openconfig/reference/blob/master/rpc/gnmi).
The current EOS versions supports gnmi.proto v0.7 and includes support for Get, Subscribe, Set, and Capabilities RPCs.

> Note: Support for openconfig.proto was dropped in EOS-4.23.0F+.

A client application is required to communicate with a gRPC service.
A sample application can be found on the Arista GitHub account: [gnmi](https://github.com/aristanetworks/goarista/tree/master/cmd/gnmi).
`gnmi` is a simple command-line client for gNMI written in Go that can be used for testing and prototyping.

Another popular gnmi client is [gnmic](https://gnmic.kmrd.dev/).

### RPC role authorizations

Starting in EOS 4.24.1F it is possible to perform authorization of each RPC (i.e. GET, SET, SUBSCRIBE),
if authorization requests is supplied as described above.

During authorization, the OpenConfig agent will communicate with the AAA agent,
allowing authorization policies or roles to permit or deny the new tokens OpenConfig.Get
and OpenConfig.Set.

For example, a role may be defined such as:

```text
role oc-read
   10 permit command OpenConfig.Get
```

A user which is assigned to this role would be allowed to issue a gNMI get or
subscribe request, but not a set request.

> Note that this is only available for gNMI.

## Enable AFT mapping

By default, mapping of the FIB (forwarding information base) to the
OpenConfig AFT (abstract forwarding table) model is disabled, as the volume of data can be large.

Starting in EOS 4.25.1F it is possible to enable these mappings, for IPV4, IPV6, or both, as described below:

```text
management api models
    ipv4-unicast
    ipv6-unicast
```

## Troubleshooting

The OpenConfig agent handles all transports described above: gNMI, RESTCONF, and NETCONF.
The agent log file is present at `/var/log/agents/OpenConfig-{PID}`.
Lines that begin with `E` are errors. Debug logging can be enabled with a regular trace command. Here are a couple of examples:

`(config)#trace OpenConfig setting server/9` # For server (gNMI) traces

`(config)#trace OpenConfig setting */9` # For all traces with verbose setting

similary if Octa is enabled:

`(config)#trace Octa setting server/9` # For server (gNMI) traces

`(config)#trace Octa setting */9` # For all traces with verbose setting

## Limitations

- In EOS versions older than 4.24.0F, not all Smash paths were accessible via Octa.

- Starting in EOS 4.24.0F configuring the Smash paths that Octa has access to will
  also affect OpenConfig.
  Enabling a Smash path for Octa can result in extra YANG paths being populated in OpenConfig.
  Disabling a Smash path can result in having some YANG paths missing in OpenConfig.

- The `%<zone-id>` optional suffix in YANG `ietf:ipv4-address`, and `ietf:ipv6-address` types are not supported.
- An OpenConfig client update/merge/replace request can erase config that is not modified
  by the incoming request. This happens if a config that is part of a certain mountpoint
  but not supported by OpenConfig is configured via CLI prior to the
  OpenConfig client update/merge/replace request is processed.
- Below listed commands are the only QoS config commands that are supported

    ```text
    class-map type qos match-any <cm name>
        match vlan <vlan id>

    policy-map type qos <pmap name>
        class <cm name>
            police cir <cir> bc <burst> kbytes
        class class-default

    interface Ethernet<xx> | port-channel<yy>
        service-policy type qos input <pmap name>
    ```

## Supported OpenConfig paths

Please refer to the TOIs for the EOS releases to see the new list of paths supported per release.

For convenience, supported paths may be found at <https://eos.arista.com/path-report>.

## References / Resources

The OpenConfig working group: [http://openconfig.net/](http://openconfig.net/)

Repository of OpenConfig YANG models: [https://github.com/openconfig/public](https://github.com/openconfig/public)

Arista Networks YANG Repository: [https://github.com/aristanetworks/yang](https://github.com/aristanetworks/yang)

Repository of gNMI specifications: [https://github.com/openconfig/reference/](https://github.com/openconfig/reference/)

YANG RFC: [https://tools.ietf.org/html/rfc6020](https://tools.ietf.org/html/rfc6020)

NETCONF RFC: [https://tools.ietf.org/html/rfc6241](https://tools.ietf.org/html/rfc6241)

RESTCONF RFC: [https://tools.ietf.org/html/rfc8040](https://tools.ietf.org/html/rfc8040)
