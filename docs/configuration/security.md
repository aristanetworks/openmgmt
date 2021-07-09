---
layout: default
title: "Securing Management Services"
date: 2021-03-02 12:17:00 --0600
categories:
---

## Changing Default Service Ports

When changing the default ports one has to make sure they are also allowed in the control-plane ACL. The default
control-plane ACL cannot be modified, so a new one has to be created and applied under `system control-plane` (EOS
`4.23+`) or `control-plane` (pre-EOS `4.23`). The fastest way to do this is to clone the existing control-plane and add
new permit rules.

### Example

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

2\. There are multiple ways to quickly edit and remove the unnecessary match
   outputs, in this example we'll use `sed` on EOS. Save the file to `/mnt/flash`:

`show ip access-lists  default-control-plane-acl | redirect flash:cpacl.txt`

3\. Enter bash: `#bash`

4\. Go to `/mnt/flash` and remove the match outputs

```shell
cd /mnt/flash
sudo sed -i  "s/\[.*//g" cpacl.txt
```

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
