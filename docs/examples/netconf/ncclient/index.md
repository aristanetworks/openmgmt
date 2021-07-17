---
layout: default
title: "ncclient examples"
date: 2021-07-16 12:17:00 --0600
categories:
---

## About NETCONF

NETCONF is a protocol defined in the [RFC 6241](https://tools.ietf.org/html/rfc6241)

## Install ncclient

```shell
pip install ncclient
```

```shell
pip3 freeze | grep ncclient
```

## Requirements on the EOS device

```shell
switch1#show running-config section netconf
management api netconf
   transport ssh test
      vrf MGMT
```
```shell
switch1#sh management api netconf
Enabled:            Yes
Server:             running on port 830, in MGMT VRF
```

## ncclient demo

### interactive python session

```
>>> from ncclient import manager
>>> eos=manager.connect(host="10.83.28.221", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)
>>>
>>> eos.connected
True
>>> eos.timeout
30
>>> eos.session_id
'1292406600'
>>>
>>> assert("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring" in eos.server_capabilities), "NetConf server not compliant with https://tools.ietf.org/html/rfc6022"
>>>
>>> conf = '''
... <config>
...     <system xmlns="http://openconfig.net/yang/system">
...         <config>
...             <domain-name>abc.xyz</domain-name>
...         </config>
...     </system>
... </config>
... '''
>>>
>>> eos.edit_config(target = "running", config = conf, default_operation="merge")
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:33ca18d3-43b5-4277-a6ce-9a751f74cada"><ok></ok></rpc-reply>
>>>
>>> domain_name='''
... <system xmlns="http://openconfig.net/yang/system">
...     <config>
...         <domain-name>
...         </domain-name>
...     </config>
... </system>
... '''
>>>
>>> domain_name_conf = eos.get_config(source="running", filter=("subtree", domain_name))
>>> print (domain_name_conf)
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:a43cfae5-3215-4f99-97ce-ff61ca1e285c"><data time-modified="2021-07-11T12:29:49.133333939Z"><system xmlns="http://openconfig.net/yang/system"><config><domain-name>abc.xyz</domain-name></config></system></data></rpc-reply>
>>>
>>> eos.close_session()
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:1841896a-9c97-467d-aef8-9a405b51d298"><ok></ok></rpc-reply>
>>>
>>> eos.connected
False
>>>
>>> exit()
```
```
>>> from lxml import etree
>>>
>>> system_e = etree.Element("system")
>>> dns_e = etree.SubElement(system_e, "dns")
>>> servers_e = etree.SubElement(dns_e, "servers")
>>> server_e = etree.SubElement(servers_e, "server")
>>> address_e = etree.SubElement(server_e, "address")
>>> config_e = etree.SubElement(server_e, "config")
>>> address_e.text = "8.8.8.8"
>>>
>>> address_e.text
'8.8.8.8'
>>>
>>> etree.tostring(system_e)
b'<system><dns><servers><server><address>8.8.8.8</address><config/></server></servers></dns></system>'
>>>
>>> etree.tostring(system_e, pretty_print = True)
b'<system>\n  <dns>\n    <servers>\n      <server>\n        <address>8.8.8.8</address>\n        <config/>\n      </server>\n    </servers>\n  </dns>\n</system>\n'
>>>
>>> etree.dump(system_e)
<system>
  <dns>
    <servers>
      <server>
        <address>8.8.8.8</address>
        <config/>
      </server>
    </servers>
  </dns>
</system>
>>>
>>> from ncclient import manager
>>> eos=manager.connect(host="10.83.28.221", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)
>>> eos.connected
True
>>>
>>> print(eos.get_config(source="running", filter=("subtree", system_e)))
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:ab16e734-04df-4d4f-8efe-27963ece586c"><data time-modified="2021-07-11T12:29:49.138275819Z"><system xmlns="http://openconfig.net/yang/system"><dns><servers><server><address>8.8.8.8</address><config><address>8.8.8.8</address></config></server></servers></dns></system></data></rpc-reply>
>>>
>>> eos.close_session()
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:2eed88ee-106b-44d1-b196-f79611512b25"><ok></ok></rpc-reply>
>>>
>>> exit()
```

### other demos

There are many python scripts using ncclient in this [directory](../../../../src/ncclient/):

- The script [print_client_capabilities.py](../../../../src/ncclient/print_client_capabilities.py) prints the NETCONF client capabilities.
- The script [print_server_capabilities.py](../../../../src/ncclient/print_server_capabilities.py) prints the NETCONF server capabilities.
- The script [get.py](../../../../src/ncclient/get.py) uses the `get` operation to retrieve the configuration and state data. It uses a filter to specify the portion of the configuration and state data to retrieve.
- The script [get_config.py](../../../../src/ncclient/get_config.py) uses the `get-config` operation with a filter to retrieve part of the configuration.
- The script [parse_xml_output.py](../../../../src/ncclient/parse_xml_output.py) uses the `get` operation to retrieve data from the device and then parse this data.
- The script [edit_config_merge.py](../../../../src/ncclient/edit_config_merge.py) uses the `edit-config` operation with the `merge` operation (which is the default operation for `edit-config`)
- The script [edit_config_replace.py](../../../../src/ncclient/edit_config_replace.py) uses the `edit-config` operation with the `replace` operation
- The script [edit_config_delete.py](../../../../src/ncclient/edit_config_delete.py)
uses the `edit-config` operation with the `delete` operation
- The script [EOS_commands_with_NETCONF.py](../../../../src/ncclient/EOS_commands_with_NETCONF.py) configures a device using the `edit-config` operation and EOS data model
- The script [candidate_configuration_commit.py](../../../../src/ncclient/candidate_configuration_commit.py) uses the `edit-config` operation with the `candidate` configuration datastore. It uses a `lock` operation and `commit` operation.
- The script [candidate_configuration_discard_changes.py](../../../../src/ncclient/candidate_configuration_discard_changes.py). uses the `edit-config` operation with the `candidate` configuration datastore. It uses a `lock` operation and `discard_change` operation to revert the candidate configuration to the current running configuration (insteaf of commiting the candidate configuration).
- The script [rpc.py](../../../../src/ncclient/rpc.py) sends RPCs to configure EOS devices.

To execute one of these scripts, run as example this command:
```shell
python 3 print_server_capabilities.py
```