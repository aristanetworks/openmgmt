---
layout: default
title: "gNOI"
date: 2021-07-16 12:17:00 --0600
categories:
---

## About gRPC

gRPC - Google Remote Procedure Call

gRPC uses protobuf and HTTP/2

## About gNOI

gNOI - gRPC Network Operations Interface

gNOI defines a set of gRPC-based microservices for executing operational commands on network devices.

gNOI [github repository](https://github.com/openconfig/gnoi)

As example, [this gNOI proto file](https://github.com/openconfig/gnoi/blob/master/system/system.proto) defines the
service `System` with the RPC `Traceroute` and `Ping`

- Ping executes the ping command on the target and streams back the results
- Traceroute executes the traceroute command on the target and streams back the results
- As you can see in the proto file, the field VRF is not defined for these messages

## About gNOI support on EOS

Please refer to this [link](https://eos.arista.com/eos-4-24-2f/gnoi/) for the gNOI support by EOS.

Examples:

- [gNOI ping](https://eos.arista.com/eos-4-22-1f/gnoi-ping/)
- [gNOI traceroute](https://eos.arista.com/eos-4-22-1f/gnoi-traceroute/)
- [gNOI Support](https://www.arista.com/en/support/toi/eos-4-24-2f/14715-gnoi)
