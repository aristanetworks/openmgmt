# The arista-cli.yang https://github.com/aristanetworks/yang/blob/master/EOS-4.24.2F/experimental/eos/models/arista-cli.yang module defines the namespace "http://arista.com/yang/cli" with the YANG container "commands" and leaf-list "command" in order to use EOS CLI with NETCONF 

from ncclient import manager
eos=manager.connect(host="10.73.1.105", port="830", timeout=30, username="arista", password="arista", hostkey_verify=False)
vlan ='''
    <config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <commands xmlns="http://arista.com/yang/cli">
            <command>vlan 98</command>
            <command>name test98</command>
            <command>interface ethernet6</command>
            <command>description test</command>
            <command>switchport access vlan 98</command>
        </commands>
    </config>
'''
reply = eos.edit_config(target="running", config=vlan, default_operation="merge")
