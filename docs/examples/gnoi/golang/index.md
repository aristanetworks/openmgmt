---
layout: default
title: "gNOI golang examples"
date: 2021-07-19 09:00:00 --0600
categories:
---

## About gRPC

gRPC - Google Remote Procedure Call

gRPC uses protobuf and HTTP/2

## About gNOI

gNOI - gRPC Network Operations Interface

gNOI defines a set of gRPC-based microservices for executing operational commands on network devices.

gNOI [github repository](https://github.com/openconfig/gnoi)

As example, we use the [system gNOI proto file](https://github.com/openconfig/gnoi/blob/master/system/system.proto).

- Ping executes the ping command on the target and streams back the results
- Traceroute executes the traceroute command on the target and streams back the results
- As you can see in the proto file, the field VRF is not defined for these messages


## About gNOI support on EOS

Please refer to this [link](https://eos.arista.com/eos-4-24-2f/gnoi/) for the gNOI support by EOS.

Examples:

- [gnoi ping](https://eos.arista.com/eos-4-22-1f/gnoi-ping/)
- [gnoi traceroute](https://eos.arista.com/eos-4-22-1f/gnoi-traceroute/)

## golang overview 

Current version of golang running on my system is as follows.

```shell
go version go1.16.5 linux/amd64
```

## change directory into golang gNOI examples.

```shell
cd src/gnoi-golang/
```

## File structure 

```
.
├── go.mod
├── go.sum
└── system-services
    ├── pinggnoi.go
    ├── traceroutegnoi.go
```

The [system-services](https://github.com/openconfig/gnoi/tree/master/system) contain the system-services protos services.

## Device config

```shell
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.1.118/24

username admin secret 0 admin

management api gnmi
   transport grpc def
```

```shell
ceos1#show management api gnmi
Enabled:            Yes
Server:             running on port 6030
SSL Profile:        none
QoS DSCP:           none
ceos1#
```

## Constants

Most files will have the following constants within the .go files ping for example.

```golang
const (
	username    = "admin"
	password    = "admin"
	target      = "127.0.0.1:4002"
	destination = "2.2.2.2"
	timeOut     = 5
)
```

These can be changed to your liking.  127.0.0.1:4002 is my current gNMI natted interface using ceos on docker. 

## gNOI demo with Arista using golang

Ping gNOI
```shell
go run pinggnoi.go 
```

Output:

```shell
source:"2.2.2.2"  time:49000  bytes:64  sequence:1  ttl:64 <nil>
```

Traceroute gNOI
```shell
 go run system-services/traceroutegnoi.go
```

Output:

```shell
destination_name:"1.1.1.1" destination_address:"1.1.1.1" hops:30 packet_size:60 <nil>
```
