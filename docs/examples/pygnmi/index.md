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
python3 pygnmi.py
```

The following will simply run the pygnmi.py file using python3 to get the openconfig interfaces.

### Truncated output

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

```shell
python3 capabilities.py
```

## gNMI Get RPC

```shell
python3 get.py
```

## gNMI Subscribe RPC

```shell
python3 sub.py
```

## gNMI Set RPC

### Update

```shell
python3 update.py
```

### Delete

```shell
python3 delete.py
```