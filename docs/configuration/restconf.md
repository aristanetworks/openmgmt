---
layout: default
title: "RESTCONF Configuration"
date: 2021-03-02 12:17:00 --0600
categories:
---

## Overview

EOS provides support for RESTCONF and the necessary transport services to support it.

The RESTCONF server is in the EOS device.

## RESTCONF configuration on EOS

### Certificate

Certificate-based authentication is required for RESTCONF to operate.  You should follow the instructions in the
[Certificate Authentication](/configuration/mtls.html) section in order to generate and install a certificate to support
RESTCONF in your environment.  Alternately, a self-signed certificate may be generated on the switch and certificate
validation can be handled appropriately by remote RESTCONF clients.

The following Cli command generates a self-signed cert:

```text
security pki certificate generate self-signed restconf.crt key restconf.key generate rsa 2048 parameters common-name restconf
```

Create ssl profile:

```text
management security
   ssl profile restconf
   certificate restconf.crt key restconf.key
```

### RESTCONF API

Configure RESTCONF:

Default VRF:

```text
management api restconf
   transport https test
   ssl profile restconf
```

Non-default VRF

```text
management api restconf
   transport https test
   ssl profile restconf
   vrf management
```

Changing the port:

```text
management api restconf
   transport https test
      port 5900
```

Apply ACL

```text
management api restconf
   transport https test
      ip access-group ACCESS_GROUP
```

>Note The ACL should be a standard ACL allowing hosts or subnets.

### Control-plane ACL

The default RESTCONF port on Arista devices is TCP 6020.

We need to change the default control-plane ACL on EOS in order to allow TCP 6020 (or to allow the configured RESTCONF port).

Please refer to [this link](../configuration/security.md)

### Status check

```text
#show management api restconf
Enabled:            Yes
Server:             running on port 6020, in management VRF
SSL Profile:        restconf
QoS DSCP:           none
```
