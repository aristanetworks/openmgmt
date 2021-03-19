---
layout: page
title: "gNMI-Gateway"
date: 2021-03-019 08:17:00 --0600
categories:
---

- [Overview](#overview)
- [EOS configuration](#EOS-configuration)
- [Start gNMI gateway](#Start-gNMI-gateway.)
- [Query gNMI gateway](#Requesting-a-target-managed-by-gNMI-gateway.)


# Overview

[gNMI gateway](https://netflixtechblog.com/simple-streaming-telemetry-27447416e68f) is a opensource project created by netflix.  The idea of gNMI gateway is the gateway sits as a gateway or a proxy for multiple gNMI targets which it then manages.  A gNMI client will then speak to the gNMI service(gNMI gateway) and use a gNMI target which the client will then request the path.

gNMI gateway documentation can be found [here](https://github.com/openconfig/gnmi-gateway)

Nanog demo can also be found [here](https://www.youtube.com/watch?v=7QXpqqGTRn8)

In this demo we will start the gNMI gateway binary and use gNMIC to then stream to a target which is managed by gNMI gateway.  Please make adjustments to the targets.json file to match your own network.

```text
The demo is structured in a few different files all which have their own function.

├── gnmi-gateway
├── index.md
├── server.crt
├── server.key
└── targets.json

gnmi-gateway - this is the binary to activate gNMI gateway

server.crt / server.key - the cert for gNMI gateway

targets.json - This is the file where you specify the targets gNMI-gateway supports hot reloading of the files.  So if changes are made within targets.json it will reload automatically with new targets and or new paths.

```

# EOS configuration 

```text
management api gnmi
   transport grpc default
      ssl profile SELFSIGNED
   provider eos-native
!
management security
   ssl profile SELFSIGNED
      certificate cvp.crt key cvp.key
!
security pki certificate generate self-signed cvp.crt key cvp.key generate rsa 2048 validity 30000 parameters common-name cvp
```

The config stated here will add a self signed sert to the device and start the gNMI service with the cert.  

# Start gNMI gateway.

```text

./gnmi-gateway -EnableGNMIServer -ServerTLSCert=server.crt -ServerTLSKey=server.key -TargetLoaders=json -TargetJSONFile=targets.json

sh-3.2# ./gnmi-gateway -EnableGNMIServer -ServerTLSCert=server.crt -ServerTLSKey=server.key -TargetLoaders=json -TargetJSONFile=targets.json
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Starting GNMI Gateway."}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Clustering is NOT enabled. No locking or cluster coordination will happen."}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Starting connection manager."}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Starting gNMI server on 0.0.0.0:9339."}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Connection manager received a target control message: 3 inserts 0 removes"}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Initializing target DC2-SP02 ([10.20.30.22:6030]) map[NoTLS:yes]."}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Initializing target DC2-LEAF1A ([10.20.30.5:6030]) map[NoTLS:yes]."}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Target DC2-SP02: Connecting"}
{"level":"warn","time":"2021-03-19T08:47:35-04:00","message":"DEPRECATED: The 'NoTLS' target flag has been deprecated and will be removed in a future release. Please use 'NoTLSVerify' instead."}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Target DC2-SP02: Subscribing"}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Initializing target DC2-LF70 ([10.20.30.70:6030]) map[NoTLS:yes]."}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Target DC2-LEAF1A: Connecting"}
{"level":"warn","time":"2021-03-19T08:47:35-04:00","message":"DEPRECATED: The 'NoTLS' target flag has been deprecated and will be removed in a future release. Please use 'NoTLSVerify' instead."}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Target DC2-LEAF1A: Subscribing"}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Target DC2-LF70: Connecting"}
{"level":"warn","time":"2021-03-19T08:47:35-04:00","message":"DEPRECATED: The 'NoTLS' target flag has been deprecated and will be removed in a future release. Please use 'NoTLSVerify' instead."}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Target DC2-LF70: Subscribing"}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Target DC2-SP02: Connected"}
{"level":"info","time":"2021-03-19T08:47:36-04:00","message":"Target DC2-LF70: Connected"}
{"level":"info","time":"2021-03-19T08:47:36-04:00","message":"Target DC2-LEAF1A: Connected"}
{"level":"info","time":"2021-03-19T08:47:37-04:00","message":"Target DC2-LF70: Synced"}
{"level":"info","time":"2021-03-19T08:47:37-04:00","message":"Target DC2-SP02: Synced"}
{"level":"info","time":"2021-03-19T08:47:38-04:00","message":"Target DC2-LEAF1A: Synced"}

```

The given stdoutput tells us that gNMI-gateway has started and began to serve up gNMI requests to the /interfaces/interface path via any gNMI external client.

# Requesting a target managed by gNMI gateway. 

```text

gnmic subscribe -a 127.0.0.1 -u ansible -p ansible --port=9339 --skip-verify --target=DC2-SP02 --path=/interfaces

{
  "source": "127.0.0.1:9339",
  "subscription-name": "default-1616158143",
  "timestamp": 1605208845740882713,
  "time": "2020-11-12T14:20:45.740882713-05:00",
  "target": "DC2-SP02",
  "updates": [
    {
      "Path": "interfaces/interface[name=Ethernet54/1]/state/tpid",
      "values": {
        "interfaces/interface/state/tpid": "openconfig-vlan-types:TPID_0X8100"
      }
    }
  ]
}

```

Since gNMI gateway is running local on my macbook we can then query the service on port 9339 passing in the target value of DC2-SP02 and start to stream data  back to the client. 
