from ncclient import manager
from ncclient.xml_ import to_ele

vlan_id = "7"
vlan_name = "seven"
interface_description = "whatever"
interface = "3"


def vlan_rpc(id, name):
    vlan_rpc = """
    <nc:edit-config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    <target>
    <running/>
    </target>
    <commands>
    <command>vlan %s</command>
    <command>name %s</command>
    </commands>
    </nc:edit-config>
    """ % (
        vlan_id,
        vlan_name,
    )
    return vlan_rpc


def interface_rpc(interface, description, vlan):
    interface_rpc = """
    <nc:edit-config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    <target>
    <running/>
    </target>
    <commands>
    <command>interface ethernet %s</command>
    <command>description %s</command>
    <command>switchport access vlan %s</command>
    </commands>
    </nc:edit-config>
    """ % (
        interface,
        description,
        vlan,
    )
    return interface_rpc


eos = manager.connect(
    host="198.51.100.203",
    port="830",
    timeout=30,
    username="arista",
    password="arista",
    hostkey_verify=False,
)

rpc = vlan_rpc(vlan_id, vlan_name)
rpcreply = eos.dispatch(to_ele(rpc))
print(rpcreply)

rpc = interface_rpc(interface, interface_description, vlan_id)
rpcreply = eos.dispatch(to_ele(rpc))
print(rpcreply)

eos.close_session()
