---
layout: default
title: "pyang examples"
date: 2021-07-16 12:17:00 --0600
categories:
---

## About Pyang

pyang is a python program.

We can use it to:

- Validate YANG modules against YANG RFCs
- Convert YANG modules into equivalent YIN module (XML)
- Generate a tree representation of YANG models for quick visualization

## Install Pyang

```shell
pip install pyang
pip3 freeze | grep pyang
```

```shell
pip3 freeze | grep pyang
```

## We need yang modules

### Create a directory

```shell
mkdir yang_modules
```

### Clone the OpenConfig repository

```shell
git clone https://github.com/openconfig/public.git
```
```
ls public
```

### Copy all the YANG files from OpenConfig to the yang_modules directory

```shell
cp public/release/models/*.yang yang_modules/.
cp -R public/release/models/*/*.yang yang_modules/.
cp public/third_party/ietf/*.yang yang_modules/.
```

### Move to the yang_modules directory

It has all the YANG files published on the OpenConfig repository

```shell
cd yang_modules/
ls
```

## Validate YANG modules

```shell
pyang openconfig-bgp.yang
pyang openconfig-interfaces.yang
```

### Convert a YANG module into an equivalent YIN module

A YANG module can be translated into an XML syntax called YIN. The translated module is called a YIN module. The YANG and YIN formats contain equivalent information using different notations: YIN is YANG in XML. A YANG module can be translated into YIN syntax without losing any information.

Example (openconfig-bgp.yin is the YIN equivalent of openconfig-bgp.yang)

```shell
pyang openconfig-bgp.yang -f yin -o openconfig-bgp.yin
ls *.yin
```
### Generate a tree representation of YANG modules for quick visualization

```shell
pyang openconfig-interfaces.yang -f tree
```
<details>
<summary> Reveal output</summary>
<p>

```shell
module: openconfig-interfaces
  +--rw interfaces
     +--rw interface* [name]
        +--rw name             -> ../config/name
        +--rw config
        |  +--rw name?            string
        |  +--rw type             identityref
        |  +--rw mtu?             uint16
        |  +--rw loopback-mode?   boolean
        |  +--rw description?     string
        |  +--rw enabled?         boolean
        +--ro state
        |  +--ro name?            string
        |  +--ro type             identityref
        |  +--ro mtu?             uint16
        |  +--ro loopback-mode?   boolean
        |  +--ro description?     string
        |  +--ro enabled?         boolean
        |  +--ro ifindex?         uint32
        |  +--ro admin-status     enumeration
        |  +--ro oper-status      enumeration
        |  +--ro last-change?     oc-types:timeticks64
        |  +--ro logical?         boolean
        |  +--ro management?      boolean
        |  +--ro cpu?             boolean
        |  +--ro counters
        |     +--ro in-octets?             oc-yang:counter64
        |     +--ro in-pkts?               oc-yang:counter64
        |     +--ro in-unicast-pkts?       oc-yang:counter64
        |     +--ro in-broadcast-pkts?     oc-yang:counter64
        |     +--ro in-multicast-pkts?     oc-yang:counter64
        |     +--ro in-discards?           oc-yang:counter64
        |     +--ro in-errors?             oc-yang:counter64
        |     +--ro in-unknown-protos?     oc-yang:counter64
        |     +--ro in-fcs-errors?         oc-yang:counter64
        |     +--ro out-octets?            oc-yang:counter64
        |     +--ro out-pkts?              oc-yang:counter64
        |     +--ro out-unicast-pkts?      oc-yang:counter64
        |     +--ro out-broadcast-pkts?    oc-yang:counter64
        |     +--ro out-multicast-pkts?    oc-yang:counter64
        |     +--ro out-discards?          oc-yang:counter64
        |     +--ro out-errors?            oc-yang:counter64
        |     +--ro carrier-transitions?   oc-yang:counter64
        |     +--ro last-clear?            oc-types:timeticks64
        +--rw hold-time
        |  +--rw config
        |  |  +--rw up?     uint32
        |  |  +--rw down?   uint32
        |  +--ro state
        |     +--ro up?     uint32
        |     +--ro down?   uint32
        +--rw subinterfaces
           +--rw subinterface* [index]
              +--rw index     -> ../config/index
              +--rw config
              |  +--rw index?         uint32
              |  +--rw description?   string
              |  +--rw enabled?       boolean
              +--ro state
                 +--ro index?          uint32
                 +--ro description?    string
                 +--ro enabled?        boolean
                 +--ro name?           string
                 +--ro ifindex?        uint32
                 +--ro admin-status    enumeration
                 +--ro oper-status     enumeration
                 +--ro last-change?    oc-types:timeticks64
                 +--ro logical?        boolean
                 +--ro management?     boolean
                 +--ro cpu?            boolean
                 +--ro counters
                    +--ro in-octets?             oc-yang:counter64
                    +--ro in-pkts?               oc-yang:counter64
                    +--ro in-unicast-pkts?       oc-yang:counter64
                    +--ro in-broadcast-pkts?     oc-yang:counter64
                    +--ro in-multicast-pkts?     oc-yang:counter64
                    +--ro in-discards?           oc-yang:counter64
                    +--ro in-errors?             oc-yang:counter64
                    +--ro in-unknown-protos?     oc-yang:counter64
                    +--ro in-fcs-errors?         oc-yang:counter64
                    +--ro out-octets?            oc-yang:counter64
                    +--ro out-pkts?              oc-yang:counter64
                    +--ro out-unicast-pkts?      oc-yang:counter64
                    +--ro out-broadcast-pkts?    oc-yang:counter64
                    +--ro out-multicast-pkts?    oc-yang:counter64
                    +--ro out-discards?          oc-yang:counter64
                    +--ro out-errors?            oc-yang:counter64
                    +--ro carrier-transitions?   oc-yang:counter64
                    +--ro last-clear?            oc-types:timeticks64
```
</p>
</details>

```shell
pyang openconfig-interfaces.yang -f tree --tree-path=/interfaces/interface/state
```
<details>
<summary> Reveal output</summary>
<p>

```shell
module: openconfig-interfaces
  +--rw interfaces
     +--rw interface* [name]
        +--ro state
           +--ro name?            string
           +--ro type             identityref
           +--ro mtu?             uint16
           +--ro loopback-mode?   boolean
           +--ro description?     string
           +--ro enabled?         boolean
           +--ro ifindex?         uint32
           +--ro admin-status     enumeration
           +--ro oper-status      enumeration
           +--ro last-change?     oc-types:timeticks64
           +--ro logical?         boolean
           +--ro management?      boolean
           +--ro cpu?             boolean
           +--ro counters
              +--ro in-octets?             oc-yang:counter64
              +--ro in-pkts?               oc-yang:counter64
              +--ro in-unicast-pkts?       oc-yang:counter64
              +--ro in-broadcast-pkts?     oc-yang:counter64
              +--ro in-multicast-pkts?     oc-yang:counter64
              +--ro in-discards?           oc-yang:counter64
              +--ro in-errors?             oc-yang:counter64
              +--ro in-unknown-protos?     oc-yang:counter64
              +--ro in-fcs-errors?         oc-yang:counter64
              +--ro out-octets?            oc-yang:counter64
              +--ro out-pkts?              oc-yang:counter64
              +--ro out-unicast-pkts?      oc-yang:counter64
              +--ro out-broadcast-pkts?    oc-yang:counter64
              +--ro out-multicast-pkts?    oc-yang:counter64
              +--ro out-discards?          oc-yang:counter64
              +--ro out-errors?            oc-yang:counter64
              +--ro carrier-transitions?   oc-yang:counter64
              +--ro last-clear?            oc-types:timeticks64
```
</p>
</details>

```shell
pyang openconfig-interfaces.yang -f tree --tree-depth=4
```
<details>
<summary> Reveal output</summary>
<p>

```shell
module: openconfig-interfaces
  +--rw interfaces
     +--rw interface* [name]
        +--rw name             -> ../config/name
        +--rw config
        |  +--rw name?            string
        |  +--rw type             identityref
        |  +--rw mtu?             uint16
        |  +--rw loopback-mode?   boolean
        |  +--rw description?     string
        |  +--rw enabled?         boolean
        +--ro state
        |  +--ro name?            string
        |  +--ro type             identityref
        |  +--ro mtu?             uint16
        |  +--ro loopback-mode?   boolean
        |  +--ro description?     string
        |  +--ro enabled?         boolean
        |  +--ro ifindex?         uint32
        |  +--ro admin-status     enumeration
        |  +--ro oper-status      enumeration
        |  +--ro last-change?     oc-types:timeticks64
        |  +--ro logical?         boolean
        |  +--ro management?      boolean
        |  +--ro cpu?             boolean
        |  +--ro counters
        |        ...
        +--rw hold-time
        |  +--rw config
        |  |     ...
        |  +--ro state
        |        ...
        +--rw subinterfaces
           +--rw subinterface* [index]
                 ...
```
</p>
</details>

```shell
pyang openconfig-bgp.yang -f tree --tree-path=/bgp/neighbors --tree-depth=4
```
<details>
<summary> Reveal output</summary>
<p>

```shell
module: openconfig-bgp
  +--rw bgp
     +--rw neighbors
        +--rw neighbor* [neighbor-address]
           +--rw neighbor-address      -> ../config/neighbor-address
           +--rw config
           |     ...
           +--ro state
           |     ...
           +--rw timers
           |     ...
           +--rw transport
           |     ...
           +--rw error-handling
           |     ...
           +--rw graceful-restart
           |     ...
           +--rw logging-options
           |     ...
           +--rw ebgp-multihop
           |     ...
           +--rw route-reflector
           |     ...
           +--rw as-path-options
           |     ...
           +--rw use-multiple-paths
           |     ...
           +--rw apply-policy
           |     ...
           +--rw afi-safis
           |     ...
           +--rw enable-bfd
```
</p>
</details>

```shell
pyang openconfig-bgp.yang -f tree --tree-path=/bgp/neighbors/neighbor/config
```
<details>
<summary> Reveal output</summary>
<p>

```shell
module: openconfig-bgp
  +--rw bgp
     +--rw neighbors
        +--rw neighbor* [neighbor-address]
           +--rw config
              +--rw peer-group?           -> ../../../../peer-groups/peer-group/peer-group-name
              +--rw neighbor-address?     oc-inet:ip-address
              +--rw enabled?              boolean
              +--rw peer-as?              oc-inet:as-number
              +--rw local-as?             oc-inet:as-number
              +--rw peer-type?            oc-bgp-types:peer-type
              +--rw auth-password?        oc-types:routing-password
              +--rw remove-private-as?    oc-bgp-types:remove-private-as-option
              +--rw route-flap-damping?   boolean
              +--rw send-community?       oc-bgp-types:community-type
              +--rw description?          string
```
</p>
</details>

```shell
pyang openconfig-bgp.yang -f tree --tree-path=/bgp/neighbors/neighbor/state \
    --tree-depth=5
```
<details>
<summary> Reveal output</summary>
<p>

```shell
module: openconfig-bgp
  +--rw bgp
     +--rw neighbors
        +--rw neighbor* [neighbor-address]
           +--ro state
              +--ro peer-group?                -> ../../../../peer-groups/peer-group/peer-group-name
              +--ro neighbor-address?          oc-inet:ip-address
              +--ro enabled?                   boolean
              +--ro peer-as?                   oc-inet:as-number
              +--ro local-as?                  oc-inet:as-number
              +--ro peer-type?                 oc-bgp-types:peer-type
              +--ro auth-password?             oc-types:routing-password
              +--ro remove-private-as?         oc-bgp-types:remove-private-as-option
              +--ro route-flap-damping?        boolean
              +--ro send-community?            oc-bgp-types:community-type
              +--ro description?               string
              +--ro session-state?             enumeration
              +--ro last-established?          oc-types:timeticks64
              +--ro established-transitions?   oc-yang:counter64
              +--ro supported-capabilities*    identityref
              +--ro messages
              |     ...
              +--ro queues
              |     ...
              +--ro dynamically-configured?    boolean
```
</p>
</details>

```shell
pyang openconfig-bgp.yang -f tree --tree-path=/bgp/neighbors/neighbor/afi-safis \
   --tree-depth=6
```
<details>
<summary> Reveal output</summary>
<p>

```shell
module: openconfig-bgp
  +--rw bgp
     +--rw neighbors
        +--rw neighbor* [neighbor-address]
           +--rw afi-safis
              +--rw afi-safi* [afi-safi-name]
                 +--rw afi-safi-name           -> ../config/afi-safi-name
                 +--rw config
                 |     ...
                 +--ro state
                 |     ...
                 +--rw graceful-restart
                 |     ...
                 +--rw add-paths
                 |     ...
                 +--rw apply-policy
                 |     ...
                 +--rw ipv4-unicast
                 |     ...
                 +--rw ipv6-unicast
                 |     ...
                 +--rw ipv4-labeled-unicast
                 |     ...
                 +--rw ipv6-labeled-unicast
                 |     ...
                 +--rw l3vpn-ipv4-unicast
                 |     ...
                 +--rw l3vpn-ipv6-unicast
                 |     ...
                 +--rw l3vpn-ipv4-multicast
                 |     ...
                 +--rw l3vpn-ipv6-multicast
                 |     ...
                 +--rw l2vpn-vpls
                 |     ...
                 +--rw l2vpn-evpn
                 |     ...
                 +--rw srte-policy-ipv4
                 |     ...
                 +--rw srte-policy-ipv6
                 |     ...
                 +--rw use-multiple-paths
```
</p>
</details>
