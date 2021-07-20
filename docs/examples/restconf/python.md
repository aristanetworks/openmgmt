---
layout: default
title: "RESTCONF with Python"
date: 2021-07-16 08:17:00 --0600
categories:
---

## Requirement on the RESTCONF client

```shell
sudo apt-get update
sudo apt-get -y upgrade
pip install requests
```

```shell
pip3 freeze | grep requests
```

## RESTCONF examples with Python

### GET

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

Execute the python script [get_eth1_status.py](https://github.com/aristanetworks/openmgmt/tree/main/src/restconf/get_eth1_status.py)

```shell
python3 get_eth1_status.py
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

### HEAD

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

### DELETE

Execute the python script [delete_lo100.py](https://github.com/aristanetworks/openmgmt/tree/main/src/restconf/delete_lo100.py)

```shell
python3 delete_lo100.py
```

output

```shell
get int lo100
status_code is 200
content is {'openconfig-interfaces:config': {'description': '222', 'enabled': True, 'arista-intf-augments:load-interval': 300, 'loopback-mode': True, 'name': 'Loopback100', 'openconfig-vlan:tpid': 'openconfig-vlan-types:TPID_0X8100', 'type': 'iana-if-type:softwareLoopback'}, 'openconfig-interfaces:hold-time': {'config': {'down': 0, 'up': 0}, 'state': {'down': 0, 'up': 0}}, 'openconfig-interfaces:name': 'Loopback100', 'openconfig-interfaces:state': {'enabled': True, 'loopback-mode': False, 'openconfig-vlan:tpid': 'openconfig-vlan-types:TPID_0X8100'}, 'openconfig-interfaces:subinterfaces': {'subinterface': [{'config': {'description': '222', 'enabled': True, 'index': 0}, 'index': 0, 'openconfig-if-ip:ipv4': {'config': {'dhcp-client': False, 'enabled': True, 'mtu': 1500}, 'state': {'dhcp-client': False, 'enabled': True, 'mtu': 1500}}, 'openconfig-if-ip:ipv6': {'config': {'dhcp-client': False, 'enabled': False, 'mtu': 1500}, 'state': {'dhcp-client': False, 'enabled': False, 'mtu': 1500}}, 'state': {'enabled': True, 'index': 0}}]}}
deleting int lo100
status_code is 200
```
