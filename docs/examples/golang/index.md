---
layout: default
title: "golang"
date: 2021-03-19 08:17:00 --0600
categories:
---

## Overview

The following example uses the [goarista](https://pkg.go.dev/github.com/aristanetworks/goarista) go module for gNMI to
interact with a device. Within this very simplistic getting started example main.go will simply perform a get method to
the device for all paths.

```golang
package main

import (
  "context"
  "fmt"

  "github.com/aristanetworks/glog"
  "github.com/aristanetworks/goarista/gnmi"
  pb "github.com/openconfig/gnmi/proto/gnmi"
)

var cfg = &gnmi.Config{
    Addr:     "10.20.30.67:6030",
    Username: "ansible",
    Password: "ansible",
}

func main() {
    paths := []string{"/"}
    var origin = "openconfig"
    //var origin = "eos_native"
    ctx := gnmi.NewContext(context.Background(), cfg)
    client, err := gnmi.Dial(cfg)
    if err != nil {
        glog.Fatal(err)
    }

    req, err := gnmi.NewGetRequest(gnmi.SplitPaths(paths), origin)
    if err != nil {
        glog.Fatal(err)
    }
    if cfg.Addr != "" {
        if req.Prefix == nil {
            req.Prefix = &pb.Path{}
        }
        req.Prefix.Target = cfg.Addr
    }

    err = gnmi.GetWithRequest(ctx, client, req)
    if err != nil {
        glog.Fatal(err)
    }
    fmt.Println(err)
}
```

Copy the above code into a file and run via the following command.

```shell
go run main.go
```

## Truncated output

```javascript
{
  "openconfig-acl:acl": {
    "state": {
      "counter-capability": "AGGREGATE_ONLY"
    }
  },
  "arista-exp-eos:arista": {
    "eos": {
      "arista-exp-eos-igmpsnooping:bridging": {
        "igmpsnooping": {
          "config": {}
        }
      },
      "arista-exp-eos-mlag:mlag": {
        "config": {
          "dual-primary-action": "action-none",
```

## Subscription Example
The following example reuses the libraries from the previous example, but instead performs a Subscribe. 
It subscribes to the interface counters for all interfaces on the system to allow for real-time statistics
to be collected. Wildcards are use to get updates for all interfaces.
```go
package main

import (
	"context"
	"fmt"
	"log"
	"path"
	"time"

	"github.com/aristanetworks/goarista/gnmi"
	pb "github.com/openconfig/gnmi/proto/gnmi"
)

var cfg = &gnmi.Config{
    Addr:     "10.20.30.67:6030",
    Username: "ansible",
    Password: "ansible",
}

func main() {
	paths := []string{"/interfaces/interface[name=*]/state/counters"}
	origin := "openconfig"
	ctx := gnmi.NewContext(context.Background(), cfg)
	client, err := gnmi.Dial(cfg)
	if err != nil {
		log.Fatal(err)
	}

	subOptions := gnmi.SubscribeOptions{
		Origin: origin,
		Paths:  gnmi.SplitPaths(paths),
		Target: cfg.Addr,
	}

	respChan := make(chan *pb.SubscribeResponse, 128)

	// Setup GNMI subscription, subscription is blocking so launch in goroutine
	go func() {
		err = gnmi.SubscribeErr(ctx, client, &subOptions, respChan)
		if err != nil {
			log.Fatal(err)
		}
	}()

	for {
		select {
		case response := <-respChan:
			switch resp := response.Response.(type) {
			// Other response types possible, we only want Updates
			case *pb.SubscribeResponse_Update:
				t := time.Unix(0, resp.Update.Timestamp).UTC()
				prefix := gnmi.StrPath(resp.Update.Prefix)
				var target string
				if t := resp.Update.Prefix.GetTarget(); t != "" {
					target = "(" + t + ") "
				}
				for _, update := range resp.Update.Update {
					fmt.Printf("[%s] %sUpdate %s = %s\n",
						t.Format(time.RFC3339Nano),
						target,
						path.Join(prefix, gnmi.StrPath(update.Path)),
						gnmi.StrUpdateVal(update),
					)
				}
			}
		}
	}
}
```

Copy the above code into a file and run via the following command.

```shell
go run main.go
```

## Truncated output

```javascript
[2023-01-10T19:48:06.515549849Z] (10.20.30.67:6030) Update /interfaces/interface[name=Ethernet53/1]/state/counters/in-pkts = 4343365249726
[2023-01-10T19:48:06.515549849Z] (10.20.30.67:6030) Update /interfaces/interface[name=Ethernet53/1]/state/counters/out-pkts = 22021980
[2023-01-10T19:48:06.515549849Z] (10.20.30.67:6030) Update /interfaces/interface[name=Ethernet49/1]/state/counters/in-octets = 2821732296
[2023-01-10T19:48:06.515549849Z] (10.20.30.67:6030) Update /interfaces/interface[name=Ethernet49/1]/state/counters/in-multicast-pkts = 29240239
[2023-01-10T19:48:06.515549849Z] (10.20.30.67:6030) Update /interfaces/interface[name=Ethernet49/1]/state/counters/out-octets = 5517763786786491
[2023-01-10T19:48:06.515549849Z] (10.20.30.67:6030) Update /interfaces/interface[name=Ethernet49/1]/state/counters/out-multicast-pkts = 3866904519547
[2023-01-10T19:48:06.515549849Z] (10.20.30.67:6030) Update /interfaces/interface[name=Ethernet49/1]/state/counters/in-pkts = 29335757
[2023-01-10T19:48:06.515549849Z] (10.20.30.67:6030) Update /interfaces/interface[name=Ethernet49/1]/state/counters/out-pkts = 3866904615059
```
