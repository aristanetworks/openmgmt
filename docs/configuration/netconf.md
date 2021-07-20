---
layout: default
title: "NETCONF Device Configuration"
date: 2021-03-02 12:17:00 --0600
categories:
---

## Overview

EOS provides support for managing the switch via NETCONF.

## NETCONF

Currently supported NETCONF operations: get, get-config, get-schema,
edit-config, lock, unlock, close-session, kill-session.

To configure NETCONF in default VRF we can enable the ssh transport under
`management api netconf`:

Default VRF

```text
management api netconf
   transport ssh test
```

Non-default VRF

```text
management api netconf
   transport ssh test
      vrf management
```

Changing the port:

```text
management api netconf
   transport ssh test
      port 830
```

Apply ACL

```text
management api netconf
   transport ssh test
      ip access-group ACCESS_GROUP
```

Note The ACL should be a standard ACL allowing hosts or subnets.

Status check:

```text
#show management api netconf

Enabled:            Yes
Server:             running on port 830, in management VRF
```
