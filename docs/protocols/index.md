---
layout: default
title: "Management Protocols"
date: 2021-03-02 12:17:00 --0600
categories:
---

## Overview

## ssh (CLI)

## eAPI

## gRPC

gRPC is a Remote Procedure Call (RPC) framework that OpenConfig utilizes as a
transport. Services built with gRPC are defined in `.proto` files. They describe
the RPCs supported by the service and the data types exchanged in those RPCs.

The OpenConfig group originally published
[openconfig.proto](https://github.com/openconfig/reference/blob/master/rpc/openconfig/openconfig.proto),
but have since deprecated it in favor of
[gnmi.proto](https://github.com/openconfig/reference/blob/master/rpc/gnmi). The
current EOS versions supports gnmi.proto v0.7 and includes support for Get,
Subscribe, Set, and Capabilities RPCs.

Note: Support for openconfig.proto was dropped in EOS-4.23.0F+.

A client application is required to communicate with a gRPC service. A sample
application can be found on the Arista GitHub account:
[gnmi](https://github.com/aristanetworks/goarista/tree/master/cmd/gnmi). `gnmi`
is a simple command-line client for gNMI written in Go that can be used for
testing and prototyping.

Another popular gnmi client is [gnmic](https://gnmic.kmrd.dev/).

## NETCONF

[NETCONF](https://tools.ietf.org/html/rfc6241) provides mechanisms to install,
manipulate and delete the configuration of network devices. It uses eXtensible
Markup Language (XML) based data encoding for the configuration data as well as
protocol messages. The NETCONF protocol operations are realized as RPCs over ssh
transport.

## RESTCONF

## References / Resources

- NETCONF RFC: [https://tools.ietf.org/html/rfc6241](https://tools.ietf.org/html/rfc6241)
- RESTCONF RFC: [https://tools.ietf.org/html/rfc8040](https://tools.ietf.org/html/rfc8040)
