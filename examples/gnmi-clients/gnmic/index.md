---
layout: page
title: "gNMIC examples"
date: 2021-03-18 12:17:00 --0600
categories:
---

- [Overview](#overview)
- [Download && install gnmic](#Download-&&-install-gnmic)
- [Device config](#Device-config)
  - [Capabilities](#capabilities)
- [openconfig-paths]
  - [Get](#Get-openconfig-paths)
  - [Subscribe](#Subscribe-openconfig-paths)
- [Eos Native paths](#eos_native-paths)
- [Cli origin](#Cli-origin)
- [Misc](#Misc)
- [Smash paths](#Smash-Paths)

## overview

The following examples are used to find openconfig paths within Arista EOS using
the [gNMIC binary](https://gnmic.kmrd.dev/). There will be some commands which
will specify one liners which will have the address of the gNMI target and some
commands which will use the `.gnmic.yaml` file which will have the target
information inside declared. All outputs will be redirected to the outputs file
with the .json extension so they are easier to view within a text editor.

## Download && install gnmic

```shell
curl -sL https://github.com/karimra/gnmic/raw/master/install.sh | sudo bash

gnmi_stuff$ gnmic version
version : 0.7.0
 commit : dcbe8d3
   date : 2021-01-28T01:58:29Z
 gitURL : https://github.com/karimra/gnmic
   docs : https://gnmic.kmrd.dev
```

## Device config

```shell

management api gnmi
   transport grpc default
   provider eos-native

ceos3#                show management api gnmi
Octa:               enabled
Enabled:            Yes
Server:             running on port 6030
SSL Profile:        none
QoS DSCP:           none
Authorization Required:No
```

```shell
gnmic -a 127.0.0.1:6030 -u admin -p admin --insecure capabilities  \
  >> outputs/capabilities.json
```

## Get openconfig paths

```shell
gnmic -a 127.0.0.1:6030 -u admin -p admin --insecure get \
  --path /  >> outputs/everything.json

gnmic -a 127.0.0.1:6030 -u admin -p admin --insecure get --path \
  /network-instances/network-instance >> outputs/network-instances.json

gnmic -a 127.0.0.1:6030 -u admin -p admin --insecure get --path \
  /network-instances/network-instance[name=default]/protocols/protocol[name=BGP]\
  >> outputs/bgp.json
```

## Subscribe openconfig paths

```shell
gnmic -a 127.0.0.1:6030 -u admin -p admin --insecure subscribe --path \
  "/interfaces/interface/state/counters"  >> outputs/interface_state.json
```

## eos_native paths

```shell
gnmic -a 127.0.0.1:6030 -u admin -p admin --insecure get --path \
  eos_native:/Sysdb/hardware/archer/xcvr/status >> outputs/doms.json

gnmic -a 127.0.0.1:6030 -u admin -p admin --insecure get \
  --path eos_native:/Eos/image >> outputs/eos_image.json
```

## Cli origin

```shell

gnmic -a 127.0.0.1:6030 -u admin -p admin --insecure  get \
  --path "cli:/show running-config" >> outputs/outputs.json

gnmic -a 127.0.0.1:6030 -u admin -p admin --insecure  get \
  --path "cli:/show ip route summary" \
  | jq '.[0].updates[0].values."show ip route summary".totalRoutes'

```

## Misc

```shell
gnmic -a 127.0.0.1:6030 -u admin -p admin --insecure get \
  --path ".../state/..." >> outputs/states.json
gnmic -a 127.0.0.1:6030 -u admin -p admin --insecure get \
  --path ".../config/..." >> outputs/configs.json
```

## Smash paths

```shell
gnmic -a 127.0.0.1:6030 -u admin -p admin --insecure get \
  --path eos_native:/Smash >> outputs/smashes.json
```
