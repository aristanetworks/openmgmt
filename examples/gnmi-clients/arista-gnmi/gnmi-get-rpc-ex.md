## gNMI GET RPC Examples

### Get all information

`gnmi -addr 10.83.13.139:6030 -username admin -password arista get /`

### Get the BGP configuration in the default VRF

`gnmi -addr 172.28.160.219:6030 -username admin -password arista get '/network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp'`

<details><summary> Reveal output</summary>
<p>

```text
/network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp:
{
  "openconfig-network-instance:global": {
 "confederation": {
   "config": {
     "identifier": 0
   },
   "state": {
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

### Get BGP neighbors

`gnmi -addr 10.83.13.139 -username admin get '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/neighbors'`

<details><summary> Reveal output</summary>
<p>

```text

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

### Get all interface descriptions

`gnmi -addr 10.83.13.139:6030 -username admin -password arista get '/interfaces/interface/subinterfaces/subinterface/state/description'`

```text
/interfaces/interface[name=Ethernet3]/subinterfaces/subinterface[index=0]/state/description:
SRV01
/interfaces/interface[name=Ethernet1]/subinterfaces/subinterface[index=0]/state/description:
DCI
/interfaces/interface[name=Ethernet2]/subinterfaces/subinterface[index=0]/state/description:
To Spines
```

### Get an interface's description

`./gnmi -addr 10.81.117.100:6030 -username admin -password arista get 'interfaces/interface[name=Ethernet1/1]/subinterfaces/subinterface/state/description'`

```text
/interfaces/interface[name=Ethernet1/1]/subinterfaces/subinterface[index=0]/state/description:
"Tyrion"
```

### Get the operational status of all interfaces

`gnmi -addr 10.83.13.139:6030 -username admin -password arista get 'interfaces/interface/state/oper-status'`

### Get all states of an interface

`gnmi -addr 10.83.13.139:6030 -username cvpadmin -password arastra get 'interfaces/interface[name=Ethernet24]/state/'`

<details><summary> Reveal output</summary>
<p>

```text
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

### Get an interface's operational status

`gnmi -addr 10.83.13.139:6030 -username cvpadmin -password arastra get 'interfaces/interface[name=Ethernet24]/state/oper-status'`

```text
/interfaces/interface[name=Ethernet24]/state/oper-status:
UP
```

### Get an interface's admin status

`gnmi -addr 10.83.13.139:6030 -username cvpadmin -password arastra get 'interfaces/interface[name=Ethernet24]/state/admin-status'`

```text
/interfaces/interface[name=Ethernet24]/state/admin-status:
UP
```

### Get the DOM metrics of all interfaces

`gnmi -addr 10.83.13.139:6030 -username cvpadmin -password arastra get "components/component/transceiver/physical-channels/channel/state/"`

### Get the DOM metrics of an interface

`gnmi -addr 10.83.13.139:6030 -username cvpadmin -password arastra get "components/component[name=Ethernet24 transceiver]/transceiver/physical-channels/channel/state/"`

<details><summary> Reveal output</summary>
<p>

```text
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

### Get per core CPU utilization

`gnmi -addr 10.83.13.139:6030 -username cvpadmin -password arastra get 'components/component/cpu'`

<details><summary> Reveal output</summary>
<p>

```text
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

### Get the available/utilized memory

`gnmi -addr 10.83.13.139:6030 -username cvpadmin -password arastra get 'components/component/state/memory/'`

```text
/components/component[name=Chassis]/state/memory:
{
  "openconfig-platform:available": "8298774528",
  "openconfig-platform:utilized": "7706267648"
}
```

### Get the system environment temperatures

`gnmi -addr 10.83.13.139:6030 -username cvpadmin -password arastra get 'components/component/state/temperature/instant'`

<details><summary> Reveal output</summary>
<p>

```text
/components/component[name=DomTemperatureSensor49]/state/temperature/instant:
30.49609375
/components/component[name=DomTemperatureSensor25]/state/temperature/instant:
24.69921875
/components/component[name=DomTemperatureSensor40]/state/temperature/instant:
25.5078125
/components/component[name=TempSensorP2/2]/state/temperature/instant:
0.0
/components/component[name=TempSensorP1/3]/state/temperature/instant:
40.0
/components/component[name=TempSensorP2/1]/state/temperature/instant:
0.0
/components/component[name=TempSensorP2/3]/state/temperature/instant:
0.0
/components/component[name=DomTemperatureSensor24]/state/temperature/instant:
24.5
/components/component[name=DomTemperatureSensor26]/state/temperature/instant:
23.73046875
/components/component[name=DomTemperatureSensor54]/state/temperature/instant:
27.26953125
/components/component[name=TempSensorP1/1]/state/temperature/instant:
34.0
/components/component[name=DomTemperatureSensor50]/state/temperature/instant:
27.453125
/components/component[name=TempSensorP1/2]/state/temperature/instant:
25.0
/components/component[name=TempSensor1]/state/temperature/instant:
45.84278576588521
/components/component[name=TempSensor15]/state/temperature/instant:
33.875
/components/component[name=TempSensor18]/state/temperature/instant:
44.625
/components/component[name=TempSensor16]/state/temperature/instant:
22.75
/components/component[name=TempSensor17]/state/temperature/instant:
37.0
/components/component[name=TempSensor14]/state/temperature/instant:
37.0
```

</p>
</details>
