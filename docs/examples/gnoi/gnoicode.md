---
layout: default
title: "gNOI in Golang"
date: 2022-01-06 10:07:00 --0600
categories:
---
## gNOI review

These are a few examples leveraging golang and gNOI using the gNOI protobuf specifically the [System service](https://github.com/openconfig/gnoi/blob/master/system/system.proto)

The following examples show how to leverage the [ping rpc](https://github.com/openconfig/gnoi/blob/master/system/system.proto#L41) and [traceroute rpc](https://github.com/openconfig/gnoi/blob/master/system/system.proto#L47)

All code can be found within the [src directory under gnoi](https://github.com/aristanetworks/openmgmt/tree/main/src/gnoi)

We will be leveraging the gNOI [godocs]((https://pkg.go.dev/github.com/openconfig/gnoi)) which module can be imported as github.com/openconfig/gnoi

Each one of the examples has the following constants which can be changed based on the environment.

```golang
const (
	username    = "admin"
	password    = "admin"
	target      = "172.20.20.2:6030"
	destination = "1.1.1.1"
	timeOut     = 5
)
```

## Test Device configuration
<br>

```shell
management api gnmi
   transport grpc default
   provider eos-native
```

### cd into src/gnoi
<br>

```shell
cd src/gnoi
```
<br>

The directory should include the go.mod/go.sum for the correct packages so nothing needs installed on the system at the current time.
<br>
<br>

```shell
ls
go.mod  go.sum  pinggnoi.go  traceroutegnoi.go
```

### Run ping.go

#### src/gnoi/ping.go

<details><summary>Reveal output</summary>
<p>

```golang
package main

import (
	"context"
	"fmt"
	"time"

	log "github.com/golang/glog"
	system "github.com/openconfig/gnoi/system"
	"google.golang.org/grpc"
	"google.golang.org/grpc/metadata"
)

const (
	username    = "admin"
	password    = "admin"
	target      = "172.20.20.2:6030"
	destination = "1.1.1.1"
	timeOut     = 5
)

func main() {
	conn, err := grpc.Dial(target, grpc.WithInsecure())
	if err != nil {
		log.Exitf("Failed to %s Error: %v", target, err)
	}
	defer conn.Close()

	// Create the new grpc service connection
	Sys := system.NewSystemClient(conn)
	// pass in context blank information with the timeout.
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	// cancel when the function is over.
	defer cancel()
	// Since Metadata needs a map to pass into the header of gRPC request create a map for it.
	metamap := make(map[string]string)
	// Set the username and password
	metamap["username"] = username
	metamap["password"] = password
	// Set the metadata needed in the metadata package
	md := metadata.New(metamap)
	// set the ctx to use the metadata in every update.
	ctx = metadata.NewOutgoingContext(ctx, md)

	for i := 0; i < 10; i++ {
		response, err := Sys.Ping(ctx, &system.PingRequest{Destination: destination})
		if err != nil {
			log.Fatalf("Error trying to ping: %v", err)
		}
		fmt.Println(response.Recv())
	}
}
```
</p>
</details>

Output
```shell
go run ping.go
source:"1.1.1.1"  time:16000  bytes:64  sequence:1  ttl:64 <nil>
source:"1.1.1.1"  time:18000  bytes:64  sequence:1  ttl:64 <nil>
source:"1.1.1.1"  time:18000  bytes:64  sequence:1  ttl:64 <nil>
source:"1.1.1.1"  time:22000  bytes:64  sequence:1  ttl:64 <nil>
source:"1.1.1.1"  time:22000  bytes:64  sequence:1  ttl:64 <nil>
source:"1.1.1.1"  time:20000  bytes:64  sequence:1  ttl:64 <nil>
source:"1.1.1.1"  time:22000  bytes:64  sequence:1  ttl:64 <nil>
source:"1.1.1.1"  time:19000  bytes:64  sequence:1  ttl:64 <nil>
source:"1.1.1.1"  time:22000  bytes:64  sequence:1  ttl:64 <nil>
source:"1.1.1.1"  time:22000  bytes:64  sequence:1  ttl:64 <nil>
```

### Run traceroute.go


#### src/gnoi/traceroute.go
<details><summary>Reveal output</summary>
<p>
<br>


```golang
package main

import (
	"context"
	"fmt"
	"time"

	log "github.com/golang/glog"
	system "github.com/openconfig/gnoi/system"
	"google.golang.org/grpc"
	"google.golang.org/grpc/metadata"
)

const (
	username    = "admin"
	password    = "admin"
	target      = "172.20.20.2:6030"
	destination = "2.2.2.2"
	timeOut     = 5
)

func main() {
	conn, err := grpc.Dial(target, grpc.WithInsecure())
	if err != nil {
		log.Exitf("Failed to %s Error: %v", target, err)
	}
	defer conn.Close()

	// Create the new grpc service connection
	Sys := system.NewSystemClient(conn)
	// pass in context blank information with the timeout.
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	// cancel when the function is over.
	defer cancel()
	// Since Metadata needs a map to pass into the header of gRPC request create a map for it.
	metamap := make(map[string]string)
	// Set the username and password
	metamap["username"] = username
	metamap["password"] = password
	// Set the metadata needed in the metadata package
	md := metadata.New(metamap)
	// set the ctx to use the metadata in every update.
	ctx = metadata.NewOutgoingContext(ctx, md)

	response, err := Sys.Traceroute(ctx, &system.TracerouteRequest{Destination: destination})
	if err != nil {
		log.Fatalf("Cannot trace path: %v", err)
	}
	fmt.Println(response.Recv())
}
```
</p>
</details>
<br>

Output
```shell
go run traceroute.go
destination_name:"2.2.2.2"  destination_address:"2.2.2.2"  hops:30  packet_size:60 <nil>
```