---
layout: default
title: "Arista gNMI client examples"
date: 2021-03-18 12:17:00 --0600
categories:
---

## gNMI GET RPC Examples

### OpenConfig paths

#### Get all information

```shell
gnmi -addr 192.0.2.139:6030 -username admin -password arista get /
```

#### Get the BGP configuration in the default VRF

```shell
gnmi -addr 198.51.100.219:6030 -username admin -password arista \
  get '/network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp'`
```

<details><summary>Reveal output</summary>
<p>

```javascript
/network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp:
{
  "openconfig-network-instance:global": {
 "confederation": {
   "config": {
     "identifier": 0
   },
   "state": {p
     "identifier": 0
   }
 },
 "config": {
   "as": 4206000022,
   "router-id": "0.0.0.0"
 },
 "default-route-distance": {
   "config": {
     "external-route-distance": 200,
     "internal-route-distance": 200
   },
   "state": {
     "external-route-distance": 200,
     "internal-route-distance": 200
   }
 },
 "graceful-restart": {
   "config": {
     "restart-time": 0
   },
   "state": {
     "restart-time": 0
   }
 },
 "route-selection-options": {
   "config": {},
   "state": {}
 },
 "state": {
   "as": 4206000022,
   "router-id": "4.4.4.4"
 }
  },
  "openconfig-network-instance:neighbors": {
 "neighbor": [
   {
     "afi-safis": {
       "afi-safi": [
         {
           "afi-safi-name": "IPV4_UNICAST",
           "config": {
             "afi-safi-name": "IPV4_UNICAST",
             "enabled": false
           },
           "graceful-restart": {
             "config": {
               "enabled": false
             },
             "state": {
               "enabled": false
             }
           },
           "state": {
             "afi-safi-name": "IPV4_UNICAST",
             "enabled": false
           }
         },
         {
           "afi-safi-name": "IPV6_UNICAST",
           "config": {
             "afi-safi-name": "IPV6_UNICAST",
             "enabled": false
           },
           "graceful-restart": {
             "config": {
               "enabled": false
             },
             "state": {
               "enabled": false
             }
           },
           "state": {
             "afi-safi-name": "IPV6_UNICAST",
             "enabled": false
           }
         }
       ]
     },
     "config": {
       "auth-password": "",
       "description": "",
       "local-as": 0,
       "neighbor-address": "3.4.5.6",
       "peer-as": 1,
       "send-community": "NONE"
     },
     "ebgp-multihop": {
       "config": {
         "multihop-ttl": 0
       },
       "state": {
         "multihop-ttl": 0
       }
     },
     "neighbor-address": "3.4.5.6",
     "route-reflector": {
       "config": {
         "route-reflector-client": false
       },
       "state": {
         "route-reflector-client": false
       }
     },
     "state": {
       "auth-password": "",
       "description": "",
       "local-as": 0,
       "peer-as": 1,
       "send-community": "NONE"
     },
     "timers": {
       "config": {
         "hold-time": "180.0",
         "keepalive-interval": "60.0"
       },
       "state": {
         "hold-time": "180.0",
         "keepalive-interval": "60.0"
       }
     },
     "transport": {
       "config": {
         "passive-mode": false
       },
       "state": {
         "passive-mode": false
       }
     }
   },
   {
     "afi-safis": {
       "afi-safi": [
         {
           "afi-safi-name": "IPV4_UNICAST",
           "config": {
             "afi-safi-name": "IPV4_UNICAST",
             "enabled": false
           },
           "graceful-restart": {
             "config": {
               "enabled": false
             },
             "state": {
               "enabled": false
             }
           },
           "state": {
             "afi-safi-name": "IPV4_UNICAST",
             "enabled": false
           }
         },
         {
           "afi-safi-name": "IPV6_UNICAST",
           "config": {
             "afi-safi-name": "IPV6_UNICAST",
             "enabled": false
           },
           "graceful-restart": {
             "config": {
               "enabled": false
             },
             "state": {
               "enabled": false
             }
           },
           "state": {
             "afi-safi-name": "IPV6_UNICAST",
             "enabled": false
           }
         }
       ]
     },
     "config": {
       "auth-password": "",
       "description": "",
       "local-as": 0,
       "neighbor-address": "20.1.1.1",
       "peer-as": 65001,
       "send-community": "NONE"
     },
     "ebgp-multihop": {
       "config": {
         "multihop-ttl": 0
       },
       "state": {
         "multihop-ttl": 0
       }
     },
     "neighbor-address": "20.1.1.1",
     "route-reflector": {
       "config": {
         "route-reflector-client": false
       },
       "state": {
         "route-reflector-client": false
       }
     },
     "state": {
       "auth-password": "",
       "description": "",
       "local-as": 0,
       "peer-as": 65001,
       "send-community": "NONE"
     },
     "timers": {
       "config": {
         "hold-time": "180.0",
         "keepalive-interval": "60.0"
       },
       "state": {
         "hold-time": "180.0",
         "keepalive-interval": "60.0"
       }
     },
     "transport": {
       "config": {
         "passive-mode": false
       },
       "state": {
         "passive-mode": false
       }
     }
   }
 ]
  }
```

</p>
</details>

#### Get BGP neighbors

```shell
gnmi -addr 192.0.2.139 -username admin \
  get '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/neighbors'
```

<details><summary> Reveal output</summary>
<p>

```javascript
/network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors:
{
  "openconfig-network-instance:neighbor": [
    {
      "afi-safis": {
        "afi-safi": [
          {
            "afi-safi-name": "openconfig-bgp-types:IPV6_UNICAST",
            "config": {
              "afi-safi-name": "openconfig-bgp-types:IPV6_UNICAST"
            },
            "state": {
              "afi-safi-name": "openconfig-bgp-types:IPV6_UNICAST",
              "prefixes": {
                "arista-bgp-augments:best-ecmp-paths": 0,
                "arista-bgp-augments:best-paths": 0,
                "installed": 0,
                "received": 0,
                "sent": 0
              }
            }
          },
          {
            "afi-safi-name": "openconfig-bgp-types:L2VPN_EVPN",
            "config": {
              "afi-safi-name": "openconfig-bgp-types:L2VPN_EVPN"
            },
            "state": {
              "afi-safi-name": "openconfig-bgp-types:L2VPN_EVPN",
              "prefixes": {
                "arista-bgp-augments:best-ecmp-paths": 0,
                "arista-bgp-augments:best-paths": 0,
                "installed": 0,
                "received": 0,
                "sent": 0
              }
            }
          },
          {
            "afi-safi-name": "openconfig-bgp-types:IPV4_UNICAST",
            "config": {
              "afi-safi-name": "openconfig-bgp-types:IPV4_UNICAST"
            },
            "state": {
              "afi-safi-name": "openconfig-bgp-types:IPV4_UNICAST",
              "prefixes": {
                "arista-bgp-augments:best-ecmp-paths": 0,
                "arista-bgp-augments:best-paths": 0,
                "installed": 0,
                "received": 0,
                "sent": 0
              }
            }
          }
        ]
      },
      "apply-policy": {
        "config": {
          "default-export-policy": "REJECT_ROUTE",
          "default-import-policy": "REJECT_ROUTE"
        },
        "state": {
          "default-export-policy": "REJECT_ROUTE",
          "default-import-policy": "REJECT_ROUTE"
        }
      },
      "as-path-options": {
        "config": {
          "replace-peer-as": false
        },
        "state": {
          "replace-peer-as": false
        }
      },
      "config": {
        "enabled": true,
        "neighbor-address": "172.168.14.2",
        "peer-as": 65002,
        "send-community": "NONE"
      },
      "ebgp-multihop": {
        "config": {
          "enabled": false,
          "multihop-ttl": 0
        },
        "state": {
          "enabled": false,
          "multihop-ttl": 0
        }
      },
      "neighbor-address": "172.168.14.2",
      "state": {
        "enabled": true,
        "established-transitions": "2",
        "last-established": "1614170027122047488",
        "messages": {
          "received": {
            "UPDATE": "2"
          },
          "sent": {
            "UPDATE": "2"
          }
        },
        "neighbor-address": "172.168.14.2",
        "peer-as": 65002,
        "send-community": "NONE",
        "session-state": "ESTABLISHED"
      },
      "transport": {
        "config": {
          "mtu-discovery": true
        },
        "state": {
          "mtu-discovery": true,
          "remote-address": "172.168.14.2",
          "remote-port": 0
        }
      }
    }
  ]
}
```

</p>
</details>

#### Get all interface descriptions

```shell
gnmi -addr 192.0.2.139:6030 -username admin -password arista \
  get '/interfaces/interface/subinterfaces/subinterface/state/description'
```

```text
/interfaces/interface[name=Ethernet3]/subinterfaces/subinterface[index=0]/state/description: SRV01
/interfaces/interface[name=Ethernet1]/subinterfaces/subinterface[index=0]/state/description: DCI
/interfaces/interface[name=Ethernet2]/subinterfaces/subinterface[index=0]/state/description: To Spines
```

#### Get an interface's description

```shell
gnmi -addr 198.51.100.100:6030 -username admin -password arista \
  get 'interfaces/interface[name=Ethernet1/1]/subinterfaces/subinterface/state/description'
```

```text
/interfaces/interface[name=Ethernet1/1]/subinterfaces/subinterface[index=0]/state/description: "Tyrion"
```

#### Get the operational status of all interfaces

```shell
gnmi -addr 192.0.2.139:6030 -username admin -password arista \
  get 'interfaces/interface/state/oper-status'`
```

##### Get all states of an interface

```shell
gnmi -addr 192.0.2.139:6030 -username cvpadmin -password arista \
  get 'interfaces/interface[name=Ethernet24]/state/'`
```

<details><summary>Reveal output</summary>
<p>

```javascript
/interfaces/interface[name=Ethernet24]/state:
{
  "openconfig-interfaces:admin-status": "UP",
  "openconfig-interfaces:counters": {
    "in-broadcast-pkts": "1",
    "in-discards": "0",
    "in-errors": "0",
    "in-fcs-errors": "0",
    "in-multicast-pkts": "70143",
    "in-octets": "570132503174",
    "in-unicast-pkts": "376128549",
    "out-broadcast-pkts": "2",
    "out-discards": "0",
    "out-errors": "0",
    "out-multicast-pkts": "169207",
    "out-octets": "569979193348",
    "out-unicast-pkts": "376049116"
  },
  "openconfig-interfaces:description": "",
  "openconfig-interfaces:enabled": true,
  "openconfig-platform-port:hardware-port": "Port24",
  "openconfig-interfaces:ifindex": 24,
  "arista-intf-augments:inactive": false,
  "openconfig-interfaces:last-change": "1614001155863084032",
  "openconfig-interfaces:loopback-mode": false,
  "openconfig-interfaces:mtu": 0,
  "openconfig-interfaces:name": "Ethernet24",
  "openconfig-interfaces:oper-status": "UP",
  "openconfig-vlan:tpid": "openconfig-vlan-types:TPID_0X8100",
  "openconfig-interfaces:type": "iana-if-type:ethernetCsmacd"
}
```

</p>
</details>

#### Get an interface's operational status

```shell
gnmi -addr 192.0.2.139:6030 -username cvpadmin -password arista \
  get 'interfaces/interface[name=Ethernet24]/state/oper-status'
```

**Output:**

```text
/interfaces/interface[name=Ethernet24]/state/oper-status: UP
```

#### Get an interface's admin status

```shell
gnmi -addr 192.0.2.139:6030 -username cvpadmin -password arista \
  get 'interfaces/interface[name=Ethernet24]/state/admin-status'`
```

**Output:**

```text
/interfaces/interface[name=Ethernet24]/state/admin-status: UP
```

##### Get the DOM metrics of all interfaces

```shell
gnmi -addr 192.0.2.139:6030 -username cvpadmin -password arista \
  get "components/component/transceiver/physical-channels/channel/state/"
```

#### Get the DOM metrics of an interface

```shell
gnmi -addr 192.0.2.139:6030 -username cvpadmin -password arista \
  get "components/component[name=Ethernet24  transceiver]/transceiver/physical-channels/channel/state/"
```

<details><summary> Reveal output</summary>
<p>

```javascript
/components/component[name=Ethernet24 transceiver]/transceiver/physical-channels/channel[index=0]/state:
{
  "openconfig-platform-transceiver:index": 0,
  "openconfig-platform-transceiver:input-power": {
    "instant": "-0.26"
  },
  "openconfig-platform-transceiver:laser-bias-current": {
    "instant": "7.49"
  },
  "openconfig-platform-transceiver:output-power": {
    "instant": "0.32"
  }
}
```

</p>
</details>

##### Get per core CPU utilization

```shell
gnmi -addr 192.0.2.139:6030 -username cvpadmin -password arista \
  get 'components/component/cpu'
```

<details><summary>Reveal output</summary>
<p>

```javascript
/components/component[name=CPU3]/cpu:
{
  "openconfig-platform-cpu:utilization": {
    "state": {
      "avg": 18,
      "instant": 16,
      "interval": "1000000000000",
      "max": 28,
      "max-time": "3230106984172745216",
      "min": 13,
      "min-time": "3230106514174602752"
    }
  }
}
/components/component[name=CPU0]/cpu:
{
  "openconfig-platform-cpu:utilization": {
    "state": {
      "avg": 17,
      "instant": 16,
      "interval": "1000000000000",
      "max": 25,
      "max-time": "3230106564173730816",
      "min": 12,
      "min-time": "3230106394175068672"
    }
  }
}
/components/component[name=CPU1]/cpu:
{
  "openconfig-platform-cpu:utilization": {
    "state": {
      "avg": 18,
      "instant": 17,
      "interval": "1000000000000",
      "max": 27,
      "max-time": "3230107464174793728",
      "min": 13,
      "min-time": "3230107334172570624"
    }
  }
}
/components/component[name=CPU2]/cpu:
{
  "openconfig-platform-cpu:utilization": {
    "state": {
      "avg": 17,
      "instant": 21,
      "interval": "1000000000000",
      "max": 24,
      "max-time": "3230106924173756928",
      "min": 11,
      "min-time": "3230107394173572608"
    }
  }
}
```

</p>
</details>

##### Get the available/utilized memory

```shell
gnmi -addr 192.0.2.139:6030 -username cvpadmin -password arista \
  get 'components/component/state/memory/'
```

**Output:**

```text
/components/component[name=Chassis]/state/memory:
{
  "openconfig-platform:available": "8298774528",
  "openconfig-platform:utilized": "7706267648"
}
```

##### Get the system environment temperatures

```shell
gnmi -addr 192.0.2.139:6030 -username cvpadmin -password arista \
   get 'components/component/state/temperature/instant'
```

<details><summary>Reveal output</summary>
<p>

```text
/components/component[name=DomTemperatureSensor49]/state/temperature/instant: 30.49609375
/components/component[name=DomTemperatureSensor25]/state/temperature/instant: 24.69921875
/components/component[name=DomTemperatureSensor40]/state/temperature/instant: 25.5078125
/components/component[name=TempSensorP2/2]/state/temperature/instant: 0.0
/components/component[name=TempSensorP1/3]/state/temperature/instant: 40.0
/components/component[name=TempSensorP2/1]/state/temperature/instant: 0.0
/components/component[name=TempSensorP2/3]/state/temperature/instant: 0.0
/components/component[name=DomTemperatureSensor24]/state/temperature/instant: 24.5
/components/component[name=DomTemperatureSensor26]/state/temperature/instant: 23.73046875
/components/component[name=DomTemperatureSensor54]/state/temperature/instant: 27.26953125
/components/component[name=TempSensorP1/1]/state/temperature/instant: 34.0
/components/component[name=DomTemperatureSensor50]/state/temperature/instant: 27.453125
/components/component[name=TempSensorP1/2]/state/temperature/instant: 25.0
/components/component[name=TempSensor1]/state/temperature/instant: 45.84278576588521
/components/component[name=TempSensor15]/state/temperature/instant: 33.875
/components/component[name=TempSensor18]/state/temperature/instant: 44.625
/components/component[name=TempSensor16]/state/temperature/instant: 22.75
/components/component[name=TempSensor17]/state/temperature/instant: 37.0
/components/component[name=TempSensor14]/state/temperature/instant: 37.0
```

</p>
</details>

### EOS Native paths

To get EOS native paths, OCTA has to be enabled as mentioned in the
configuration section. Performing GET/SUBSCRIBE actions using EOS native paths
require changing the origin to `eos_native`.

#### Commonly used paths

- MAC table: `/Smash/bridging/status/smashFdbStatus`
- ARP table: `/Smash/arp/status/arpEntry`
- Neighbor table: `/Smash/arp/status/neighborEntry`
- IPv4 RIB: `/Smash/routing/status/route`
- IPv6 RIB: `/Smash/routing6/status/route`
- IPv4 next-hop table: `/Smash/routing/status/nexthop`
- IPv6 next-hop table: `/Smash/routing6/status/nexthop`
- CPU info: `/Kernel/proc/cpu`
- Process statistics: `/Kernel/proc/stat`
- System info: `/Kernel/sysinfo`
- EOS version: `/Eos/image`
- Interface counters: `/Smash/counters/ethIntf/<agent>/current/counter`
  - Values for `<agent>` are:
    - 7500-family, 7280-family, 7020-family (Arad/Jericho ASICs): `SandCounters`
    - 7300-family, 7250-family, 7050-family, 7010 products, 720-family (Trident
      ASICs): `StrataCounters`
    - For 7060-family, 7260-family (Tomahawk): `Strata-FixedSystem` or
      `StrataCounters` from 4.22+
    - 7150-family products (Alta ASICs): `FocalPointV2`
    - 7160-family products (Cavium/Xpliant ASICs): `XpCounters`
    - 7170-family products (Barefoot ASIC): `BfnCounters`

##### Get CPU utilization

```shell
gnmi -addr 192.0.2.130:6030 -username admin \
  get origin=eos_native '/Kernel/proc/cpu/utilization/total'
```

**Output:**

```text
/Kernel/proc/cpu/utilization/total/nice:
38446
/Kernel/proc/cpu/utilization/total/system:
2347714
/Kernel/proc/cpu/utilization/total/idle:
247720286
/Kernel/proc/cpu/utilization/total/name:
total
/Kernel/proc/cpu/utilization/total/util:
7
/Kernel/proc/cpu/utilization/total/user:
16984784
```

##### Get transceiver DOM temperature

```shell
gnmi -addr 192.0.2.130:6030 -username admin  get origin=eos_native \
  'Sysdb/environment/archer/temperature/status/system/DomTemperatureSensor32'`
```

<details><summary>Reveal output</summary>
<p>

```text
/Sysdb/environment/archer/temperature/status/system/DomTemperatureSensor32/temperature:
{
  "value": 32.5
}
/Sysdb/environment/archer/temperature/status/system/DomTemperatureSensor32/maxTemperature:
{
  "value": 34.88671875
}
/Sysdb/environment/archer/temperature/status/system/DomTemperatureSensor32/maxTemperatureTime: 1564757444.339129
/Sysdb/environment/archer/temperature/status/system/DomTemperatureSensor32/name: DomTemperatureSensor32
/Sysdb/environment/archer/temperature/status/system/DomTemperatureSensor32/generationId: 0
/Sysdb/environment/archer/temperature/status/system/DomTemperatureSensor32/hwStatus: ok
/Sysdb/environment/archer/temperature/status/system/DomTemperatureSensor32/alertRaised: false
/Sysdb/environment/archer/temperature/status/system/DomTemperatureSensor32/alertRaisedCount: 0
/Sysdb/environment/archer/temperature/status/system/DomTemperatureSensor32/lastAlertRaisedTime: 1564194739.259879
```

</p>
</details>

##### Get connectivity monitor host stats

```shell
gnmi -addr 192.0.2.139:6030 -username admin get origin=eos_native '/Sysdb/connectivityMonitor/status/hostStatus/'
```

<details><summary> Reveal output</summary>
<p>

```text
/Sysdb/connectivityMonitor/status/hostStatus/wls100_default/key/hostName: wls100
/Sysdb/connectivityMonitor/status/hostStatus/wls100_default/key/vrfName:
{
  "value": "default"
}
/Sysdb/connectivityMonitor/status/hostStatus/wls100_default/name: wls100_default
/Sysdb/connectivityMonitor/status/hostStatus/wls100_default/defaultStats/packetLoss: 0
/Sysdb/connectivityMonitor/status/hostStatus/wls100_default/defaultStats/httpResponseTime: 0
/Sysdb/connectivityMonitor/status/hostStatus/wls100_default/defaultStats/interfaceName:
/Sysdb/connectivityMonitor/status/hostStatus/wls100_default/defaultStats/jitter: 0
/Sysdb/connectivityMonitor/status/hostStatus/wls100_default/defaultStats/latency: 0
/Sysdb/connectivityMonitor/status/hostStatus/wls100_default/ipAddr: "192.0.2.140"
/Sysdb/connectivityMonitor/status/hostStatus/ats323_management/key/hostName: ats323
/Sysdb/connectivityMonitor/status/hostStatus/ats323_management/key/vrfName:
{
  "value": "management"
}
/Sysdb/connectivityMonitor/status/hostStatus/ats323_management/name: ats323_management
/Sysdb/connectivityMonitor/status/hostStatus/ats323_management/ipAddr: "192.0.2.138"
/Sysdb/connectivityMonitor/status/hostStatus/ats323_management/defaultStats/latency: 0.127
/Sysdb/connectivityMonitor/status/hostStatus/ats323_management/defaultStats/jitter: 0.033
/Sysdb/connectivityMonitor/status/hostStatus/ats323_management/defaultStats/packetLoss: 0
/Sysdb/connectivityMonitor/status/hostStatus/ats323_management/defaultStats/httpResponseTime: 21.860306
/Sysdb/connectivityMonitor/status/hostStatus/ats323_management/defaultStats/interfaceName:
```

</p>
</details>

## gNMI SET RPC Examples

### OpenConfig paths

#### Configure BGP neighbor

##### Configure neighbor address and peer AS

```shell
gnmi -addr 192.0.2.139:6030 -username cvpadmin -password arista \
  update '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=198.51.100.43]' \
  '{"config": {"neighbor-address":"198.51.100.43", "peer-as": 123}}'
```

##### Configure neighbor address, peer AS and send-community

```shell
gnmi -addr 192.0.2.203:6030 -username arista -password arista
  update '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=198.51.100.43]' \
  {"config": {"neighbor-address":"198.51.100.43", "peer-as": 123, "enabled": true, "send-community": "EXTENDED"}}'
```

#### Create peer group

```shell
gnmi -addr 192.0.2.203 -username arista -password arista update \
  '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/peer-groups/peer-group[peer-group-name=XYZ]' \
  '{"config": {"peer-group-name":"XYZ", "local-as": 114}}'
```

#### Update the peer AS

```shell
gnmi -addr 192.0.2.203:6030 -username arista -password arista \
  update '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=198.51.100.0]/config/peer-as' \
  '110'
```

```shell
gnmi -addr 192.0.2.203:6030 -username arista -password arista \
  update '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=198.51.100.0]' \
  '{"config": {"peer-as": 110}}'
```

#### Update the peer group

```shell
gnmi -addr 192.0.2.203:6030 -username arista -password arista \
  update '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=198.51.100.43]/config/peer-group' \
  'XYZ'
```

```shell
gnmi -addr 192.0.2.203:6030 -username arista -password arista \
  update '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp/neighbors/neighbor[neighbor-address=198.51.100.0]' \
  '{"config": {"peer-group": "XYZ","peer-as": 143}}'
```

#### Update BGP config using json file

```shell
gnmi -addr 192.0.2.203:6030 -username arista -password arista \
  update '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP][identifier=BGP]/bgp'
```

<details><summary> Reveal output</summary>
<p>

```javascript
{
    "neighbors": {
        "neighbor": [
            {
                "config": {
                    "enabled": true,
                    "neighbor-address": "10.10.10.154",
                    "peer-group": "XYZ"
                },
                "neighbor-address": "10.10.10.154"
            },
            {
                "config": {
                    "enabled": true,
                    "neighbor-address": "10.10.10.157",
                    "peer-group": "XYZ"
                },
                "neighbor-address": "10.10.10.157"
            }
        ]
    },
    "peer-groups": {
        "peer-group": [
            {
                "config": {
                    "peer-as": 65002,
                    "peer-group-name": "ABC"
                },
                "peer-group-name": "ABC"
            }
        ]
    }
}
```

</p>
</details>

#### Create an ACL

```shell
gnmi -addr 192.0.2.203:6030 -username admin -password arista \
  update /acl/acl-sets acl2.json
```

```shell
cat acl2.json
```

<details><summary>Reveal output</summary>
<p>

```javascript
{
   "acl-set": [
      {
         "config": {
            "name": "test",
            "type": "ACL_IPV4"
         },
         "name": "test",
         "type": "ACL_IPV4",
         "acl-entries": {
            "acl-entry": [
               {
                  "sequence-id": 10,
                  "actions": {
                     "config": {
                        "forwarding-action": "DROP"
                     }
                  },
                  "config": {
                     "sequence-id": 10
                  },
                  "ipv4": {
                     "config": {
                        "destination-address": "192.0.2.1/32",
                        "source-address": "0.0.0.0/0"
                     }
                  }
               }
            ]
         }
      }
   ]
}
```

</p>
</details>

This creates

```text
ip access-list test
   10 deny ip any 1.0.0.0/12
```

#### Shutdown an interface

```shell
gnmi -addr 192.0.2.139:6030 -username arista -password arista  \
  update '/interfaces/interface[name=Ethernet1]/config/enabled' \
  'false'
```

#### Bring up an interface

```shell
gnmi -addr 192.0.2.139:6030 -username arista -password arista  \
  update '/interfaces/interface[name=Ethernet1]/config/enabled' \
  'true'
```

## gNMI SUBSCRIBE RPC Examples

### OpenConfig paths

#### Subscribe to all BGP neighbor states

```shell
gnmi -addr 192.0.2.203 -username arista -password arista \
  subscribe '/network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state'
```

#### Subscribe to specific BGP neighbor state

```shell
gnmi -addr 192.0.2.203 -username arista -password arista \
  subscribe '/network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor[neighbor-address=198.51.100.5]/state'
```

#### Subscribe with stream mode sample and interval

```shell
gnmi -addr 192.0.2.214:6030 -username admin -password arista \
  -sample_interval 5s -stream_mode sample                     \
  subscribe                                                   \
  '/network-instances/network-instance[name=Tenant_A_WEB_Zone]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=198.51.100.1]/afi-safis/afi-safi[afi-safi-name=openconfig-bgp-types:IPV4_UNICAST]/state/prefixes/received'
```

## CLI origin

### Changing the maximum-routes for a BGP neighbor

```shell
gnmi -addr 192.0.2.214:6030 -username arista -password arista \
    update origin=cli "" "router bgp 65101
    neighbor IPv4-UNDERLAY-PEERS maximum-routes 12500"
```

> NOTE the `neighbor` command has to be on a new line, so the previous line should not end in `\`.

### show version

```shell
gnmi -addr 192.0.2.214:6030 -username cvpadmin -password arista \
   get  origin=cli "show version"
```

<details><summary> Reveal output</summary>
<p>

```javascript
/show version:
{
  "architecture": "i686",
  "bootupTimestamp": 1626291561.0,
  "configMacAddress": "00:00:00:00:00:00",
  "hardwareRevision": "",
  "hwMacAddress": "00:00:00:00:00:00",
  "imageFormatVersion": "1.0",
  "internalBuildId": "ed275a6c-1771-482d-829b-125e9c6ba677",
  "internalVersion": "4.26.2F-23035564.riorel",
  "isIntlVersion": false,
  "memFree": 2422124,
  "memTotal": 4002356,
  "mfgName": "Arista",
  "modelName": "vEOS-lab",
  "serialNumber": "BAD032986065E8DC14CBB6472EC314A6",
  "systemMacAddress": "50:08:00:a7:ca:c3",
  "uptime": 1814877.63,
  "version": "4.26.2F-23035564.riorel (engineering build)"
}
```

</p>
</details>
