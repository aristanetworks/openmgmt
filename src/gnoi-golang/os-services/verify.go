package main

import (
	"context"
	"fmt"
	"time"

	log "github.com/golang/glog"
	Op "github.com/openconfig/gnoi/os"
	"google.golang.org/grpc"
	"google.golang.org/grpc/metadata"
)

const (
	username    = "admin"
	password    = "admin"
	target      = "192.168.4.242:4002"
	timeOut     = 5
)

func main() {
	conn, err := grpc.Dial(target, grpc.WithInsecure())
	if err != nil {
		log.Exitf("Failed to %s Error: %v", target, err)
	}
	defer conn.Close()

	// Create the new grpc service connection
	Ops := Op.NewOSClient(conn)
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

	response, err := Ops.Verify(ctx, &Op.VerifyRequest{})
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(response)
}
