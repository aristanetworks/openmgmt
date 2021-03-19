# gNMI SUBSCRIBE RPC Examples

## OpenConfig paths

### Subscribe to all BGP neighbor states

`gnmi -addr 10.83.28.203 -username arista -password arista subscribe '/network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state'`

### Subscribe to specific BGP neighbor state

`gnmi -addr 10.83.28.203 -username arista -password arista subscribe '/network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor[neighbor-address=10.10.10.5]/state'`

### Subscribe with stream mode sample and interval

`gnmi -addr 10.83.13.214:6030 -username admin -password arista -sample_interval 5s -stream_mode sample subscribe '/network-instances/network-instance[name=Tenant_A_WEB_Zone]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=10.255.251.1]/afi-safis/afi-safi[afi-safi-name=openconfig-bgp-types:IPV4_UNICAST]/state/prefixes/received'`
