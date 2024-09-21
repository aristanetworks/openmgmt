# om-pe12 Commands Output

## Table of Contents

- [show lldp neighbors](#show-lldp-neighbors)
- [show ip interface brief](#show-ip-interface-brief)
- [show interfaces description](#show-interfaces-description)
- [show version](#show-version)
- [show running-config](#show-running-config)
## show interfaces description

```
Interface                      Status         Protocol           Description
Et1                            up             up                 
Et2                            up             up                 
Et3                            up             up                 
Et4                            up             up                 
Ma0                            up             up
```
## show ip interface brief

```
Address
Interface       IP Address           Status     Protocol         MTU    Owner  
--------------- -------------------- ---------- ------------- --------- -------
Management0     172.144.100.5/24     up         up              1500
```
## show lldp neighbors

```
Last table change time   : 0:03:29 ago
Number of table inserts  : 11
Number of table deletes  : 0
Number of table drops    : 0
Number of table age-outs : 0

Port          Neighbor Device ID       Neighbor Port ID    TTL
---------- ------------------------ ---------------------- ---
Et1           om-spine1                Ethernet2           120
Et2           om-spine2                Ethernet2           120
Ma0           client3                  0242.ac90.640a      120
Ma0           om-spine1                Management0         120
Ma0           client2                  0242.ac90.6409      120
Ma0           client1                  0242.ac90.6408      120
Ma0           client4                  0242.ac90.640b      120
Ma0           om-pe11                  Management0         120
Ma0           om-pe21                  Management0         120
Ma0           om-pe22                  Management0         120
Ma0           om-spine2                Management0         120
```
## show running-config

```
! Command: show running-config
! device: om-pe12 (cEOSLab, EOS-4.32.2F-38195967.4322F (engineering build))
!
no aaa root
!
username admin privilege 15 role network-admin secret sha512 $6$fplrvGkhdy0dHX7W$Egkv31d13S5rNNJ1fUL0PNiBCODratyip2yqpFUpQ.sbJrcyhphT3rRcqyz/60gVkhbM0NmOrsbtqh7tujruE1
!
management api http-commands
   protocol https ssl profile eAPI
   no shutdown
   !
   vrf MGMT
      no shutdown
!
no service interface inactive port-id allocation disabled
!
transceiver qsfp default-mode 4x10G
!
service routing protocols model multi-agent
!
hostname om-pe12
!
spanning-tree mode mstp
!
system l1
   unsupported speed action error
   unsupported error-correction action error
!
vrf instance MGMT
!
management api gnmi
   transport grpc MGMT
      vrf MGMT
      notification timestamp send-time
   !
   transport grpc default
      notification timestamp send-time
   provider eos-native
!
management security
   ssl profile eAPI
      cipher-list HIGH:!eNULL:!aNULL:!MD5:!ADH:!ANULL
      certificate eAPI.crt key eAPI.key
!
interface Ethernet1
!
interface Ethernet2
!
interface Ethernet3
!
interface Ethernet4
!
interface Management0
   description oob_management
   vrf MGMT
   ip address 172.144.100.5/24
   ipv6 address 2001:172:144:100::7/80
!
no ip routing
no ip routing vrf MGMT
!
ip route vrf MGMT 0.0.0.0/0 172.144.100.1
!
ipv6 route vrf MGMT ::/0 2001:172:144:100::1
!
router multicast
   ipv4
      software-forwarding kernel
   !
   ipv6
      software-forwarding kernel
!
end
```
## show version

```
Arista cEOSLab
Hardware version: 
Serial number: OMLEAF2
Hardware MAC address: 001c.aaab.aa12
System MAC address: 001c.aaab.aa12

Software image version: 4.32.2F-38195967.4322F (engineering build)
Architecture: x86_64
Internal build version: 4.32.2F-38195967.4322F
Internal build ID: 47416e3e-5279-42fe-a5bd-cf7624a68bb9
Image format version: 1.0
Image optimization: None

Kernel version: 6.8.7-1.el7.elrepo.x86_64

Uptime: 4 minutes
Total memory: 65442240 kB
Free memory: 3337740 kB
```
