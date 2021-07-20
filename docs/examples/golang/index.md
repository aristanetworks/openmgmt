---
layout: default
title: "golang"
date: 2021-03-19 08:17:00 --0600
categories:
---

## Overview

The following example uses the [goarista](https://pkg.go.dev/github.com/aristanetworks/goarista) go module for gNMI to
interact with a device.  Within this very simplistic getting started example main.go will simply perform a get method to
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
