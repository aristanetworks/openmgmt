from ncclient import manager

eos = manager.connect(
    host="198.51.100.221",
    port="830",
    timeout=30,
    username="arista",
    password="arista",
    hostkey_verify=False,
)

# Edit the running configuration with replace operation

cfg_interface_ethernet3_description = """
<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>Ethernet3</name>
            <config>
                <description nc:operation="replace">This is the new interface description</description>
            </config>
        </interface>
    </interfaces>
</config>
"""
reply = eos.edit_config(
    target="running",
    config=cfg_interface_ethernet3_description,
    default_operation="none",
)

eos.close_session()
