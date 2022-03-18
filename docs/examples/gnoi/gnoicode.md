---
layout: default
title: "gNOI in Golang"
date: 2022-01-06 10:07:00 --0600
categories:
---
## gNOI review

These are a few examples leveraging golang and gNOI using the gNOI protobuf specifically the [System
service](https://github.com/openconfig/gnoi/blob/master/system/system.proto)

The following examples show how to leverage the [ping
rpc](https://github.com/openconfig/gnoi/blob/master/system/system.proto#L41) and [traceroute
rpc](https://github.com/openconfig/gnoi/blob/master/system/system.proto#L47)

All code can be found within the [src directory under
gnoi](https://github.com/aristanetworks/openmgmt/tree/main/src/gnoi)

We will be leveraging the gNOI [godocs]((https://pkg.go.dev/github.com/openconfig/gnoi)) which module can be imported as
github.com/openconfig/gnoi

Each one of the examples has the following default flags which can be changed based on the environment.

```text
-username    = "admin"
-password    = "admin"
-target      = "172.20.20.2:6030"
-destination = "1.1.1.1"
```

## Test Device configuration

```text
management api gnmi
   transport grpc default
   provider eos-native
```

### cd into src/gnoi

```text
cd src/gnoi
```

The directory should include the go.mod/go.sum for the correct packages so nothing needs installed on the system at the
current time.

```text
ls
go.mod  go.sum  pinggnoi.go  traceroutegnoi.go
```

### Run ping.go

#### src/gnoi/ping.go

<details><summary>Reveal output</summary>
<p>

```golang
--8<-- "src/gnoi/ping/ping.go"
```

</p>
</details>

Output

```text
go run ping/ping.go -username admin -password admin -target 172.20.20.2:6030 -destination 2.2.2.2
source:"2.2.2.2" time:38000 bytes:64 sequence:1 ttl:64 <nil>
source:"2.2.2.2" time:44000 bytes:64 sequence:1 ttl:64 <nil>
source:"2.2.2.2" time:37000 bytes:64 sequence:1 ttl:64 <nil>
source:"2.2.2.2" time:41000 bytes:64 sequence:1 ttl:64 <nil>
source:"2.2.2.2" time:40000 bytes:64 sequence:1 ttl:64 <nil>
source:"2.2.2.2" time:38000 bytes:64 sequence:1 ttl:64 <nil>
source:"2.2.2.2" time:40000 bytes:64 sequence:1 ttl:64 <nil>
source:"2.2.2.2" time:36000 bytes:64 sequence:1 ttl:64 <nil>
source:"2.2.2.2" time:44000 bytes:64 sequence:1 ttl:64 <nil>
source:"2.2.2.2" time:66000 bytes:64 sequence:1 ttl:64 <nil>
```

### Run traceroute.go

#### src/gnoi/traceroute.go

<details><summary>Reveal output</summary>
<p>

```golang
--8<-- "src/gnoi/traceroute/traceroute.go"
```

</p>
</details>
<br>

Output

```text
go run traceroute/traceroute.go -username admin -password admin -target 172.20.20.2:6030 -destination 2.2.2.2
destination_name:"2.2.2.2"  destination_address:"2.2.2.2"  hops:30  packet_size:60 <nil>
```
