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
