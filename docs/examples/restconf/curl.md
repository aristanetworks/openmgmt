---
layout: default
title: "RESTCONF with cURL"
date: 2021-07-16 08:17:00 --0600
categories:
---


## Requirement on the RESTCONF client

```shell
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install curl jq -y
```

## RESTCONF examples using cURL

### GET

#### Get interface description for Ethernet1

```shell
curl -s GET 'https://192.0.2.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/config/description' \
      --header 'Accept: application/yang-data+json' -u arista:arista  --insecure
```

Output:

```javascript
{"openconfig-interfaces:description":"P2P_LINK_TO_DC1-SPINE1_Ethernet1"}
```

#### Get interface stats for Ethernet1 and output the "in-octets" using jq

```shell
curl -s GET 'https://192.0.2.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1' \
      --header 'Accept: application/yang-data+json' -u arista:arista  \
      --insecure | jq .'"openconfig-interfaces:state".counters."in-octets"'
```

Output:

```text
"48284395"
```

#### Get interfaces stats and output the name of the 2nd (3rd index) using jq

```shell
curl -s GET 'https://192.0.2.105:6020/restconf/data/openconfig-interfaces:interfaces' \
     --header 'Accept: application/yang-data+json' -u arista:arista \
     --insecure | jq .'"openconfig-interfaces:interface"[2].name'
```

Output:

```text
"Ethernet1"
```

#### Get the system information and parse the hostname using jq

```shell
curl -X GET https://192.0.2.105:6020/restconf/data/system \
    --header 'Accept: application/yang-data+json' -u arista:arista \
    --insecure | jq .'"openconfig-system:config".hostname'
```

Output:

```text
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 66151    0 66151    0     0   284k      0 --:--:-- --:--:-- --:--:--  284k
"switch1"
```

#### Get PfxRcd and PfxAcc stats from a BGP neighbor

```shell
 curl -s GET 'https://192.0.2.100:5900/restconf/data/network-instances/network-instance=default/protocols/protocol=BGP,BGP/bgp/neighbors/neighbor=192.0.2.21/afi-safis/afi-safi=IPV4_UNICAST' \
    --header 'Accept: application/yang-data+json' -u cvpadmin:arastra --insecure | jq
```

Output:

```shell
{
  "openconfig-network-instance:afi-safi-name": "openconfig-bgp-types:IPV4_UNICAST",
  "openconfig-network-instance:config": {
    "afi-safi-name": "openconfig-bgp-types:IPV4_UNICAST"
  },
  "openconfig-network-instance:state": {
    "afi-safi-name": "openconfig-bgp-types:IPV4_UNICAST",
    "prefixes": {
      "arista-bgp-augments:best-ecmp-paths": 0,
      "arista-bgp-augments:best-paths": 0,
      "installed": 7,
      "received": 7,
      "sent": 7
    }
  }
}
```

> NOTE: The protocol must have multiple keys, i.e.: `protocol=BGP,BGP`, in this case, it's the `identifier` and
> the `name` of the protocol, if either of these is omitted; on the switch side in the Octa/OpenConfig agent logs
> an error similar to the following would be generated:
>
> `handler.go:95] ERROR mismatch between number of keys in [identifier name] and values present [BGP]` or
> if both would be omitted the error message would be:
> `handler.go:95] ERROR failed to find key values after element "protocol" in "network-instances/network-instance=default/protocols/protocol`
>
> Tip: [pyang](../pyang/) can be useful to understand what keys each leaf requires, e.g:
>
>```shell
> pyang openconfig-network-instance.yang -f tree --tree-depth=4 | tail -n 4
>        |        ...
>        +--rw protocols
>           +--rw protocol* [identifier name]
>                 ...
>

### HEAD

```shell
curl --head 'https://192.0.2.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1' \
    --header 'Accept: application/yang-data+json' -u arista:arista  --insecure
```

output

```shell
HTTP/1.1 200 OK
Content-Type: application/yang.data+json
Date: Sun, 04 Jul 2021 14:20:39 GMT
```

### PUT

#### Interface configuration example

Let's check before the change

```shell
curl -s GET 'https://192.0.2.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4/config' \
   --header 'Accept: application/yang-data+json' -u arista:arista  --insecure
```

output

```javascript
{"openconfig-interfaces:description":"blabla","openconfig-interfaces:enabled":false,"arista-intf-augments:load-interval":300,"openconfig-interfaces:loopback-mode":false,"openconfig-interfaces:mtu":0,"openconfig-interfaces:name":"Ethernet4","openconfig-vlan:tpid":"openconfig-vlan-types:TPID_0X8100","openconfig-interfaces:type":"iana-if-type:ethernetCsmacd"}
```

Let's use the file [interface.json](https://github.com/aristanetworks/openmgmt/tree/main/src/restconf/interface.json)

```shell
more interface.json
```

output

```javascript
{"enabled":true,"name":"Ethernet4", "description":"restconf_test"}
```

```shell
curl -X PUT https://192.0.2.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4/config \
   -H 'Content-Type: application/json' -u arista:arista -d @interface.json  --insecure
```

output

```javascript
{"openconfig-interfaces:description":"restconf_test","openconfig-interfaces:enabled":true,"openconfig-interfaces:name":"Ethernet4"}
```

Let's verify after the change

```shell
curl -s GET 'https://192.0.2.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4/config' \
   --header 'Accept: application/yang-data+json' -u arista:arista  --insecure
```

output

```javascript
{"openconfig-interfaces:description":"restconf_test","openconfig-interfaces:enabled":true,"arista-intf-augments:load-interval":300,"openconfig-interfaces:loopback-mode":false,"openconfig-interfaces:mtu":0,"openconfig-interfaces:name":"Ethernet4","openconfig-vlan:tpid":"openconfig-vlan-types:TPID_0X8100","openconfig-interfaces:type":"iana-if-type:ethernetCsmacd"}
```

```shell
curl -s GET 'https://192.0.2.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4/config' \
   --header 'Accept: application/yang-data+json' -u arista:arista  --insecure | jq .
```

output

```javascript
{
  "openconfig-interfaces:description": "restconf_test",
  "openconfig-interfaces:enabled": true,
  "arista-intf-augments:load-interval": 300,
  "openconfig-interfaces:loopback-mode": false,
  "openconfig-interfaces:mtu": 0,
  "openconfig-interfaces:name": "Ethernet4",
  "openconfig-vlan:tpid": "openconfig-vlan-types:TPID_0X8100",
  "openconfig-interfaces:type": "iana-if-type:ethernetCsmacd"
}
```

#### Device hostname example

Let's check before the change

```shell
curl -X GET https://192.0.2.105:6020/restconf/data/system/config \
   --header 'Accept: application/yang-data+json' -u arista:arista  --insecure
```

output

```javascript
{"openconfig-system:hostname":"DC1-LEAF1A"}
```

```shell
curl -X GET https://192.0.2.105:6020/restconf/data/system \
   --header 'Accept: application/yang-data+json' -u arista:arista \
   --insecure | jq .'"openconfig-system:config".hostname'
```

output

```text
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 74748    0 74748    0     0   300k      0 --:--:-- --:--:-- --:--:--  300k
"DC1-LEAF1A"
```

```shell
curl -X PUT https://192.0.2.105:6020/restconf/data/system/config \
      -H 'Content-Type: application/json' -u arista:arista \
      -d '{"openconfig-system:hostname":"test"}'  --insecure
```

output

```javascript
{"openconfig-system:hostname":"test"}
```

Let's verify after the change

```shell
curl -X GET https://192.0.2.105:6020/restconf/data/system/config \
      --header 'Accept: application/yang-data+json' -u arista:arista  --insecure
```

output

```javascript
{"openconfig-system:hostname":"test"}
```

### POST

#### Interface configuration example

Let's check before the change

```shell
curl -s GET 'https://192.0.2.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4' \
   --header 'Accept: application/yang-data+json' -u arista:arista \
   --insecure | jq .'"openconfig-interfaces:config"'
```

output

```javascript
{
  "description": "",
  "enabled": true,
  "arista-intf-augments:load-interval": 300,
  "loopback-mode": false,
  "mtu": 0,
  "name": "Ethernet4",
  "openconfig-vlan:tpid": "openconfig-vlan-types:TPID_0X8100",
  "type": "iana-if-type:ethernetCsmacd"
}
```

```shell
curl -X POST https://192.0.2.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4/config \
   -H 'Content-Type: application/json' -u arista:arista \
   -d '{"openconfig-interfaces:description":"restconf_test"}' --insecure
```

output

```shell
{"openconfig-interfaces:description":"restconf_test"}
```

```shell
curl -X POST https://192.0.2.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4/config \
    -H 'Content-Type: application/json' -u arista:arista \
    -d '{"openconfig-interfaces:enabled":false}'  --insecure
```

output

```shell
{"openconfig-interfaces:enabled":false}
```

Let's verify after the change

```shell
curl -s GET 'https://192.0.2.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4' \
   --header 'Accept: application/yang-data+json' -u arista:arista \
   --insecure | jq .'"openconfig-interfaces:config".description'
```

output

```text
"restconf_test"
```

```shell
curl -s GET 'https://192.0.2.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4' \
   --header 'Accept: application/yang-data+json' \
   -u arista:arista  --insecure | jq .'"openconfig-interfaces:config"'
```

output

```javascript
{
  "description": "restconf_test",
  "enabled": false,
  "arista-intf-augments:load-interval": 300,
  "loopback-mode": false,
  "mtu": 0,
  "name": "Ethernet4",
  "openconfig-vlan:tpid": "openconfig-vlan-types:TPID_0X8100",
  "type": "iana-if-type:ethernetCsmacd"
}
```

### DELETE

Let's check before the change

```shell
curl -s GET 'https://192.0.2.105:6020/restconf/data/ietf-interfaces:interfaces/interface=Loopback100' \
      --header 'Accept: application/yang-data+json' -u arista:arista  --insecure
```

output

```javascript
{"openconfig-interfaces:config":{"description":"test","enabled":true,"arista-intf-augments:load-interval":300,"loopback-mode":true,"name":"Loopback100","openconfig-vlan:tpid":"openconfig-vlan-types:TPID_0X8100","type":"iana-if-type:softwareLoopback"},"openconfig-interfaces:hold-time":{"config":{"down":0,"up":0},"state":{"down":0,"up":0}},"openconfig-interfaces:name":"Loopback100","openconfig-interfaces:state":{"enabled":true,"loopback-mode":false,"openconfig-vlan:tpid":"openconfig-vlan-types:TPID_0X8100"},"openconfig-interfaces:subinterfaces":{"subinterface":[{"config":{"description":"test","enabled":true,"index":0},"index":0,"openconfig-if-ip:ipv4":{"config":{"dhcp-client":false,"enabled":true,"mtu":1500},"state":{"dhcp-client":false,"enabled":true,"mtu":1500}},"openconfig-if-ip:ipv6":{"config":{"dhcp-client":false,"enabled":false,"mtu":1500},"state":{"dhcp-client":false,"enabled":false,"mtu":1500}},"state":{"enabled":true,"index":0}}]}}
```

```shell
curl -X DELETE https://192.0.2.105:6020/restconf/data/ietf-interfaces:interfaces/interface=Loopback100 \
    -u arista:arista  --insecure
```
