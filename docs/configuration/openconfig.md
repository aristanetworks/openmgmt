---
layout: default
title: "OpenConfig Configuration"
date: 2021-03-02 12:17:00 --0600
categories:
---

## Overview

EOS supports the OpenConfig gNMI interface for device management.

### Platform compatibility

All EOS flavors support OpenConfig (phyiscal, virtual, containerized, cloud).

### gNMI

To start the gNMI server, which listens by default on TCP/6030 configure the gRPC transport under `management api gnmi`
in the global config mode:

Default VRF

```text
management api gnmi
  transport grpc openmgmt
```

Non-default VRF

```text
management api gnmi
   transport grpc openmgmt
     vrf management
```

Changing the port:

```text
management api gnmi
   transport grpc openmgmt
      port 5900
```

Apply ACL

```text
management api gnmi
   transport grpc openmgmt
      ip access-group ACCESS_GROUP
```

Note, the ACL should be a standard ACL allowing hosts or subnets.

Authenticate the connection with TLS

```text
management api gnmi
   transport grpc openmgmt
      ssl profile PROFILE
```

Enable authorization of incoming requests

```text
management api gnmi
   transport grpc openmgmt
      authorization requests
```

Status check

```text
#show management api gnmi
Octa:               No
Enabled:            Yes
Server:             running on port 6030, in default VRF
SSL Profile:        none
QoS DSCP:           none
```

### OCTA

The OpenConfig agent (gNMI API) can leverage the EOS state streaming agent's (TerminAttr) libraries, thus exposing EOS
native paths. If Octa (OpenConfig + TerminAttr) is enabled then OpenConfig, in addition to accepting OpenConfig paths in
gNMI get/subscribe requests, will also support EOS native paths (e.g. Sysdb/Smash paths). This feature was introduced in
`4.22.1F`.

gNMI requests received by Octa are interpreted as either OpenConfig or TerminAttr requests, as follows.

- gNMI requests containing an origin of `eos_native` are processed as as native path requests.
- Requests lacking an origin of `eos_native` are treated as OpenConfig requests.

A gNMI client that supports specification of an origin as part of the associated RPC is a requirement.

Note support for sending GET/SUBSCRIBE requests to both an openconfig and an eos-native path in the same call is not yet
supported.

#### How to enable Octa

Octa can be enable by adding `provider eos-native` under `management api gnmi`

`SW(config-mgmt-api-gnmi)#provider eos-native`

Status check

```text
#show management api gnmi
Octa:               enabled
Enabled:            Yes
Server:             running on port 6030, in default VRF
SSL Profile:        none
QoS DSCP:           none
```

##### API models

Starting in EOS `4.24.0F` it is possible to configure the Smash paths that Octa has access to. Under the `management api
models` mode, the provider smash sub-mode allows for enabling or disabling a Smash path with the `[no] path
smash_path_here [disabled]` command.

```text
management api models
   provider smash
      path forwarding/status
      path routing/status disabled
      path routing/isis/lsdb
```

Note that every time a new path is added the Octa agent has to be restarted.
EOS CLI:

```text
management api gnmi
   transport grpc <NAME>
   shutdown
   no shutdown
```

Bash:
`$ sudo killall Octa`

Alternatively `agent Octa terminate` can be used from EOS CLI as well.

`show management api models` will list the Smash paths enabled/disabled

e.g.:

```text
#show management api models
provider smash
  path /Smash/bridging
  path /Smash/forwarding/status
  path /Smash/routing/isis/lsdb
  path /Smash/routing
  path /Smash/routing/status disabled
provider sysdb
```

## AAA Accounting for gNMI/OpenConfig

Starting with EOS 4.27.2F `accounting requests` can be enabled to account records for gNMI/gNOI RPCs:

```text
management api gnmi
   transport grpc default
      authorization requests
      accounting requests
   provider eos-native
!
aaa accounting commands all default start-stop logging
```

we can also use these commands to log to tacacs+ or radius and syslog too

```text
aaa accounting commands all default start-stop group tacacs+
aaa accounting commands all default start-stop group radius
```

```text
spine1# sh management api gnmi 
Octa: enabled

Transport: default
Enabled: yes
Server: running on port 6030, in default VRF
SSL profile: none
QoS DSCP: none
Authorization required: yes
Accounting requests: yes
Certificate username authentication: no
Notification timestamp: last change time
Listen addresses: ::
spine1#
```

Configuration change using OpenConfig and gNMI:

```text
$ gnmic -a 192.168.0.10:6030 -u arista -p arista77rx --insecure set --update-path "/interfaces/interface[name=Ethernet1]/config/description" --update-value "test"
{
  "source": "192.168.0.10:6030",
  "timestamp": 1663615213475353999,
  "time": "2022-09-19T19:20:13.475353999Z",
  "results": [
    {
      "operation": "UPDATE",
      "path": "interfaces/interface[name=Ethernet1]/config/description"
    }
  ]
}
```

```text
$ gnmic -a 192.168.0.10:6030 -u arista -p arista77rx --insecure get --path "/interfaces/interface[name=Ethernet1]/config/description"
[
  {
    "source": "192.168.0.10:6030",
    "timestamp": 1663615224964145128,
    "time": "2022-09-19T19:20:24.964145128Z",
    "updates": [
      {
        "Path": "interfaces/interface[name=Ethernet1]/config/description",
        "values": {
          "interfaces/interface/config/description": "test"
        }
      }
    ]
  }
] 
```

Syslog messages on the device:

```text
spine1#sh logging last 5 minutes
Sep 19 19:20:13 spine1 Aaa: %ACCOUNTING-6-CMD: arista unknown unknown stop task_id=34 start_time=1663615213.48 timezone=UTC service=shell priv-lvl=15 cmd=OpenConfig.Set addr=192.168.0.1:57388 rpc=/gnmi.gNMI/Set request={"update":[{"path":"/interfaces/interface[name=Ethernet1]/config/description","val":"\\"test\\""}]} <cr>
Sep 19 19:20:13 spine1 ConfigAgent: %SYS-5-CONFIG_SESSION_ENTERED: User arista entered configuration session session11521733719371 on GNMI (192.168.0.1:57388)
Sep 19 19:20:13 spine1 ConfigAgent: %SYS-5-CONFIG_SESSION_COMMIT_SUCCESS: User arista committed configuration session session11521733719371 successfully on GNMI (192.168.0.1:57388)
Sep 19 19:20:13 spine1 ConfigAgent: %SYS-5-CONFIG_SESSION_EXITED: User arista exited configuration session session11521733719371 on GNMI (192.168.0.1:57388)
Sep 19 19:20:24 spine1 Aaa: %ACCOUNTING-6-CMD: arista unknown unknown stop task_id=35 start_time=1663615224.96 timezone=UTC service=shell priv-lvl=15 cmd=OpenConfig.Get addr=192.168.0.1:57428 rpc=/gnmi.gNMI/Get request={"path":[{"path":"/interfaces/interface[name=Ethernet1]/config/description"}]} <cr>
```

```text
spine1#trace monitor octa
--- Monitoring /var/log/agents/Octa-3748 ---
I0919 19:20:13.715618    3748 router.go:234] Cli commands:
configure session session11521733719371
interface Ethernet1
description test
exit
configure session session11521733719371 commit
^Cspine1#
```

```text
spine1#bash ps -ef | grep Octa
root      3748   480  2 16:51 ?        00:03:20 /usr/bin/Octa --agenttitle=Octa
```

```text
spine1#bash  more /var/log/agents/Octa-3748 | tail -4
interface Ethernet1
description test
exit
configure session session11521733719371 commit
spine1#
```

### Limitations

An accounting record is limited to a maximum of 8098 characters.  
The record will be truncated if it exceeds the maximum character length.

## gNMI per-RPC role authorizations

Starting in EOS `4.24.1F` it is possible to perform authorization of each RPC (i.e. GET, SET, SUBSCRIBE), if
authorization requests is supplied as described above.

During authorization, the OpenConfig agent will communicate with the AAA agent, allowing authorization policies or roles
to permit or deny the new tokens OpenConfig.Get and OpenConfig.Set.

For example, a role may be defined such as:

```text
role oc-read
   10 permit command OpenConfig.Get
```

A user which is assigned to this role would be allowed to issue a gNMI GET or SUBSCRIBE request, but not a SET request.

> Note that this is only available for gNMI.

## Enable AFT mapping

By default, mapping of the FIB (forwarding information base) to the OpenConfig AFT (abstract forwarding table) model is
disabled, as the volume of data can be large.

Starting in EOS `4.25.1F` it is possible to enable these mappings, for IPV4, IPV6, or both, as described below:

```text
management api models
   provider aft
      ipv4-unicast
      ipv6-unicast
```

> Note that prior to EOS 4.27 a restart of the gNMI agent is required, e.g.: `agent Octa terminate` or
> `agent OpenConfig terminate` (in case the eos-native provider is not enabled).

## Telemetry Timestamps

Per the GNMI specification, the default timestamp field of a notification message is set to be the time at which the
value of the underlying data source changes or when the reported event takes place.  In order to facilitate integration
in legacy environments oriented around polling style operations, an option to support overriding the timestamp field to
the send-time is available. (as of 4.27.0F)

Overriding the timestamp to `send-time` is applicable to all STREAM and POLL subscriptions.

Configuration is outlined below.

```text
management api gnmi
   transport grpc <NAME>
      notification timestamp send-time
```

If there's a need to return to the standards-oriented operation, the following mechanisms can be used to reset the
behavior.

```text
no notification timestamp send-time
default notification timestamp
notification timestamp last-change-time
```

<details><summary>Validation</summary>
<p>

```text
#show management api gnmi
Octa: enabled
Set persistence: enabled

Transport: default
Enabled: yes
Server: running on port 6030, in default VRF
SSL profile: none
QoS DSCP: none
Authorization required: no
Accounting requests: no
Certificate username authentication: no
Notification timestamp: send time  !! note: timestamp mode
Listen addresses: ::
```

</p>
</details>

## Configuration Persistence

By default, within EOS, the application of gNMI `Set` RPCs are not persisted to the `startup-config`.  A `copy
running-config startup-config` is required in order to save configuration updates imposed via gNMI.

As of EOS 4.28.0F, if the operator desires to be able to save gNMI-driven configuration automatically, persistence can be
enabled by adding the following configuration. With this option, all gnmi `Set` operations will be saved to the
`startup-config`. Note, the configuration is saved using Arista's EOS configuration syntax and there is no corresponding
presentation of the OpenConfig syntax.

```text
management api gnmi
   transport grpc <NAME>
   operation set persistence
```

If there is a need to return to the default mode of gNMI configuration non-persistence, this can be disabled using the
following commands.

```text
no operation set persistence
default operation set persistence
```

<details><summary>Validation</summary>
<p>

```text
#show management api gnmi
Octa: enabled
Set persistence: enabled  !! note: persistence state

Transport: default
Enabled: yes
Server: running on port 6030, in default VRF
SSL profile: none
QoS DSCP: none
Authorization required: no
Accounting requests: no
Certificate username authentication: no
Notification timestamp: last change time
Listen addresses: ::
```

</p>
</details>

## Troubleshooting

The OpenConfig agent handles all transports described above: gNMI, RESTCONF, and
NETCONF. The agent log file is present at `/var/log/agents/OpenConfig-{PID}`.
Lines that begin with `E` are errors. Debug logging can be enabled with a
regular trace command. Here are a couple of examples:

`(config)#trace OpenConfig setting server/9` - For server (gNMI) traces

`(config)#trace OpenConfig setting */9` - For all traces with verbose setting

similarly if Octa is enabled:

`(config)#trace Octa setting server/9` - For server (gNMI) traces

`(config)#trace Octa setting */9` - For all traces with verbose setting

## Limitations

- In EOS versions prior to `4.24.0F`, not all Smash paths were accessible via Octa.
- Starting in EOS `4.24.0F` configuring the Smash paths that Octa has access to will also affect OpenConfig. Enabling a
  Smash path for Octa can result in extra YANG paths being populated in OpenConfig. Disabling a Smash path can result in
  having some YANG paths missing in OpenConfig.
- The `%<zone-id>` optional suffix in YANG `ietf:ipv4-address`, and `ietf:ipv6-address` types are not supported.
- An OpenConfig client update/merge/replace request can erase config that is not modified by the incoming request. This
  happens if a config that is part of a certain mount point but not supported by OpenConfig is configured via CLI prior
  to the OpenConfig client update/merge/replace request is processed.

## Supported OpenConfig paths

Please refer to the [EOS Central TOIs](https://eos.arista.com/toi/) to see the new list of paths supported per release.

For convenience, supported paths may be found at: <https://eos.arista.com/path-report>.

## References / Resources

- The OpenConfig working group: [http://openconfig.net/](http://openconfig.net/)
- Repository of gNMI specifications: [https://github.com/openconfig/reference/](https://github.com/openconfig/reference/)
