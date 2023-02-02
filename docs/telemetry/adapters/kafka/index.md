---
layout: default
title: "kafka-telegraf"
date: 2022-03-1 20:03:00 --0600
categories:
---

## Introduction

Kafka is a popular message bus system that allows applications to communicate over a pub/sub bus
as either a publisher or a consumer.
A popular method of distributing streaming telemetry is to take the telemetry data and output it
to a Kafka topic so it can be further reacted upon.

This lab will leverage the Telegraf container to take streaming telemetry
from two cEOS lab devices from their gNMI interfaces and output the data to a Kafka topic.

## Prerequisite

- [Containerlab](https://containerlab.dev/)
- [Docker](https://www.docker.com/)
- [ceos](https://containerlab.dev/manual/kinds/ceos/)

cEOS lab will need to be downloaded from the arista software downloads
and imported via docker with a tag of 4.29.2F

## Environment

The containerlab file
<details><summary>Reveal output</summary>
<p>

```yaml
--8<-- "src/kafka-telegraf/initial.yaml"
```

</p>
</details>

Looking at the telegraf.conf file

<details><summary>Reveal output</summary>
<p>

```bash
--8<-- "src/kafka-telegraf/telegraf.conf"
```

</p>
</details>
We can see that we are going to have telegraf use the
[gnmi input plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/gnmi)
which will simply connect to the two cEOS nodes and start to stream their interface counters and BGP statistics.  
On the outputs portion we can see that we are going to take this gNMI data and send it to the
Kafka broker on the subject of Telegraf.
So any application that connects to the same Kafka broker will also be able to see this data.
This containerlab file will consist of the following Docker containers

- cEOS (2) each running gNMI interface
- Kafka container
- Zookeeper
- Telegraf
- Binary for testing purposes

### Running the lab

```bash
cd src/kafka-telegraf/
containerlab -t initial.yaml deploy
```

Our environment should look as the following

```bash
+---+-----------------------------+--------------+------------------------+-------+---------+------------------+----------------------+
| # |            Name             | Container ID |         Image          | Kind  |  State  |   IPv4 Address   |     IPv6 Address     |
+---+-----------------------------+--------------+------------------------+-------+---------+------------------+----------------------+
| 1 | clab-kafka-ceos1            | 81405697c609 | ceoslab:4.29.2F        | ceos  | running | 172.20.20.101/24 | 2001:172:20:20::6/64 |
| 2 | clab-kafka-ceos2            | 3b3cb2b23537 | ceoslab:4.29.2F        | ceos  | running | 172.20.20.102/24 | 2001:172:20:20::5/64 |
| 3 | clab-kafka-kafka-server     | 25205108237e | bitnami/kafka:latest   | linux | running | 172.20.20.103/24 | 2001:172:20:20::3/64 |
| 4 | clab-kafka-telegraf-server  | 4c5c7e173a55 | telegraf:latest        | linux | running | 172.20.20.105/24 | 2001:172:20:20::4/64 |
| 5 | clab-kafka-zookeeper-server | 9feea244597e | wurstmeister/zookeeper | linux | running | 172.20.20.104/24 | 2001:172:20:20::7/64 |
+---+-----------------------------+--------------+------------------------+-------+---------+------------------+----------------------+
```

### Checking telegraf

docker logs clab-kafka-telegraf-server
<details><summary>Reveal output</summary>
<p>
```bash
2023-02-01T17:16:24Z I! Using config file: /etc/telegraf/telegraf.conf
2023-02-01T17:16:24Z I! Starting Telegraf 1.25.0
2023-02-01T17:16:24Z I! Available plugins: 228 inputs, 9 aggregators, 26 processors, 21 parsers, 57 outputs, 2 secret-stores
2023-02-01T17:16:24Z I! Loaded inputs: gnmi
2023-02-01T17:16:24Z I! Loaded aggregators:
2023-02-01T17:16:24Z I! Loaded processors:
2023-02-01T17:16:24Z I! Loaded secretstores:
2023-02-01T17:16:24Z I! Loaded outputs: kafka
2023-02-01T17:16:24Z I! Tags enabled: host=telegraf-server
2023-02-01T17:16:24Z I! [agent] Config: Interval:10s, Quiet:false, Hostname:"telegraf-server", Flush Interval:10s
2023-02-01T17:16:29Z E! [inputs.gnmi] Error in plugin: failed to setup subscription: rpc error: code = Unavailable desc
2023-02-01T17:16:29Z E! [inputs.gnmi] Error in plugin: failed to setup subscription: rpc error: code = Unavailable desc
```

</p>
</details>

This is okay it reconnects but never tells you it is reconnecting.

### Binary for testing

Since all of our devices are accessible within the same machine there is a small binary that can subscribe to the
same telegraf topic and display information.  
Within the `/bin` directory it is compiled for either darwin or linux/amd64.

```bash
cd /bin
./kafakconsumer --kafka-brokers 172.20.20.103:9092 -kafka-topic telegraf
```

<details><summary>Reveal output</summary>
<p>

```bash
ifcounters,host=telegraf-server,name=Management0,path=openconfig:/interfaces/interface/state/counters,source=clab-kafka-ceos1 
in_broadcast_pkts=0i,in_discards=0i,in_errors=0i,in_fcs_errors=0i,
in_multicast_pkts=0i,out_broadcast_pkts=0i,out_discards=0i,out_errors=0i,out_multicast_pkts=0i 1675272643699038728

ifcounters,host=telegraf-server,name=Management0,path=openconfig:/interfaces/interface/state/counters,source=clab-kafka-ceos1 
in_octets=6886i,in_pkts=65i,in_unicast_pkts=65i,out_octets=2273i,out_pkts=25i,out_unicast_pkts=25i 1675272646690338017

openconfig_bgp,/network-instances/network-instance/protocols/protocol/name=BGP,host=telegraf-server,identifier=BGP,
name=default,source=clab-kafka-ceos2 global/state/router_id="2.2.2.2" 1675271796987568362

openconfig_bgp,/network-instances/network-instance/protocols/protocol/name=BGP,afi_safi_name=IPV4_UNICAST,host=telegraf-server,
identifier=BGP,name=default,neighbor_address=10.0.0.1,source=clab-kafka-ceos2 
neighbors/neighbor/afi_safis/afi_safi/afi_safi_name="openconfig-bgp-types:IPV4_UNICAST" 1675271796630909428

openconfig_bgp,/network-instances/network-instance/protocols/protocol/name=BGP,afi_safi_name=IPV4_UNICAST,host=telegraf-server,
identifier=BGP,name=default,neighbor_address=10.0.0.1,source=clab-kafka-ceos2 
neighbors/neighbor/afi_safis/afi_safi/config/afi_safi_name="openconfig-bgp-types:IPV4_UNICAST" 1675271796630909428
```

</p>
</details>

## Lab Cleanup

```bash
containerlab -t initial.yaml destroy
```

<details><summary>Reveal output</summary>
<p>

```bash
INFO[0000] Parsing & checking topology file: initial.yaml 
INFO[0000] Destroying lab: kafka                        
INFO[0000] Removed container: clab-kafka-telegraf-server 
INFO[0000] Removed container: clab-kafka-zookeeper-server 
INFO[0001] Removed container: clab-kafka-kafka-server   
INFO[0001] Removed container: clab-kafka-ceos2          
INFO[0001] Removed container: clab-kafka-ceos1          
INFO[0001] Removing containerlab host entries from /etc/hosts file 
```

</p>
</details>
The environment should be back to the way it was previously after deletion.
