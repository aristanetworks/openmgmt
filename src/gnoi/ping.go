package main

import (
	"context"
	"flag"
	"fmt"
	"time"

	log "github.com/golang/glog"
	system "github.com/openconfig/gnoi/system"
	"google.golang.org/grpc"
	"google.golang.org/grpc/metadata"
)

func main() {
	// Add input parameters
	username := flag.String("username", "admin", "username for connection to gNOI")
	password := flag.String("password", "admin", "password for connection to gNOI")
	target := flag.String("target", "172.20.20.2:6030", "Target ip or hostname of the device running gNOI")
	destination := flag.String("destination", "2.2.2.2", "Destination of the address to ping to")
	flag.Parse()
	conn, err := grpc.Dial(*target, grpc.WithInsecure())
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
	metamap["username"] = *username
	metamap["password"] = *password
	// Set the metadata needed in the metadata package
	md := metadata.New(metamap)
	// set the ctx to use the metadata in every update.
	ctx = metadata.NewOutgoingContext(ctx, md)
	// Try to ping 10 times with a loop
	for i := 0; i < 10; i++ {
		response, err := Sys.Ping(ctx, &system.PingRequest{Destination: *destination})
		if err != nil {
			log.Fatalf("Error trying to ping: %v", err)
		}
		fmt.Println(response.Recv())
	}
}
