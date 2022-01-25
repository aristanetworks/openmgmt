---
layout: default
title: "gNMI-Gateway"
date: 2021-03-19 08:17:00 --0600
categories:
---

## Overview

[gNMI gateway](https://netflixtechblog.com/simple-streaming-telemetry-27447416e68f) is an opensource project created by
Netflix. Conceptually, gNMI gateway sits as a proxy for multiple gNMI targets. A gNMI client speaks to a common gNMI
service endpoint within the network (gNMI gateway) and specifies a gNMI target with an accompanying path.  The gNMI
gateway will in turn initiate the connection to the target device and stream the contents to the originating proxy.

- [gNMI gateway documentation](https://github.com/openconfig/gnmi-gateway)
- [NANOG demonstration](https://www.youtube.com/watch?v=7QXpqqGTRn8)

This demo will start the gNMI gateway binary and use gNMIC to stream to a target which is managed by the gNMI gateway.
Please make adjustments to the `targets.json` file to match your environment.

The demo is dependent on the following files:

- **gnmi-gateway** - The binary to activate gNMI gateway. This must be built for the platform that it will run on.
  Details regarding generation of the binary for the target platform can be found in the [gNMI gateway
  documentation](https://github.com/openconfig/gnmi-gateway).
- **server.crt** / **server.key** - the certificate and key for gNMI gateway.  These can be generated through a CA.
  Additional details may be found [here](/openmgmt/configuration/mtls/).
- **targets.json** - This file specifies the targets.  gNMI-gateway supports hot reloading of the files. So if changes
  are made within targets.json it will reload automatically with new targets and or new paths.

<details><summary>sample: targets.json</summary>
<p>

```javascript
{
  "request": {
    "default": {
      "subscribe": {
        "prefix": {
        },
        "subscription": [
          {
            "path": {
              "elem": [
                {
                  "name": "interfaces"
                }
              ]
            }
          }
        ]
      }
    }
  },
  "target": {
    "DC2-SP02": {
      "addresses": [
        "198.51.100.22:6030"
      ],
      "credentials": {
        "username": "ansible",
        "password": "ansible"
      },
      "request": "default",
      "meta": {
        "NoTLS": "yes"
      }
    },
    "DC2-LEAF1A": {
      "addresses": [
        "198.51.100.5:6030"
      ],
      "credentials": {
        "username": "ansible",
        "password": "ansible"
      },
      "request": "default",
      "meta": {
        "NoTLS": "yes"
      }
    },
    "DC2-LF70": {
      "addresses": [
        "198.51.100.70:6030"
      ],
      "credentials": {
        "username": "ansible",
        "password": "ansible"
      },
      "request": "default",
      "meta": {
        "NoTLS": "yes"
      }
    }
  }
}
```

</p>
</details>

## EOS Configuration

gNMI will need to be enabled on the target which is managed by gNMI gateway and a certificate will need to be installed
to use TLS-based authentication.  Additional details regarding enabling gnmi on EOS devices can be found
[here](/openmgmt/configuration/openconfig/).  Additional details regarding certificate management and configuration can
be found [here](/openmgmt/configuration/mtls/).

## Start gNMI gateway

Note, the `server.crt` must be signed by a CA that the switch can resolve.

```shell
gnmi-gateway -EnableGNMIServer -ServerTLSCert=server.crt \
  -ServerTLSKey=server.key -TargetLoaders=json -TargetJSONFile=targets.json

```

**Output:**
<details><summary>Reveal Output</summary>
<p>

```text
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Starting GNMI Gateway."}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Clustering is NOT enabled. No locking or cluster coordination will happen."}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Starting connection manager."}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Starting gNMI server on 0.0.0.0:9339."}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Connection manager received a target control message: 3 inserts 0 removes"}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Initializing target DC2-SP02 ([198.51.100.22:6030]) map[NoTLS:yes]."}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Initializing target DC2-LEAF1A ([198.51.100.5:6030]) map[NoTLS:yes]."}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Target DC2-SP02: Connecting"}
{"level":"warn","time":"2021-03-19T08:47:35-04:00","message":"DEPRECATED: The 'NoTLS' target flag has been deprecated and will be removed in a future release. Please use 'NoTLSVerify' instead."}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Target DC2-SP02: Subscribing"}
{"level":"info","time":"2021-03-19T08:47:35-04:00","message":"Initializing target DC2-LF70 ([198.51.100.70:6030]) map[NoTLS:yes]."}
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

</p>
</details>

The output indicates that gNMI-gateway has started and will now serve gNMI requests to the `/interfaces/interface` path
on behalf of any external gNMI client.

## Requesting a target managed by gNMI gateway

```shell
gnmic subscribe -a 192.0.2.1 -u ansible -p ansible --port=9339 \
  --skip-verify --target=DC2-SP02 --path=/interfaces
```

**Output:**

```javascript
{
  "source": "192.0.2.1:9339",
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

Since the gNMI gateway is running locally a query can be issued to the service on port 9339 passing in the target value
of `DC2-SP02` and telemetry will start to stream data back to the client.
