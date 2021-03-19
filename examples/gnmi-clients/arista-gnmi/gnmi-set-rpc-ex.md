# gNMI SET RPC Examples

## OpenConfig paths

### Configure BGP neighbor

#### Configure neighbor address and peer AS

```text
gnmi -addr 10.83.13.139:6030 -username cvpadmin -password arastra update  '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/neighbors/neighbor[neighbor-address=10.10.100.43]' '{"config": {"neighbor-address":"10.10.100.43", "peer-as": 123}}'
```

#### Configure neighbor address, peer AS and send-community

```text
gnmi -addr 10.83.28.203:6030 -username arista -password arista update '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/neighbors/neighbor[neighbor-address=10.10.100.43]' '{"config": {"neighbor-address":"10.10.100.43", "peer-as": 123, "enabled": true, "send-community": "EXTENDED"}}'
```

### Create peer group

```text
gnmi -addr 10.83.28.203 -username arista -password arista update '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/peer-groups/peer-group[peer-group-name=XYZ]' '{"config": {"peer-group-name":"XYZ", "local-as": 114}}'
```

### Update the peer AS

```text
gnmi -addr 10.83.28.203:6030 -username arista -password arista update '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/neighbors/neighbor[neighbor-address=10.10.10.0]/config/peer-as' '110'
```

```text
gnmi -addr 10.83.28.203:6030 -username arista -password arista update '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/neighbors/neighbor[neighbor-address=10.10.10.0]' '{"config": {"peer-as": 110}}'
```

### Update the peer group

```text
gnmi -addr 10.83.28.203:6030 -username arista -password arista update '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/neighbors/neighbor[neighbor-address=10.10.100.43]/config/peer-group' 'XYZ'
```

```text
gnmi -addr 10.83.28.203:6030 -username arista -password arista update '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/neighbors/neighbor[neighbor-address=10.10.10.0]' '{"config": {"peer-group": "XYZ","peer-as": 143}}'
```

### Update BGP config using json file

`gnmi -addr 10.83.28.203:6030 -username arista -password arista update '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp'`

<details><summary> Reveal output</summary>
<p>

```text
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

### Create an ACL

`gnmi -addr 10.83.28.203:6030 -username admin -password arista update /acl/acl-sets acl2.json`

cat acl2.json

<details><summary> Reveal output</summary>
<p>

```text
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
                        "destination-address": "1.2.3.4/12",
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

### Shutdown an interface

```text
gnmi -addr 10.83.13.139:6030 -username arista -password arista update '/interfaces/interface[name=Ethernet1]/config/enabled' 'false'
```

### Bring up an interface

```text
gnmi -addr 10.83.13.139:6030 -username arista -password arista update '/interfaces/interface[name=Ethernet1]/config/enabled' 'true'
```
