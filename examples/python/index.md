---
layout: page
title: "python"
date: 2021-03-19 08:17:00 --0600
categories:
---

## Overview

The following example uses the [pygnmi](https://pypi.org/project/pygnmi/) python module to talk to gNMI
devices.

```shell
python3 pygnmi.py
```

The following will simply run the pygnmi.py file using python3 to get the
openconfig interfaces.

## Truncated output

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
