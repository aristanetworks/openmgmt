---
layout: default
title: "RESTCONF Configuration"
date: 2021-03-02 12:17:00 --0600
categories:
---

## Overview

EOS provides support for RESTCONF and the necessary transport services to support it.

The RESTCONF server is in the EOS device.

## RESTCONF configuration on EOS

### Certificate

Certificate-based authentication is required for RESTCONF to operate.  You should follow the instructions in the
[Certificate Authentication](/configuration/mtls.html) section in order to generate and install a certificate to support
RESTCONF in your environment.  Alternately, a self-signed certificate may be generated on the switch and certificate
validation can be handled appropriately by remote RESTCONF clients.

The following Cli command generates a self-signed cert:

```text
security pki certificate generate self-signed restconf.crt key restconf.key generate rsa 2048 parameters common-name restconf
```

Create ssl profile:

```text
management security
   ssl profile restconf
   certificate restconf.crt key restconf.key
```

### RESTCONF API

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

### Control-plane ACL

The default RESTCONF port on Arista devices is TCP 6020.
We need to change the default control-plane ACL on EOS in order to allow TCP 6020.

Here's the default Control Plane ACL

```text
device#show ip access-lists default-control-plane-acl
```

The new one includes the RESTCONF port

```text
device#show ip access-lists def2
IP Access List def2
        9 permit tcp any any eq 6020
        10 permit icmp any any
        20 permit ip any any tracked [match 147 packets, 0:00:14 ago]
        30 permit udp any any eq bfd ttl eq 255
        40 permit udp any any eq bfd-echo ttl eq 254
        50 permit udp any any eq multihop-bfd
        60 permit udp any any eq micro-bfd
        70 permit udp any any eq sbfd
        80 permit udp any eq sbfd any eq sbfd-initiator
        90 permit ospf any any [match 1882 packets, 0:00:04 ago]
        100 permit tcp any any eq ssh telnet www snmp bgp https msdp ldp netconf-ssh gnmi
        110 permit udp any any eq bootps bootpc ntp snmp rip ldp
        120 permit tcp any any eq mlag ttl eq 255
        130 permit udp any any eq mlag ttl eq 255
        140 permit vrrp any any
        150 permit ahp any any
        160 permit pim any any [match 124 packets, 0:00:14 ago]
        170 permit igmp any any [match 90 packets, 0:01:24 ago]
        180 permit tcp any any range 5900 5910
        190 permit tcp any any range 50000 50100
        200 permit udp any any range 51000 51100
        210 permit tcp any any eq 3333
        220 permit tcp any any eq nat ttl eq 255
        230 permit tcp any eq bgp any
        240 permit rsvp any any
        250 permit tcp any any eq 6040
```

```text
device#sh run sec control
system control-plane
   ip access-group def2 vrf MGMT in
```

### Status check

```text
#show management api restconf
Enabled:            Yes
Server:             running on port 6020, in management VRF
SSL Profile:        restconf
QoS DSCP:           none
```
