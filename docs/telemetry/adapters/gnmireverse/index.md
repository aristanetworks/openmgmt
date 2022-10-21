---
layout: default
title: "gNMIReverse Examples"
date: 2021-05-19 20:03:00 --0600
categories:
---

## Introduction

gNMIReverse is a Dial-Out gRPC service (available on our
[Github](https://github.com/aristanetworks/goarista/tree/master/gnmireverse) page) that reverses the direction of the
dial for gNMI Subscriptions. The gNMIReverse client (running along with gNMI target) on the switch sends data to the
gNMIReverse Server.

This article contains steps on how to build the gNMIReverse client and server binaries and examples on how to configure,
the daemon to run the gNMIReverse client on EOS.

## Prerequisite

The following tools are required to proceed with this setup including cloning the repository and compiling client binary
for EOS.

- [Go](https://golang.org/doc/install)
- [Git](https://www.atlassian.com/git/tutorials/install-git)

## Installing and configuring gNMIReverse client

### Building the client and server binaries

Pull the repository from GitHub (or you can use git clone)

```shell
go get -u github.com/aristanetworks/goarista/gnmireverse
```

Go to the gNMIReverse directory (or the directory to which you have cloned the repo using git clone)

```shell
cd $GOPATH/src/github.com/aristanetworks/goarista/gnmireverse/
```

Compile the package for both server and client

```shell
cd $GOPATH/src/github.com/aristanetworks/goarista/gnmireverse/client
GOOS=linux GOARCH=386 go build

cd $GOPATH/src/github.com/aristanetworks/goarista/gnmireverse/server
GOOS=linux GOARCH=386 go build
```

**NOTE**: For EOS with x86_64 architecture, compile the package as follows for the client:

<pre><code>
cd $GOPATH/src/github.com/aristanetworks/goarista/gnmireverse/client
GOOS=linux GOARCH=<span style="color: red;">amd64</span> go build

cd $GOPATH/src/github.com/aristanetworks/goarista/gnmireverse/server
GOOS=linux GOARCH=<span style="color: red;">amd64</span> go build
</code></pre>

Copy the client binary file to switch **/mnt/flash/** directory

```shell
scp $GOPATH/src/github.com/aristanetworks/goarista/gnmireverse/client/client admin@<switch-MGMT-IP>:/mnt/flash/
```

## gNMIReverse client daemon Configuration

First enable gNMI server on the switch ([Octa](https://eos.arista.com/eos-4-22-1f/octa-single-port-for-gnmi/) can be
enabled if required, as discussed later in this article)

### Non-default VRF

<pre><code>!
management api gnmi
   transport grpc def
       <span style="color: red;">vrf management</span>
   provider eos-native
!</code></pre>

In the above example, we have the gNMI server running on default port 6030 in VRF management on the switch.

<pre><code># show management api gnmi
Octa:               enabled
Enabled:            Yes
<span style="color: red;">Server:             running on port 6030, in management VRF</span>
SSL Profile:        none
QoS DSCP:           none
Authorization Required:No
</code></pre>

gNMIReverse client daemon configuration (non-default VRF):

Note: The `\` elements have been added to aid readability, these should be removed when entering the configuration.

<pre><code>daemon gnmi_reverse_client_1
   exec /mnt/flash/client -username cvpadmin -password arista         \
   <span style="color: red;">  -target_addr=management/127.0.0.1:6030                           \
     -collector_addr=management/198.51.100.115:6000</span>                    \
     -collector_tls=false                                             \
     -target_value=gb421                                              \
     -sample /system/processes/process[pid=*]/state@15s
   no shutdown
</code></pre>

### Default VRF

```shell
!
management api gnmi
   transport grpc def
   provider eos-native
!
```

gNMI server running on default port 6030 in default VRF on the switch.

```shell
# show management api gnmi
Octa:               enabled
Enabled:            Yes
Server:             running on port 6030, in default VRF
SSL Profile:        none
QoS DSCP:           none
Authorization Required:No
```

gNMIReverse client daemon configuration (default VRF):

Note: The `\` elements have been added to aid readability, these should be removed when entering the configuration.

<pre><code>daemon gnmi_reverse_client_1
   exec /mnt/flash/client -username cvpadmin -password arista \
   <span style="color: red;">  -target_addr=127.0.0.1:6030                              \
     -collector_addr=198.51.100.115:6000</span> -collector_tls=false  \
     -target_value=gb421 -sample /system/processes/process[pid=*]/state@15s
   no shutdown
</code></pre>

The gNMIReverse client flags are explained below.

| flag  | description |
| :--- | :--------  |
| username | Username to authenticate with the target (gNMI server)|
| password | Password to authenticate with the target (gNMI server) |
| target_addr | Address of the gNMI server running on the switch. `[<vrf-name>/]address:port` |
| collector_addr | Address of the gNMIReverse server. `[<vrf-name>/]host:port` |
| collector_tls | use TLS in connection with collector (default true) |
| target_value | To include the device name |
| sample | Path to subscribe with SAMPLE subscription mode. `<path>@<time-interval>` <br> Ex. `-sample /interfaces/interface/state/counters@30s` |
| subscribe | Path to subscribe with TARGET_DEFINED subscription mode if there are any changes on the subscribe path |

## Running the gNMIReverse Server

```shell
$ ./server -tls=false -addr=198.51.100.115:6000

[2020-12-28T10:52:17.990029143Z] (gb421) /system/processes/process[pid=1919]/state/cpu-usage-system = 89538
[2020-12-28T10:52:27.990635976Z] (gb421) /system/processes/process[pid=1919]/state/cpu-usage-user = 312674
[2020-12-28T10:52:27.990681209Z] (gb421) /system/processes/process[pid=1919]/state/cpu-utilization = 0
[2020-12-28T10:52:07.990565267Z] (gb421) /system/processes/process[pid=1919]/state/memory-usage = 403599360
[2020-12-28T09:28:37.99397Z] (gb421) /system/processes/process[pid=1919]/state/name = ConfigAgent
[2020-12-28T09:28:27.975545302Z] (gb421) /system/processes/process[pid=1919]/state/pid = 1919
[2020-12-28T09:28:38.058955133Z] (gb421) /system/processes/process[pid=1919]/state/start-time = 1608564420584540928
```

We can see samples from switch gb421 (gNMIReverse client) for the path “/system/processes/process[pid=*]/state” which
will be updated every 15 seconds based on the client daemon configuration.

## Subscribing to eos_native paths

Enable [Octa](https://eos.arista.com/eos-4-22-1f/octa-single-port-for-gnmi/)

<pre><code>!
management api gnmi
   transport grpc def
      vrf management
   <span style="color: red;">provider eos-native</span>
!
</code></pre>

Configure the daemon to subscribe to the eos_native path as in following example:

Note: The `\` elements have been added to aid readability, these should be removed when entering the configuration.

<pre><code>daemon gnmi_reverse_client_1
   exec /mnt/flash/client -username cvpadmin -password arista \
     -target_addr=management/127.0.0.1:6030                   \
     -collector_addr=management/198.51.100.115:6000            \
     -collector_tls=false -target_value=gb421                 \
     -sample /system/processes/process[pid=*]/state@30s       \
     <span style="color: red;">-origin eos_native                                       \
     -subscribe /Kernel/proc/meminfo/</span>
   no shutdown
</code></pre>

On the server side we can see the updates from the same subscription path:

```shell
$ ./server -tls=false -addr=198.51.100.115:6000

[2020-12-29T06:55:15.29120758Z] (gb421) /Kernel/proc/meminfo/memFree = 2482671616
[2020-12-29T06:55:15.29121703Z] (gb421) /Kernel/proc/meminfo/memAvailable = 6465200128
[2020-12-29T06:55:15.29122834Z] (gb421) /Kernel/proc/meminfo/active = 3750023168
[2020-12-29T06:55:15.291235635Z] (gb421) /Kernel/proc/meminfo/activeAnon = 1048485888
[2020-12-29T06:55:15.291254147Z] (gb421) /Kernel/proc/meminfo/anonPages = 991825920
[2020-12-29T06:55:15.291261051Z] (gb421) /Kernel/proc/meminfo/slab = 398680064
[2020-12-29T06:55:15.291265299Z] (gb421) /Kernel/proc/meminfo/sUnreclaim = 218755072
[2020-12-29T06:55:15.291275563Z] (gb421) /Kernel/proc/meminfo/committedAS = 3991588864

[2020-12-29T06:55:25.290455551Z] (gb421) /Kernel/proc/meminfo/memFree = 2482679808
[2020-12-29T06:55:25.29046483Z] (gb421) /Kernel/proc/meminfo/memAvailable = 6465232896
[2020-12-29T06:55:25.290476436Z] (gb421) /Kernel/proc/meminfo/active = 3750035456
[2020-12-29T06:55:25.290486217Z] (gb421) /Kernel/proc/meminfo/activeAnon = 1048498176
[2020-12-29T06:55:25.290507211Z] (gb421) /Kernel/proc/meminfo/anonPages = 991838208
[2020-12-29T06:55:25.290517806Z] (gb421) /Kernel/proc/meminfo/sReclaimable = 179949568
[2020-12-29T06:55:25.290523744Z] (gb421) /Kernel/proc/meminfo/sUnreclaim = 218730496
```

## Subscribing to Smash paths

Enable Smash paths for Octa under **management api models** as follows:

<pre><code>!
management api models
   provider smash
      <span style="color: red;">path routing/status</span>
!
</code></pre>

Configure the gNMIReverse client daemon:

Note: The `\` elements have been added to aid readability, these should be removed when entering the configuration.

<pre><code>daemon gnmi_reverse_client_1
   exec /mnt/flash/client -username cvpadmin -password arista           \
     -target_addr=management/127.0.0.1:6030                             \
     -collector_addr=management/198.51.100.115:6000                      \
     -collector_tls=false -target_value=gb421                           \
     -sample /system/processes/process[pid=*]/state@30s                 \
     <span style="color: red;">-origin eos_native</span>                                                 \
     -subscribe /Kernel/proc/meminfo/                                   \
     <span style="color: red;">-subscribe /Smash/routing/status/</span>
   no shutdown
</code></pre>

On server side we can see updates as follows:

```shell
$ ./server -tls=false -addr=198.51.100.115:6000

[2020-12-29T07:39:33.857345257Z] (gb421) /Smash/routing/status/route/1.1.1.1\/32/storage = 4294967240
[2020-12-29T07:39:33.857345257Z] (gb421) /Smash/routing/status/route/1.1.1.1\/32/routeType = ebgp
[2020-12-29T07:39:33.857345257Z] (gb421) /Smash/routing/status/route/1.1.1.1\/32/fecId = {"value":12884901894}
[2020-12-29T07:39:33.857345257Z] (gb421) /Smash/routing/status/route/1.1.1.1\/32/key = "1.1.1.1/32"
[2020-12-29T07:39:33.857345257Z] (gb421) /Smash/routing/status/route/1.1.1.1\/32/metric = {"value":0}
```

## References

[Github](https://github.com/aristanetworks/goarista/tree/master/gnmireverse)
