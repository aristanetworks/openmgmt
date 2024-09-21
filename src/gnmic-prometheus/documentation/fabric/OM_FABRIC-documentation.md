# OM_FABRIC

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| OM_FABRIC | l3leaf | om-pe11 | 172.144.100.4/24 | cEOS-LAB | Provisioned | - |
| OM_FABRIC | l3leaf | om-pe12 | 172.144.100.5/24 | cEOS-LAB | Provisioned | - |
| OM_FABRIC | l3leaf | om-pe21 | 172.144.100.6/24 | cEOS-LAB | Provisioned | - |
| OM_FABRIC | l3leaf | om-pe22 | 172.144.100.7/24 | cEOS-LAB | Provisioned | - |
| OM_FABRIC | spine | om-spine1 | 172.144.100.2/24 | cEOS-LAB | Provisioned | - |
| OM_FABRIC | spine | om-spine2 | 172.144.100.3/24 | cEOS-LAB | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | om-pe11 | Ethernet1 | spine | om-spine1 | Ethernet1 |
| l3leaf | om-pe11 | Ethernet2 | spine | om-spine2 | Ethernet1 |
| l3leaf | om-pe12 | Ethernet1 | spine | om-spine1 | Ethernet2 |
| l3leaf | om-pe12 | Ethernet2 | spine | om-spine2 | Ethernet2 |
| l3leaf | om-pe21 | Ethernet1 | spine | om-spine1 | Ethernet3 |
| l3leaf | om-pe21 | Ethernet2 | spine | om-spine2 | Ethernet3 |
| l3leaf | om-pe22 | Ethernet1 | spine | om-spine1 | Ethernet4 |
| l3leaf | om-pe22 | Ethernet2 | spine | om-spine2 | Ethernet4 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 172.31.255.0/24 | 256 | 16 | 6.25 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| om-pe11 | Ethernet1 | 172.31.255.1/31 | om-spine1 | Ethernet1 | 172.31.255.0/31 |
| om-pe11 | Ethernet2 | 172.31.255.3/31 | om-spine2 | Ethernet1 | 172.31.255.2/31 |
| om-pe12 | Ethernet1 | 172.31.255.5/31 | om-spine1 | Ethernet2 | 172.31.255.4/31 |
| om-pe12 | Ethernet2 | 172.31.255.7/31 | om-spine2 | Ethernet2 | 172.31.255.6/31 |
| om-pe21 | Ethernet1 | 172.31.255.9/31 | om-spine1 | Ethernet3 | 172.31.255.8/31 |
| om-pe21 | Ethernet2 | 172.31.255.11/31 | om-spine2 | Ethernet3 | 172.31.255.10/31 |
| om-pe22 | Ethernet1 | 172.31.255.13/31 | om-spine1 | Ethernet4 | 172.31.255.12/31 |
| om-pe22 | Ethernet2 | 172.31.255.15/31 | om-spine2 | Ethernet4 | 172.31.255.14/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.255.0/24 | 256 | 6 | 2.35 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| OM_FABRIC | om-pe11 | 192.168.255.3/32 |
| OM_FABRIC | om-pe12 | 192.168.255.4/32 |
| OM_FABRIC | om-pe21 | 192.168.255.5/32 |
| OM_FABRIC | om-pe22 | 192.168.255.6/32 |
| OM_FABRIC | om-spine1 | 192.168.255.1/32 |
| OM_FABRIC | om-spine2 | 192.168.255.2/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 192.168.254.0/24 | 256 | 4 | 1.57 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| OM_FABRIC | om-pe11 | 192.168.254.3/32 |
| OM_FABRIC | om-pe12 | 192.168.254.4/32 |
| OM_FABRIC | om-pe21 | 192.168.254.5/32 |
| OM_FABRIC | om-pe22 | 192.168.254.6/32 |
