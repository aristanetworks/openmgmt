---
layout: default
title: "gNOIc examples"
date: 2021-07-16 12:17:00 --0600
categories:
---

## About gRPC

gRPC - Google Remote Procedure Call

gRPC uses protobuf and HTTP/2

## About gNOI

gNOI - gRPC Network Operations Interface

gNOI defines a set of gRPC-based microservices for executing operational commands on network devices.

gNOI [github repository](https://github.com/openconfig/gnoi)

As example, [this gNOI proto file](https://github.com/openconfig/gnoi/blob/master/system/system.proto) defines the service `System` with the RPC `Traceroute` and `Ping`

- Ping executes the ping command on the target and streams back the results
- Traceroute executes the traceroute command on the target and streams back the results
- As you can see in the proto file, the field VRF is not defined for these messages

## About gNOI support on EOS

Please refer to this [link](https://eos.arista.com/eos-4-24-2f/gnoi/) for the gNOI support by EOS.

Examples:

- [gnoi ping](https://eos.arista.com/eos-4-22-1f/gnoi-ping/)
- [gnoi traceroute](https://eos.arista.com/eos-4-22-1f/gnoi-traceroute/)

## gNOIc overview

gNOIc is a gNOI CLI client:

- [source code](https://github.com/karimra/gnoic)
- [documentation](https://gnoic.kmrd.dev/)

The following examples shows various gNOIc commands with Arista EOS devices.

## Download & install gNOIc

To install run:

```shell
bash -c "$(curl -sL https://get-gnoic.kmrd.dev)"
```

To get the version run:

```shell
gnoic version
```

Output:

```shell
version : 0.0.5
 commit : 26c6248
   date : 2021-05-12T10:12:55Z
 gitURL : https://github.com/karimra/gnoic
   docs : https://gnoic.kmrd.dev
```

## Device config

```shell
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.1.118/24

username arista secret 0 arista

management api gnmi
   transport grpc def
      vrf MGMT
```

```shell
DC1-L2LEAF2A#show management api gnmi
Enabled:            Yes
Server:             running on port 6030, in MGMT VRF
SSL Profile:        none
QoS DSCP:           none
DC1-L2LEAF2A#
```

Before to use gNOI ping and traceroute, lets run these commands locally:

```shell
$ ssh arista@10.73.1.118
Password:
Last login: Thu Jun  3 12:06:25 2021 from 10.73.1.3
DC1-L2LEAF2A>en
DC1-L2LEAF2A#bash

Arista Networks EOS shell

[arista@DC1-L2LEAF2A ~]$ ping  172.31.255.0 -c 2
PING 172.31.255.0 (172.31.255.0) 56(84) bytes of data.
64 bytes from 172.31.255.0: icmp_seq=1 ttl=63 time=24.6 ms
64 bytes from 172.31.255.0: icmp_seq=2 ttl=63 time=18.8 ms

--- 172.31.255.0 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 18.861/21.738/24.616/2.881 ms
[arista@DC1-L2LEAF2A ~]$
[arista@DC1-L2LEAF2A ~]$ traceroute -A 172.31.255.0
traceroute to 172.31.255.0 (172.31.255.0), 30 hops max, 60 byte packets
 1  10.90.90.1 (10.90.90.1) [!!]  26.636 ms  29.420 ms  32.113 ms
 2  172.31.255.0 (172.31.255.0) [!!]  52.764 ms  53.881 ms  63.213 ms
[arista@DC1-L2LEAF2A ~]$
[arista@DC1-L2LEAF2A ~]$ exit
logout
DC1-L2LEAF2A#exit
Connection to 10.73.1.118 closed.
```

## gNOI demo with Arista using gNOIc

```shell
gnoic -a 10.73.1.118:6030 -u arista -p arista --insecure  system ping \
   --destination 172.31.255.0 --count 2 --do-not-resolve
```

Output:

```shell
WARN[0000] "10.73.1.118:6030" could not lookup hostname: lookup 118.1.73.10.in-addr.arpa. on 127.0.0.53:53: no such host
source: "172.31.255.0"
time: 31200000
bytes: 64
sequence: 1
ttl: 63
source: "172.31.255.0"
time: 33900000
bytes: 64
sequence: 2
ttl: 63
source: "172.31.255.0"
time: 1001000000
sent: 2
received: 2
min_time: 31251000
avg_time: 32590000
max_time: 33930000
std_dev: 1351000
```

```shell
 gnoic -a 10.73.1.118:6030 -u arista -p arista --insecure  system traceroute \
    --destination 172.31.255.0 --do-not-resolve
```

Output:

```shell
WARN[0000] "10.73.1.118:6030" could not lookup hostname: lookup 118.1.73.10.in-addr.arpa. on 127.0.0.53:53: no such host
destination_name: "172.31.255.0"
destination_address: "172.31.255.0"
hops: 30
packet_size: 60
hop: 1
address: "10.90.90.1"
rtt: 21440000
hop: 1
address: "10.90.90.1"
rtt: 23011000
hop: 1
address: "10.90.90.1"
rtt: 31135000
hop: 2
address: "172.31.255.0"
rtt: 62216000
hop: 2
address: "172.31.255.0"
rtt: 63213000
hop: 2
address: "172.31.255.0"
rtt: 71079000
```

```shell
gnoic -a 10.73.1.118:6030 -u arista -p arista --insecure cert can-generate-csr
```

Output:

```shell
WARN[0000] "10.73.1.118:6030" could not lookup hostname: lookup 118.1.73.10.in-addr.arpa. on 127.0.0.53:53: no such host
INFO[0000] "10.73.1.118:6030" key-type=KT_RSA, cert-type=CT_X509, key-size=2048: can_generate: true
+------------------+------------------+
|   Target Name    | Can Generate CSR |
+------------------+------------------+
| 10.73.1.118:6030 | true             |
+------------------+------------------+
```
