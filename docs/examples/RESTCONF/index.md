---
layout: default
title: "RESTCONF"
date: 2021-07-16 08:17:00 --0600
categories:
---

RESTCONF examples with EOS

## About RESTCONF

RESTCONF is defined in the [RFC 8040](https://datatracker.ietf.org/doc/html/rfc8040)

- The GET method is sent by the client to retrieve data for a resource.
- The HEAD method is sent by the client to retrieve just the header fields (which contain the metadata for a resource)
that would be returned for the comparable GET method, without the response message-body.
It is supported for all resources that support the GET method.
- The POST method is sent by the client to create a data resource.
- The PUT method is sent by the client to create or replace the target data resource.
- The DELETE method is used to delete the target resource.

## EOS configuration

Please refer to [this link](../../configuration/restconf.md)

## Requirement on the RESTCONF client

```shell
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install jq -y
pip install requests
```

```shell
pip3 freeze | grep requests
```

## RESTCONF examples

## GET

### Using cURL

```shell
curl -s GET 'https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/config/description' \
      --header 'Accept: application/yang-data+json' -u arista:arista  --insecure
```

output

```javascript
{"openconfig-interfaces:description":"P2P_LINK_TO_DC1-SPINE1_Ethernet1"}
```

```shell
curl -s GET 'https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1' \
      --header 'Accept: application/yang-data+json' -u arista:arista  \
      --insecure | jq .'"openconfig-interfaces:state".counters."in-octets"'
```

output

```text
"48284395"
```

```shell
curl -s GET 'https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces' \
     --header 'Accept: application/yang-data+json' -u arista:arista \
     --insecure | jq .'"openconfig-interfaces:interface"[2].name'
```

output

```text
"Ethernet1"
```

```shell
curl -X GET https://10.73.1.105:6020/restconf/data/system \
    --header 'Accept: application/yang-data+json' -u arista:arista \
    --insecure | jq .'"openconfig-system:config".hostname'
```

output

```text
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 66151    0 66151    0     0   284k      0 --:--:-- --:--:-- --:--:--  284k
"switch1"
```

### Using Python

```python
$ python3
Python 3.6.9 (default, Jan 26 2021, 15:33:00)
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> from requests.auth import HTTPBasicAuth
>>> import json
>>> USER = 'arista'
>>> PASS = 'arista'
>>> requests.packages.urllib3.disable_warnings()
>>> headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}
>>> headers = {'Accept': 'application/yang-data+json'}
>>> api_call = "https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/state"
>>> result = requests.get(api_call, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False)
>>> result.status_code
200
>>> result.ok
True
>>> result.url
'https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/state'
>>> result.content
b'{"openconfig-interfaces:admin-status":"UP","openconfig-interfaces:counters":{"in-broadcast-pkts":"0","in-discards":"0","in-errors":"0","in-fcs-errors":"0","in-multicast-pkts":"972","in-octets":"116602","in-unicast-pkts":"131","out-broadcast-pkts":"1","out-discards":"0","out-errors":"0","out-multicast-pkts":"1761","out-octets":"199997","out-unicast-pkts":"122"},"openconfig-interfaces:description":"restconf_test","openconfig-interfaces:enabled":true,"openconfig-platform-port:hardware-port":"Port1","openconfig-interfaces:ifindex":1,"arista-intf-augments:inactive":false,"openconfig-interfaces:last-change":"1624966430515012864","openconfig-interfaces:loopback-mode":false,"openconfig-interfaces:mtu":0,"openconfig-interfaces:name":"Ethernet1","openconfig-interfaces:oper-status":"UP","openconfig-vlan:tpid":"openconfig-vlan-types:TPID_0X8100","openconfig-interfaces:type":"iana-if-type:ethernetCsmacd"}\n'
>>> result.json()
{'openconfig-interfaces:admin-status': 'UP', 'openconfig-interfaces:counters': {'in-broadcast-pkts': '0', 'in-discards': '0', 'in-errors': '0', 'in-fcs-errors': '0', 'in-multicast-pkts': '972', 'in-octets': '116602', 'in-unicast-pkts': '131', 'out-broadcast-pkts': '1', 'out-discards': '0', 'out-errors': '0', 'out-multicast-pkts': '1761', 'out-octets': '199997', 'out-unicast-pkts': '122'}, 'openconfig-interfaces:description': 'restconf_test', 'openconfig-interfaces:enabled': True, 'openconfig-platform-port:hardware-port': 'Port1', 'openconfig-interfaces:ifindex': 1, 'arista-intf-augments:inactive': False, 'openconfig-interfaces:last-change': '1624966430515012864', 'openconfig-interfaces:loopback-mode': False, 'openconfig-interfaces:mtu': 0, 'openconfig-interfaces:name': 'Ethernet1', 'openconfig-interfaces:oper-status': 'UP', 'openconfig-vlan:tpid': 'openconfig-vlan-types:TPID_0X8100', 'openconfig-interfaces:type': 'iana-if-type:ethernetCsmacd'}
>>> result.json()['openconfig-interfaces:oper-status']
'UP'
>>> result.json()['openconfig-interfaces:counters']['out-octets']
'199997'
>>> exit()
```

Execute the python script [get.py](https://github.com/aristanetworks/openmgmt/tree/main/src/restconf/get.py)

```shell
python3 get.py
```

output

```javascript
{'arista-intf-augments:inactive': False,
 'openconfig-interfaces:admin-status': 'UP',
 'openconfig-interfaces:counters': {'in-broadcast-pkts': '0',
                                    'in-discards': '0',
                                    'in-errors': '0',
                                    'in-fcs-errors': '0',
                                    'in-multicast-pkts': '1762',
                                    'in-octets': '202553',
                                    'in-unicast-pkts': '183',
                                    'out-broadcast-pkts': '1',
                                    'out-discards': '0',
                                    'out-errors': '0',
                                    'out-multicast-pkts': '2552',
                                    'out-octets': '284793',
                                    'out-unicast-pkts': '174'},
 'openconfig-interfaces:description': 'restconf_test',
 'openconfig-interfaces:enabled': True,
 'openconfig-interfaces:ifindex': 1,
 'openconfig-interfaces:last-change': '1624966430515012864',
 'openconfig-interfaces:loopback-mode': False,
 'openconfig-interfaces:mtu': 0,
 'openconfig-interfaces:name': 'Ethernet1',
 'openconfig-interfaces:oper-status': 'UP',
 'openconfig-interfaces:type': 'iana-if-type:ethernetCsmacd',
 'openconfig-platform-port:hardware-port': 'Port1',
 'openconfig-vlan:tpid': 'openconfig-vlan-types:TPID_0X8100'}
```

## HEAD

### Using cURL

```shell
curl --head 'https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1' \
    --header 'Accept: application/yang-data+json' -u arista:arista  --insecure
```

output

```shell
HTTP/1.1 200 OK
Content-Type: application/yang.data+json
Date: Sun, 04 Jul 2021 14:20:39 GMT
```

### Using Python

Execute the python script [head.py](https://github.com/aristanetworks/openmgmt/tree/main/src/restconf/head.py)

```shell
python3 head.py
```

output

```shell
url is https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/state
status_code is 200
headers are {'Content-Type': 'application/yang.data+json', 'Date': 'Sun, 18 Jul 2021 08:49:52 GMT'}
content is b''
```

## PUT

### Using cURL

#### Interface configuration example

Let's check before the change

```shell
curl -s GET 'https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4/config' \
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
curl -X PUT https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4/config \
   -H 'Content-Type: application/json' -u arista:arista -d @interface.json  --insecure
```

output

```javascript
{"openconfig-interfaces:description":"restconf_test","openconfig-interfaces:enabled":true,"openconfig-interfaces:name":"Ethernet4"}
```

Let's verify after the change

```shell
curl -s GET 'https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4/config' \
   --header 'Accept: application/yang-data+json' -u arista:arista  --insecure
```

output

```javascript
{"openconfig-interfaces:description":"restconf_test","openconfig-interfaces:enabled":true,"arista-intf-augments:load-interval":300,"openconfig-interfaces:loopback-mode":false,"openconfig-interfaces:mtu":0,"openconfig-interfaces:name":"Ethernet4","openconfig-vlan:tpid":"openconfig-vlan-types:TPID_0X8100","openconfig-interfaces:type":"iana-if-type:ethernetCsmacd"}
```

```shell
curl -s GET 'https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4/config' \
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
curl -X GET https://10.73.1.105:6020/restconf/data/system/config \
   --header 'Accept: application/yang-data+json' -u arista:arista  --insecure
```

output

```javascript
{"openconfig-system:hostname":"DC1-LEAF1A"}
```

```shell
curl -X GET https://10.73.1.105:6020/restconf/data/system \
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
curl -X PUT https://10.73.1.105:6020/restconf/data/system/config \
      -H 'Content-Type: application/json' -u arista:arista \
      -d '{"openconfig-system:hostname":"test"}'  --insecure
```

output

```javascript
{"openconfig-system:hostname":"test"}
```

Let's verify after the change

```shell
curl -X GET https://10.73.1.105:6020/restconf/data/system/config \
      --header 'Accept: application/yang-data+json' -u arista:arista  --insecure
```

output

```javascript
{"openconfig-system:hostname":"test"}
```

## POST

### Using cURL

#### Interface configuration example

Let's check before the change

```shell
curl -s GET 'https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4' \
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
curl -X POST https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4/config \
   -H 'Content-Type: application/json' -u arista:arista \
   -d '{"openconfig-interfaces:description":"restconf_test"}' --insecure
```

output

```shell
{"openconfig-interfaces:description":"restconf_test"}
```

```shell
curl -X POST https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4/config \
    -H 'Content-Type: application/json' -u arista:arista \
    -d '{"openconfig-interfaces:enabled":false}'  --insecure
```

output

```shell
{"openconfig-interfaces:enabled":false}
```

Let's verify after the change

```shell
curl -s GET 'https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4' \
   --header 'Accept: application/yang-data+json' -u arista:arista \
   --insecure | jq .'"openconfig-interfaces:config".description'
```

output

```text
"restconf_test"
```

```shell
curl -s GET 'https://10.73.1.105:6020/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet4' \
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

## DELETE

### Using cURL

Let's check before the change

```shell
curl -s GET 'https://10.73.1.105:6020/restconf/data/ietf-interfaces:interfaces/interface=Loopback100' \
      --header 'Accept: application/yang-data+json' -u arista:arista  --insecure
```

output

```javascript
{"openconfig-interfaces:config":{"description":"test","enabled":true,"arista-intf-augments:load-interval":300,"loopback-mode":true,"name":"Loopback100","openconfig-vlan:tpid":"openconfig-vlan-types:TPID_0X8100","type":"iana-if-type:softwareLoopback"},"openconfig-interfaces:hold-time":{"config":{"down":0,"up":0},"state":{"down":0,"up":0}},"openconfig-interfaces:name":"Loopback100","openconfig-interfaces:state":{"enabled":true,"loopback-mode":false,"openconfig-vlan:tpid":"openconfig-vlan-types:TPID_0X8100"},"openconfig-interfaces:subinterfaces":{"subinterface":[{"config":{"description":"test","enabled":true,"index":0},"index":0,"openconfig-if-ip:ipv4":{"config":{"dhcp-client":false,"enabled":true,"mtu":1500},"state":{"dhcp-client":false,"enabled":true,"mtu":1500}},"openconfig-if-ip:ipv6":{"config":{"dhcp-client":false,"enabled":false,"mtu":1500},"state":{"dhcp-client":false,"enabled":false,"mtu":1500}},"state":{"enabled":true,"index":0}}]}}
```

```shell
curl -X DELETE https://10.73.1.105:6020/restconf/data/ietf-interfaces:interfaces/interface=Loopback100 \
    -u arista:arista  --insecure
```

### Using Python

Execute the python script [delete.py](https://github.com/aristanetworks/openmgmt/tree/main/src/restconf/delete.py)

```shell
python3 delete.py
```

output

```shell
get int lo100
status_code is 200
content is {'openconfig-interfaces:config': {'description': '222', 'enabled': True, 'arista-intf-augments:load-interval': 300, 'loopback-mode': True, 'name': 'Loopback100', 'openconfig-vlan:tpid': 'openconfig-vlan-types:TPID_0X8100', 'type': 'iana-if-type:softwareLoopback'}, 'openconfig-interfaces:hold-time': {'config': {'down': 0, 'up': 0}, 'state': {'down': 0, 'up': 0}}, 'openconfig-interfaces:name': 'Loopback100', 'openconfig-interfaces:state': {'enabled': True, 'loopback-mode': False, 'openconfig-vlan:tpid': 'openconfig-vlan-types:TPID_0X8100'}, 'openconfig-interfaces:subinterfaces': {'subinterface': [{'config': {'description': '222', 'enabled': True, 'index': 0}, 'index': 0, 'openconfig-if-ip:ipv4': {'config': {'dhcp-client': False, 'enabled': True, 'mtu': 1500}, 'state': {'dhcp-client': False, 'enabled': True, 'mtu': 1500}}, 'openconfig-if-ip:ipv6': {'config': {'dhcp-client': False, 'enabled': False, 'mtu': 1500}, 'state': {'dhcp-client': False, 'enabled': False, 'mtu': 1500}}, 'state': {'enabled': True, 'index': 0}}]}}
deleting int lo100
status_code is 200
```
