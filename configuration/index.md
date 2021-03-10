---
layout: page
title: "Device Configuration"
date: 2021-03-02 12:17:00 --0600
categories:
---

## overview

## CLI

## OpenConfig (configuration)
----

### GNMI

To start the gNMI server, which listens by default on TCP/6030 configured the gRPC transport
under `management api gnmi` in the global config mode:

Default VRF

```
management api gnmi
  transport grpc openmgmt
```

Non-default VRF

```
management api gnmi
   transport grpc openmgmt
     vrf management
```

Changing the port:

```
management api gnmi
   transport grpc openmgmt
      port 5900
```

Apply ACL

```
management api gnmi
   transport grpc openmgmt
      ip access-group ACCESS_GROUP
```

Authenticate the connection with TLS

```
management api gnmi
   transport grpc openmgmt
      ssl profile PROFILE
```

Enable authorization of incoming requests

```
management api gnmi
   transport grpc openmgmt
      authorization requests
```


## RPCs

### RPC: SetRequest()

### RPCs and role authorization

Starting in EOS 4.24.1F it is possible to perform authorization of each RPC (i.e. GET, SET, SUBSCRIBE), if authorization requests is supplied as described above.

During authorization, the OpenConfig agent will communicate with the AAA agent, allowing authorization policies or roles to permit or deny the new tokens OpenConfig.Get and OpenConfig.Set.

For example, a role may be defined such as:

```
role oc-read
   10 permit command OpenConfig.Get
```

A user which is assigned to this role would be allowed to issue a gNMI get or subscribe request, but not a set request.

> Note that this is only available for gNMI.
## References / Resources

The OpenConfig working group: [http://openconfig.net/](http://openconfig.net/)

Repository of OpenConfig YANG models: [https://github.com/openconfig/public](https://github.com/openconfig/public)

Repository of gNMI specifications: [https://github.com/openconfig/reference/](https://github.com/openconfig/reference/)

YANG RFC: [https://tools.ietf.org/html/rfc6020](https://tools.ietf.org/html/rfc6020)

NETCONF RFC: [https://tools.ietf.org/html/rfc6241](https://tools.ietf.org/html/rfc6241)

RESTCONF RFC: [https://tools.ietf.org/html/rfc8040](https://tools.ietf.org/html/rfc8040)