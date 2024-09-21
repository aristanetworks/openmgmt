---
layout: default
title: "prometheus-grafana"
date: 2024-09-21 20:00:00 +0100
categories:
---

## Introduction

Prometheus is an open-source monitoring and alerting toolkit designed primarily for cloud-native environments, including Kubernetes. Developed by SoundCloud in 2012, it has gained popularity due to its ability to collect and store metrics as time-series data, which includes timestamps and optional key-value pairs known as labels. (1) // --> TODO add citation

Prometheus operates on a pull-based model, where it scrapes metrics from HTTP endpoints exposed by monitored services, storing this data in a time-series database. Users can query this data using PromQL, a powerful query language, to generate alerts and visualize metrics through tools like Grafana. (2) // --> TODO add citation

Since joining the Cloud Native Computing Foundation in 2016, Prometheus has become a cornerstone in the monitoring landscape, particularly suited for dynamic service-oriented architectures and microservices. (3) // --> TODO add citation

## Prerequisite

- [Containerlab](https://containerlab.dev/)
- [Docker](https://www.docker.com/)
- [cEOS](https://containerlab.dev/manual/kinds/ceos/)

cEOS lab will need to be downloaded from the arista software downloads
and imported via docker with a tag of e.g. 4.32.2F

## Environment

// TODO Add  small diagram

The Containerlab file

<details><summary>Reveal output</summary>
<p>

```yaml
--8<-- "src/gnmic-prometheus/topology.yaml"
```

</p>
</details>

Looking at the `gnmic.yml` file

<details><summary>Reveal output</summary>
<p>

```bash
--8<-- "src/gnmic-prometheus/gnmic.yml"
```

We can see that we're going to use `gnmic` to subscribe to several OpenConfig and EOS native paths and write the data into
Prometheus either in their raw states or modifying them with [processors](https://gnmic.openconfig.net/user_guide/event_processors/intro/), which
are needed due to Prometheus only accepting numerical values.

</p>
</details>

### Running the lab

```bash
cd src/gnmic-prometheus/
containerlab -t topology.yaml deploy
```

or

`containerlab -t topology.yaml deploy --reconfigure` on subsequent runs when modifications are made

Our environment should look as the following:

```
+----+--------------------+--------------+-------------------------------------------------------------+-------+---------+--------------------+------------------------+
| #  |        Name        | Container ID |                            Image                            | Kind  |  State  |    IPv4 Address    |      IPv6 Address      |
+----+--------------------+--------------+-------------------------------------------------------------+-------+---------+--------------------+------------------------+
|  1 | clab-om-avd        | 2b71ef8fe868 | ghcr.io/aristanetworks/avd/universal:python3.12-avd-v4.10.2 | linux | running | 172.144.100.230/24 | 2001:172:144:100::7/80 |
|  2 | clab-om-client1    | 5d6f06a162d3 | alpine-host                                                 | linux | running | 172.144.100.8/24   | 2001:172:144:100::8/80 |
|  3 | clab-om-client2    | 95642c587a14 | alpine-host                                                 | linux | running | 172.144.100.9/24   | 2001:172:144:100::9/80 |
|  4 | clab-om-client3    | d4fd040c251b | alpine-host                                                 | linux | running | 172.144.100.10/24  | 2001:172:144:100::a/80 |
|  5 | clab-om-client4    | f98b0a992d42 | alpine-host                                                 | linux | running | 172.144.100.11/24  | 2001:172:144:100::c/80 |
|  6 | clab-om-gnmic      | 7676f355ade9 | ghcr.io/openconfig/gnmic:0.38.2                             | linux | running | 172.144.100.200/24 | 2001:172:144:100::2/80 |
|  7 | clab-om-grafana    | 0fa1af12aac9 | grafana/grafana:11.2.0                                      | linux | running | 172.144.100.220/24 | 2001:172:144:100::d/80 |
|  8 | clab-om-om-pe11    | bd4888d56a1a | ceosimage:4.32.2F                                           | ceos  | running | 172.144.100.4/24   | 2001:172:144:100::4/80 |
|  9 | clab-om-om-pe12    | 51fe187893c7 | ceosimage:4.32.2F                                           | ceos  | running | 172.144.100.5/24   | 2001:172:144:100::b/80 |
| 10 | clab-om-om-pe21    | b9ed639155cb | ceosimage:4.32.2F                                           | ceos  | running | 172.144.100.6/24   | 2001:172:144:100::3/80 |
| 11 | clab-om-om-pe22    | 2b0061a2aec0 | ceosimage:4.32.2F                                           | ceos  | running | 172.144.100.7/24   | 2001:172:144:100::f/80 |
| 12 | clab-om-om-spine1  | 582e33ddbdb6 | ceosimage:4.32.2F                                           | ceos  | running | 172.144.100.2/24   | 2001:172:144:100::5/80 |
| 13 | clab-om-om-spine2  | a5f28f53582e | ceosimage:4.32.2F                                           | ceos  | running | 172.144.100.3/24   | 2001:172:144:100::6/80 |
| 14 | clab-om-prometheus | 04cdbdd65795 | prom/prometheus:v2.54.1                                     | linux | running | 172.144.100.210/24 | 2001:172:144:100::e/80 |
+----+--------------------+--------------+-------------------------------------------------------------+-------+---------+--------------------+------------------------+
```

Now we're ready to access Grafana at http://myserver:3001 (arista/arista)

To add additional configurations to the switches, such as configuring EVPN we can use the `clab-om-avd` container and run the ansible playbook inside:

```
docker exec -it clab-om-avd zsh
cd project
ansible-playbook playbooks/fabric-deploy-config.yaml -i inventory.yaml
```

> NOTE You might need to create the avd user on the host if it doesn't exist, otherwise the container won't be able to create files.

```
useradd avd
usermod -aG wheel avd
chown -R avd:avd ./
```
