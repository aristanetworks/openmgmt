---
layout: default
title: "gNOIc examples"
date: 2021-07-16 12:17:00 --0600
categories:
---
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
   ip address 192.0.2.118/24

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
$ ssh arista@192.0.2.118
Password:
Last login: Thu Jun  3 12:06:25 2021 from 192.0.2.3
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
Connection to 192.0.2.118 closed.
```

## gNOI demo with Arista using gNOIc

### gNOI Ping

```shell
gnoic -a 192.0.2.118:6030 -u arista -p arista --insecure  system ping \
   --destination 172.31.255.0 --count 2 --do-not-resolve
```

Output:

```shell
WARN[0000] "192.0.2.118:6030" could not lookup hostname: lookup 118.1.73.10.in-addr.arpa. on 127.0.0.53:53: no such host
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

### gNOI Traceroute

```shell
 gnoic -a 192.0.2.118:6030 -u arista -p arista --insecure  system traceroute \
    --destination 172.31.255.0 --do-not-resolve
```

Output:

```shell
WARN[0000] "192.0.2.118:6030" could not lookup hostname: lookup 118.1.73.10.in-addr.arpa. on 127.0.0.53:53: no such host
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

### gNOI cert

```shell
gnoic -a 192.0.2.118:6030 -u arista -p arista --insecure cert can-generate-csr
```

Output:

```shell
WARN[0000] "192.0.2.118:6030" could not lookup hostname: lookup 118.1.73.10.in-addr.arpa. on 127.0.0.53:53: no such host
INFO[0000] "192.0.2.118:6030" key-type=KT_RSA, cert-type=CT_X509, key-size=2048: can_generate: true
+------------------+------------------+
|   Target Name    | Can Generate CSR |
+------------------+------------------+
| 192.0.2.118:6030 | true             |
+------------------+------------------+
```

### Upgrading EOS using gNOI

EOS supports gNOI OS Install/Activate/Verification (4.24.2F+) and gNOI System Reboot/Reboot/RebootStatus (4.27.0F+)
that can be used to upload the EOS image, activate that image (set the boot-config) so that it boots with it next time,
verify the image activation was successful and lastly to reboot the device to perform the upgrade.

#### gNOI OS Install

To upload an EOS SWI image to a switch we can use the `gnoi.os.OS/Installation` RPC:

```shell
gnoic -a 192.0.2.1:6030 --insecure  --gzip -u admin -p admin \
   os install \
   --version 4.29.1F \
   --pkg EOS.swi
```

Output:

```shell
INFO[0000] starting install RPC
INFO[0000] target "192.0.2.1:6030": starting Install stream
INFO[0003] target "192.0.2.1:6030": TransferProgress bytes_received:5242880
INFO[0003] target "192.0.2.1:6030": TransferProgress bytes_received:10485760
...
INFO[0411] target "192.0.2.1:6030": TransferProgress bytes_received:1030750208
INFO[0413] target "192.0.2.1:6030": sending TransferEnd
INFO[0413] target "192.0.2.1:6030": TransferProgress bytes_received:1035993088
INFO[0413] target "192.0.2.1:6030": TransferContent done...
```

#### gNOI OS Activate

To activate the new EOS image (equivalent to running `boot system flash:EOS.swi` on the CLI) we can use  the
`/gnoi.os.OS/Activation` RPC:

```shell
gnoic -a 192.0.2.1:6030 --insecure  --gzip -u admin -p admin \
   os activate \
   --version 4.29.1F \
   --no-reboot
```

Output:

```shell
INFO[0034] target "192.0.2.1:6030" activate response "activate_ok:{}"
```

#### gNOI OS Verify

```shell
gnoic -a 192.0.2.1:6030 --insecure  --gzip -u admin -p admin os verify
```

Output:

```shell
+-------------------+---------+---------------------+
|    Target Name    | Version | Activation Fail Msg |
+-------------------+---------+---------------------+
| 192.0.2.1:6030 | 4.29.1F |                     |
+-------------------+---------+---------------------+
```

#### gNOI System Reboot

To reboot the device we can use `gnoi.system.System/Reboot` RPC and the `COLD` method:

```shell
gnoic -a 192.0.2.1:6030 --insecure  --gzip -u admin -p admin \
   system reboot \
   --method COLD
```

> Note on older EOS versions you may get the following error message:

```shell
ERRO[0009] "192.0.2.1:6030" System Reboot failed: rpc error: code = Unavailable desc = error reading from server: EOF
Error: there was 1 error(s)
```

## References

[gNOI Support](https://www.arista.com/en/support/toi/eos-4-24-2f/14715-gnoi)
