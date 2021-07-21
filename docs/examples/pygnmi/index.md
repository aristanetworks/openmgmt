---
layout: default
title: "pygnmi"
date: 2021-07-16 08:17:00 --0600
categories:
---

## Overview

The following example uses the [pygnmi](https://pypi.org/project/pygnmi/) python module to talk to gNMI
devices.

```python
# Modules
from pygnmi.client import gNMIclient
import json

# Variables
host = ('10.20.30.67', '6030')

# Body
if __name__ == '__main__':
    with gNMIclient(target=host, username='ansible', password='ansible', insecure=True) as gc:
         result = gc.get(path=['openconfig:interfaces'])
    print(json.dumps(result, indent=4))
```

Assuming that the `pygnmi` module has been installed, this can be executed via the following command.

```shell
python3 gnmi_example.py
```

The following will simply run the [`gnmi_example.py`](https://github.com/aristanetworks/openmgmt/blob/main/src/pygnmi/gnmi_example.py) file using python3 to get the openconfig interfaces.

Truncated output

```javascript
{
    "notification": [
        {
            "timestamp": 0,
            "update": [
                {
                    "path": "interfaces",
                    "json_ietf_val": {
                        "openconfig-interfaces:interface": [
                            {
                                "config": {
                                    "enabled": true,
                                    "arista-intf-augments:load-interval": 300,
                                    "loopback-mode": false,
                                    "mtu": 0,
                                    "name": "Ethernet1",
                                    "openconfig-vlan:tpid": "openconfig-vlan-types:TPID_0X8100",
                                    "type": "iana-if-type:ethernetCsmacd"
                                },

```

## gNMI Capabilities RPC

The file [capabilities.py](https://github.com/aristanetworks/openmgmt/blob/main/src/pygnmi/capabilities.py) uses the [pygnmi](https://pypi.org/project/pygnmi/) python module to get the gNMI capabilities.

```shell
python3 capabilities.py
```

<details><summary>Reveal output</summary>
<p>

```shell
{'gnmi_version': '0.7.0',
 'supported_encodings': ['json', 'json_ietf', 'ascii'],
 'supported_models': [{'name': 'arista-exp-eos-varp-net-inst',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'openconfig-acl',
                       'organization': 'OpenConfig working group',
                       'version': '1.1.1'},
                      {'name': 'arista-system-notsupported-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'openconfig-system-management',
                       'organization': 'OpenConfig working group',
                       'version': '0.2.0'},
                      {'name': 'arista-isis-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'openconfig-rib-bgp-types',
                       'organization': 'OpenConfig working group',
                       'version': '0.5.0'},
                      {'name': 'openconfig-platform-types',
                       'organization': 'OpenConfig working group',
                       'version': '1.0.0'},
                      {'name': 'openconfig-network-instance',
                       'organization': 'OpenConfig working group',
                       'version': '0.13.2'},
                      {'name': 'arista-bgp-augments',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-exp-eos-igmpsnooping',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'ietf-netconf',
                       'organization': 'IETF NETCONF (Network Configuration) '
                                       'Working Group',
                       'version': ''},
                      {'name': 'openconfig-policy-types',
                       'organization': 'OpenConfig working group',
                       'version': '3.1.1'},
                      {'name': 'openconfig-rib-bgp',
                       'organization': 'OpenConfig working group',
                       'version': '0.6.0'},
                      {'name': 'arista-local-routing-notsupported-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-exp-eos-varp-intf',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'arista-interfaces-notsupported-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-rpc-netconf',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'openconfig-platform-psu',
                       'organization': 'OpenConfig working group',
                       'version': '0.2.1'},
                      {'name': 'openconfig-packet-match-types',
                       'organization': 'OpenConfig working group',
                       'version': '1.0.2'},
                      {'name': 'openconfig-platform-fan',
                       'organization': 'OpenConfig working group',
                       'version': '0.1.1'},
                      {'name': 'openconfig-inet-types',
                       'organization': 'OpenConfig working group',
                       'version': '0.3.3'},
                      {'name': 'openconfig-igmp',
                       'organization': 'OpenConfig working group',
                       'version': '0.2.0'},
                      {'name': 'openconfig-aaa-types',
                       'organization': 'OpenConfig working group',
                       'version': '0.4.1'},
                      {'name': 'openconfig-lldp',
                       'organization': 'OpenConfig working group',
                       'version': '0.2.1'},
                      {'name': 'arista-relay-agent-deviations',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'arista-intf-augments',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'arista-qos-augments',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'ietf-yang-types',
                       'organization': 'IETF NETMOD (NETCONF Data Modeling '
                                       'Language) Working Group',
                       'version': ''},
                      {'name': 'openconfig-openflow',
                       'organization': 'OpenConfig working group',
                       'version': '0.1.2'},
                      {'name': 'iana-if-type',
                       'organization': 'IANA',
                       'version': ''},
                      {'name': 'arista-exp-eos-vxlan-config',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'arista-routing-policy-notsupported-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'openconfig-aaa',
                       'organization': 'OpenConfig working group',
                       'version': '0.4.3'},
                      {'name': 'openconfig-if-ip',
                       'organization': 'OpenConfig working group',
                       'version': '3.0.0'},
                      {'name': 'arista-srte-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-local-routing-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-lacp-augments',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'arista-bgp-notsupported-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-exp-eos-multicast',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'openconfig-interfaces',
                       'organization': 'OpenConfig working group',
                       'version': '2.4.3'},
                      {'name': 'openconfig-extensions',
                       'organization': 'OpenConfig working group',
                       'version': ''},
                      {'name': 'openconfig-system-terminal',
                       'organization': 'OpenConfig working group',
                       'version': '0.3.1'},
                      {'name': 'openconfig-bgp-types',
                       'organization': 'OpenConfig working group',
                       'version': '5.0.2'},
                      {'name': 'arista-netinst-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-system-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'openconfig-segment-routing',
                       'organization': 'OpenConfig working group',
                       'version': '0.0.4'},
                      {'name': 'openconfig-platform',
                       'organization': 'OpenConfig working group',
                       'version': '0.12.2'},
                      {'name': 'openconfig-pf-srte',
                       'organization': 'OpenConfig working group',
                       'version': '0.1.1'},
                      {'name': 'arista-vlan-deviations',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'openconfig-bfd',
                       'organization': 'OpenConfig working group',
                       'version': '0.2.0'},
                      {'name': 'openconfig-if-tunnel',
                       'organization': 'OpenConfig working group',
                       'version': '0.1.1'},
                      {'name': 'openconfig-alarms',
                       'organization': 'OpenConfig working group',
                       'version': '0.3.2'},
                      {'name': 'openconfig-if-aggregate',
                       'organization': 'OpenConfig working group',
                       'version': '2.4.2'},
                      {'name': 'arista-acl-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-acl-notsupported-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-messages-notsupported-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'openconfig-network-instance-types',
                       'organization': 'OpenConfig working group',
                       'version': '0.8.2'},
                      {'name': 'openconfig-types',
                       'organization': 'OpenConfig working group',
                       'version': '0.6.0'},
                      {'name': 'ietf-interfaces',
                       'organization': 'IETF NETMOD (Network Modeling) Working '
                                       'Group',
                       'version': ''},
                      {'name': 'openconfig-procmon',
                       'organization': 'OpenConfig working group',
                       'version': '0.4.0'},
                      {'name': 'arista-exp-eos-qos',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'arista-exp-eos',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'arista-qos-notsupported-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'openconfig-aft',
                       'organization': 'OpenConfig working group',
                       'version': '0.4.0'},
                      {'name': 'arista-isis-augments',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'openconfig-packet-match',
                       'organization': 'OpenConfig working group',
                       'version': '1.1.1'},
                      {'name': 'arista-lldp-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'openconfig-if-ethernet',
                       'organization': 'OpenConfig working group',
                       'version': '2.7.2'},
                      {'name': 'openconfig-mpls-sr',
                       'organization': 'OpenConfig working group',
                       'version': '3.0.1'},
                      {'name': 'openconfig-policy-forwarding',
                       'organization': 'OpenConfig working group',
                       'version': '0.2.1'},
                      {'name': 'arista-intf-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'openconfig-isis-lsdb-types',
                       'organization': 'OpenConfig working group',
                       'version': '0.4.2'},
                      {'name': 'vlan-translation',
                       'organization': 'Arista Networks',
                       'version': ''},
                      {'name': 'arista-gnoi-cert',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-network-instance-notsupported-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-bfd-augments',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'arista-vlan-augments',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'openconfig-hercules-interfaces',
                       'organization': 'OpenConfig Hercules Working Group',
                       'version': '0.2.0'},
                      {'name': 'arista-lacp-notsupported-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-srte-augments',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'openconfig-igmp-types',
                       'organization': 'OpenConfig working group',
                       'version': '0.1.1'},
                      {'name': 'openconfig-lacp',
                       'organization': 'OpenConfig working group',
                       'version': '1.1.1'},
                      {'name': 'openconfig-routing-policy',
                       'organization': 'OpenConfig working group',
                       'version': '3.1.1'},
                      {'name': 'arista-lacp-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'openconfig-system-logging',
                       'organization': 'OpenConfig working group',
                       'version': '0.3.1'},
                      {'name': 'openconfig-aft-types',
                       'organization': 'OpenConfig Working Group',
                       'version': '0.3.3'},
                      {'name': 'openconfig-network-instance-l3',
                       'organization': 'OpenConfig working group',
                       'version': '0.11.1'},
                      {'name': 'arista-bgp-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-rpol-augments',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'arista-eos-types',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'openconfig-qos-types',
                       'organization': 'OpenConfig working group',
                       'version': '0.2.1'},
                      {'name': 'arista-openflow-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'openconfig-mpls-types',
                       'organization': 'OpenConfig working group',
                       'version': '3.1.0'},
                      {'name': 'openconfig-hercules-qos',
                       'organization': 'OpenConfig Hercules Working Group',
                       'version': '0.1.0'},
                      {'name': 'openconfig-bgp',
                       'organization': 'OpenConfig working group',
                       'version': '6.0.0'},
                      {'name': 'arista-platform-notsupported-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-system-augments',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-exp-eos-mlag',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'openconfig-system',
                       'organization': 'OpenConfig working group',
                       'version': '0.8.0'},
                      {'name': 'openconfig-isis',
                       'organization': 'OpenConfig working group',
                       'version': '0.4.2'},
                      {'name': 'openconfig-lldp-types',
                       'organization': 'OpenConfig working group',
                       'version': '0.1.1'},
                      {'name': 'openconfig-vlan',
                       'organization': 'OpenConfig working group',
                       'version': '3.2.0'},
                      {'name': 'openconfig-if-types',
                       'organization': 'OpenConfig working group',
                       'version': '0.2.1'},
                      {'name': 'openconfig-relay-agent',
                       'organization': 'OpenConfig working group',
                       'version': '0.1.1'},
                      {'name': 'arista-lldp-notsupported-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-aft-augments',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'openconfig-vlan-types',
                       'organization': 'OpenConfig working group',
                       'version': '3.1.0'},
                      {'name': 'arista-mpls-augments',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'arista-mpls-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'openconfig-alarm-types',
                       'organization': 'OpenConfig working group',
                       'version': '0.2.1'},
                      {'name': 'openconfig-hercules-platform',
                       'organization': 'OpenConfig Hercules Working Group',
                       'version': '0.2.0'},
                      {'name': 'openconfig-ospfv2',
                       'organization': 'OpenConfig working group',
                       'version': '0.2.2'},
                      {'name': 'ietf-netconf-monitoring',
                       'organization': 'IETF NETCONF (Network Configuration) '
                                       'Working Group',
                       'version': ''},
                      {'name': 'arista-exp-eos-evpn',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-exp-eos-vxlan',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'openconfig-platform-port',
                       'organization': 'OpenConfig working group',
                       'version': '0.3.2'},
                      {'name': 'openconfig-messages',
                       'organization': 'OpenConfig working group',
                       'version': '0.0.1'},
                      {'name': 'openconfig-platform-cpu',
                       'organization': 'OpenConfig working group',
                       'version': '0.1.1'},
                      {'name': 'openconfig-if-poe',
                       'organization': 'OpenConfig working group',
                       'version': '0.1.1'},
                      {'name': 'openconfig-pim',
                       'organization': 'OpenConfig working group',
                       'version': '0.2.0'},
                      {'name': 'openconfig-openflow-types',
                       'organization': 'OpenConfig working group',
                       'version': '0.1.2'},
                      {'name': 'openconfig-mpls',
                       'organization': 'OpenConfig working group',
                       'version': '3.1.0'},
                      {'name': 'openconfig-platform-linecard',
                       'organization': 'OpenConfig working group',
                       'version': '0.1.1'},
                      {'name': 'openconfig-mpls-ldp',
                       'organization': 'OpenConfig working group',
                       'version': '3.0.2'},
                      {'name': 'openconfig-bgp-policy',
                       'organization': 'OpenConfig working group',
                       'version': '6.0.1'},
                      {'name': 'openconfig-mpls-rsvp',
                       'organization': 'OpenConfig working group',
                       'version': '3.0.1'},
                      {'name': 'arista-exp-eos-qos-config',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'openconfig-yang-types',
                       'organization': 'OpenConfig working group',
                       'version': '0.2.1'},
                      {'name': 'openconfig-qos',
                       'organization': 'OpenConfig working group',
                       'version': '0.2.3'},
                      {'name': 'openconfig-local-routing',
                       'organization': 'OpenConfig working group',
                       'version': '1.0.2'},
                      {'name': 'ietf-inet-types',
                       'organization': 'IETF NETMOD (NETCONF Data Modeling '
                                       'Language) Working Group',
                       'version': ''},
                      {'name': 'arista-rpol-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-pim-augments',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'openconfig-pim-types',
                       'organization': 'OpenConfig working group',
                       'version': '0.1.1'},
                      {'name': 'arista-bfd-notsupported-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-lldp-augments',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''},
                      {'name': 'arista-exp-eos-qos-acl-config',
                       'organization': 'Arista Networks <http://arista.com/>',
                       'version': ''},
                      {'name': 'openconfig-isis-types',
                       'organization': 'OpenConfig working group',
                       'version': '0.4.2'},
                      {'name': 'openconfig-ospf-policy',
                       'organization': 'OpenConfig working group',
                       'version': '0.1.3'},
                      {'name': 'openconfig-ospf-types',
                       'organization': 'OpenConfig working group',
                       'version': '0.1.3'},
                      {'name': 'arista-bfd-deviations',
                       'organization': 'Arista Networks, Inc.',
                       'version': ''}]}
```

</p>
</details>

## gNMI Get RPC

The file [get.py](https://github.com/aristanetworks/openmgmt/blob/main/src/pygnmi/get.py) uses the [pygnmi](https://pypi.org/project/pygnmi/) python module and uses the gNMI GET RPC

```shell
python3 get.py
```

<details><summary>Reveal output</summary>
<p>

```shell
{
  "notification": [
    {
      "timestamp": 0,
      "update": [
        {
          "path": "interfaces/interface[name=Ethernet1]/state/counters",
          "val": {
            "openconfig-interfaces:in-broadcast-pkts": "2",
            "openconfig-interfaces:in-discards": "0",
            "openconfig-interfaces:in-errors": "0",
            "openconfig-interfaces:in-fcs-errors": "0",
            "openconfig-interfaces:in-multicast-pkts": "189439",
            "openconfig-interfaces:in-octets": "48284395",
            "openconfig-interfaces:in-unicast-pkts": "416884",
            "openconfig-interfaces:out-broadcast-pkts": "14",
            "openconfig-interfaces:out-discards": "0",
            "openconfig-interfaces:out-errors": "0",
            "openconfig-interfaces:out-multicast-pkts": "217232",
            "openconfig-interfaces:out-octets": "51749355",
            "openconfig-interfaces:out-unicast-pkts": "416911"
          }
        }
      ]
    },
    {
      "timestamp": 0,
      "update": [
        {
          "path": "network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state",
          "val": {
            "openconfig-network-instance:enabled": true,
            "openconfig-network-instance:established-transitions": "0",
            "openconfig-network-instance:last-established": "1625684802230601216",
            "openconfig-network-instance:messages": {
              "received": {
                "UPDATE": "0"
              },
              "sent": {
                "UPDATE": "0"
              }
            },
            "openconfig-network-instance:neighbor-address": "192.168.255.2",
            "openconfig-network-instance:peer-group": "EVPN-OVERLAY-PEERS",
            "openconfig-network-instance:send-community": "NONE",
            "openconfig-network-instance:session-state": "ACTIVE"
          }
        },
        {
          "path": "network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state",
          "val": {
            "openconfig-network-instance:enabled": true,
            "openconfig-network-instance:established-transitions": "2",
            "openconfig-network-instance:last-established": "1625740129181922304",
            "openconfig-network-instance:messages": {
              "received": {
                "UPDATE": "2"
              },
              "sent": {
                "UPDATE": "24"
              }
            },
            "openconfig-network-instance:neighbor-address": "192.168.255.1",
            "openconfig-network-instance:peer-group": "EVPN-OVERLAY-PEERS",
            "openconfig-network-instance:send-community": "NONE",
            "openconfig-network-instance:session-state": "ACTIVE"
          }
        }
      ]
    }
  ]
}
```

</p>
</details>

## gNMI Subscribe RPC

The file [sub.py](https://github.com/aristanetworks/openmgmt/blob/main/src/pygnmi/sub.py) uses the [pygnmi](https://pypi.org/project/pygnmi/) python module and uses the gNMI Subscribe RPC

```shell
python3 sub.py
```

<details><summary>Reveal output</summary>
<p>

```shell
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-broadcast-pkts', 'val': 2}], 'timestamp': 1626462768674581749}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-discards', 'val': 0}], 'timestamp': 1626462768674597259}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-errors', 'val': 0}], 'timestamp': 1626462768674603747}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-fcs-errors', 'val': 0}], 'timestamp': 1626462768672465216}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-multicast-pkts', 'val': 189439}], 'timestamp': 1626462768674588779}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-octets', 'val': 48284395}], 'timestamp': 1626462768674553338}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-unicast-pkts', 'val': 416884}], 'timestamp': 1626462768674571889}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-broadcast-pkts', 'val': 14}], 'timestamp': 1626462768674624983}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-discards', 'val': 0}], 'timestamp': 1626462768674639908}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-errors', 'val': 0}], 'timestamp': 1626462768674645915}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-multicast-pkts', 'val': 217294}], 'timestamp': 1626599894372892660}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-octets', 'val': 51756949}], 'timestamp': 1626599894372858163}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-unicast-pkts', 'val': 416911}], 'timestamp': 1626462768674617475}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/enabled', 'val': True}], 'timestamp': 1626462768440845697}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/established-transitions', 'val': 0}], 'timestamp': 1626462768468632490}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/last-established', 'val': 1625684802230601216}], 'timestamp': 1626462768469284793}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/messages/received/UPDATE', 'val': 0}], 'timestamp': 1626462768421128387}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/messages/sent/UPDATE', 'val': 0}], 'timestamp': 1626462768421184402}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/neighbor-address', 'val': '192.168.255.2'}], 'timestamp': 1626462768421876850}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/peer-group', 'val': 'EVPN-OVERLAY-PEERS'}], 'timestamp': 1626462768439035722}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/send-community', 'val': 'NONE'}], 'timestamp': 1626462768419003214}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/session-state', 'val': 'ACTIVE'}], 'timestamp': 1626462768469145043}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/enabled', 'val': True}], 'timestamp': 1626462768428252812}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/established-transitions', 'val': 2}], 'timestamp': 1626462768470394508}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/last-established', 'val': 1625740129181922304}], 'timestamp': 1626462768469974563}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/messages/received/UPDATE', 'val': 2}], 'timestamp': 1626462768424768147}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/messages/sent/UPDATE', 'val': 24}], 'timestamp': 1626462768424826346}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/neighbor-address', 'val': '192.168.255.1'}], 'timestamp': 1626462768425586744}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/peer-group', 'val': 'EVPN-OVERLAY-PEERS'}], 'timestamp': 1626462768427044044}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/send-community', 'val': 'NONE'}], 'timestamp': 1626462768423035498}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/session-state', 'val': 'ACTIVE'}], 'timestamp': 1626462768469536321}}
{'sync_response': True}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-broadcast-pkts', 'val': 2}], 'timestamp': 1626462768674581749}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-discards', 'val': 0}], 'timestamp': 1626462768674597259}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-errors', 'val': 0}], 'timestamp': 1626462768674603747}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-fcs-errors', 'val': 0}], 'timestamp': 1626462768672465216}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-multicast-pkts', 'val': 189439}], 'timestamp': 1626462768674588779}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-octets', 'val': 48284395}], 'timestamp': 1626462768674553338}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-unicast-pkts', 'val': 416884}], 'timestamp': 1626462768674571889}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-broadcast-pkts', 'val': 14}], 'timestamp': 1626462768674624983}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-discards', 'val': 0}], 'timestamp': 1626462768674639908}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-errors', 'val': 0}], 'timestamp': 1626462768674645915}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-multicast-pkts', 'val': 217299}], 'timestamp': 1626599904372340631}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-octets', 'val': 51757564}], 'timestamp': 1626599904372302101}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-unicast-pkts', 'val': 416911}], 'timestamp': 1626462768674617475}}
{'sync_response': True}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/enabled', 'val': True}], 'timestamp': 1626462768440845697}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/established-transitions', 'val': 0}], 'timestamp': 1626462768468632490}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/last-established', 'val': 1625684802230601216}], 'timestamp': 1626462768469284793}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/messages/received/UPDATE', 'val': 0}], 'timestamp': 1626462768421128387}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/messages/sent/UPDATE', 'val': 0}], 'timestamp': 1626462768421184402}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/neighbor-address', 'val': '192.168.255.2'}], 'timestamp': 1626462768421876850}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/peer-group', 'val': 'EVPN-OVERLAY-PEERS'}], 'timestamp': 1626462768439035722}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/send-community', 'val': 'NONE'}], 'timestamp': 1626462768419003214}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/session-state', 'val': 'ACTIVE'}], 'timestamp': 1626462768469145043}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/enabled', 'val': True}], 'timestamp': 1626462768428252812}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/established-transitions', 'val': 2}], 'timestamp': 1626462768470394508}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/last-established', 'val': 1625740129181922304}], 'timestamp': 1626462768469974563}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/messages/received/UPDATE', 'val': 2}], 'timestamp': 1626462768424768147}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/messages/sent/UPDATE', 'val': 24}], 'timestamp': 1626462768424826346}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/neighbor-address', 'val': '192.168.255.1'}], 'timestamp': 1626462768425586744}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/peer-group', 'val': 'EVPN-OVERLAY-PEERS'}], 'timestamp': 1626462768427044044}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/send-community', 'val': 'NONE'}], 'timestamp': 1626462768423035498}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/session-state', 'val': 'ACTIVE'}], 'timestamp': 1626462768469536321}}
{'sync_response': True}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-broadcast-pkts', 'val': 2}], 'timestamp': 1626462768674581749}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-discards', 'val': 0}], 'timestamp': 1626462768674597259}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-errors', 'val': 0}], 'timestamp': 1626462768674603747}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-fcs-errors', 'val': 0}], 'timestamp': 1626462768672465216}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-multicast-pkts', 'val': 189439}], 'timestamp': 1626462768674588779}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-octets', 'val': 48284395}], 'timestamp': 1626462768674553338}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-unicast-pkts', 'val': 416884}], 'timestamp': 1626462768674571889}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-broadcast-pkts', 'val': 14}], 'timestamp': 1626462768674624983}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-discards', 'val': 0}], 'timestamp': 1626462768674639908}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-errors', 'val': 0}], 'timestamp': 1626462768674645915}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-multicast-pkts', 'val': 217304}], 'timestamp': 1626599914374756337}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-octets', 'val': 51758179}], 'timestamp': 1626599914374727204}}
{'update': {'update': [{'path': 'interfaces/interface[name=Ethernet1]/state/counters/out-unicast-pkts', 'val': 416911}], 'timestamp': 1626462768674617475}}
{'sync_response': True}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/enabled', 'val': True}], 'timestamp': 1626462768440845697}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/established-transitions', 'val': 0}], 'timestamp': 1626462768468632490}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/last-established', 'val': 1625684802230601216}], 'timestamp': 1626462768469284793}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/messages/received/UPDATE', 'val': 0}], 'timestamp': 1626462768421128387}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/messages/sent/UPDATE', 'val': 0}], 'timestamp': 1626462768421184402}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/neighbor-address', 'val': '192.168.255.2'}], 'timestamp': 1626462768421876850}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/peer-group', 'val': 'EVPN-OVERLAY-PEERS'}], 'timestamp': 1626462768439035722}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/send-community', 'val': 'NONE'}], 'timestamp': 1626462768419003214}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.2]/state/session-state', 'val': 'ACTIVE'}], 'timestamp': 1626462768469145043}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/enabled', 'val': True}], 'timestamp': 1626462768428252812}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/established-transitions', 'val': 2}], 'timestamp': 1626462768470394508}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/last-established', 'val': 1625740129181922304}], 'timestamp': 1626462768469974563}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/messages/received/UPDATE', 'val': 2}], 'timestamp': 1626462768424768147}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/messages/sent/UPDATE', 'val': 24}], 'timestamp': 1626462768424826346}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/neighbor-address', 'val': '192.168.255.1'}], 'timestamp': 1626462768425586744}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/peer-group', 'val': 'EVPN-OVERLAY-PEERS'}], 'timestamp': 1626462768427044044}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/send-community', 'val': 'NONE'}], 'timestamp': 1626462768423035498}}
{'update': {'update': [{'path': 'network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=192.168.255.1]/state/session-state', 'val': 'ACTIVE'}], 'timestamp': 1626462768469536321}}
```

</p>
</details>

## gNMI Set RPC

### Update

The file [update.py](https://github.com/aristanetworks/openmgmt/blob/main/src/pygnmi/update.py) uses the [pygnmi](https://pypi.org/project/pygnmi/) python module and uses the gNMI SET RPC (update)

```shell
python3 update.py
```

output

```shell
GET RPC, interface Ethernet1 config, before the update
{
  "notification": [
    {
      "timestamp": 0,
      "update": [
        {
          "path": "interfaces/interface[name=Ethernet1]/config",
          "val": {
            "arista-intf-augments:load-interval": 300,
            "openconfig-interfaces:description": "test1234",
            "openconfig-interfaces:enabled": true,
            "openconfig-interfaces:loopback-mode": false,
            "openconfig-interfaces:mtu": 0,
            "openconfig-interfaces:name": "Ethernet1",
            "openconfig-interfaces:type": "iana-if-type:ethernetCsmacd",
            "openconfig-vlan:tpid": "openconfig-vlan-types:TPID_0X8100"
          }
        }
      ]
    }
  ]
}

SET RPC, update, interface Ethernet1
{'response': [{'path': 'interfaces/interface[name=Ethernet1]', 'op': 'UPDATE'}]}

GET RPC, interface Ethernet1 config, after the update
{
  "notification": [
    {
      "timestamp": 0,
      "update": [
        {
          "path": "interfaces/interface[name=Ethernet1]/config",
          "val": {
            "arista-intf-augments:load-interval": 300,
            "openconfig-interfaces:description": "Test",
            "openconfig-interfaces:enabled": true,
            "openconfig-interfaces:loopback-mode": false,
            "openconfig-interfaces:mtu": 0,
            "openconfig-interfaces:name": "Ethernet1",
            "openconfig-interfaces:type": "iana-if-type:ethernetCsmacd",
            "openconfig-vlan:tpid": "openconfig-vlan-types:TPID_0X8100"
          }
        }
      ]
    }
  ]
}
```

</p>
</details>

### Delete

The file [delete.py](https://github.com/aristanetworks/openmgmt/blob/main/src/pygnmi/delete.py) uses the [pygnmi](https://pypi.org/project/pygnmi/) python module and uses the gNMI SET RPC (delete)

```shell
python3 delete.py
```

output

```shell
{'response': [{'path': 'interfaces/interface[name=Ethernet1]/config/description', 'op': 'DELETE'}]}
```
