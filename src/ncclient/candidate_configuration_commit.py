# This file shows an example with the edit-config NETCONF operation and the candidate configuration datastore.

cfg_system = """
<config>
    <system xmlns="http://openconfig.net/yang/system">
        <config>
            <domain-name>abc.xyz</domain-name>
            <hostname>switch1</hostname>
            <login-banner>Access to this swicth is stricly restticted to authorized persons only. Every activity on this system is monitored. </login-banner>
        </config>
        <dns>
            <servers>
                <server>
                    <address>8.8.8.8</address>
                    <config>
                        <address>8.8.8.8</address>
                    </config>
                </server>
                <server>
                    <address>1.1.1.1</address>
                    <config>
                        <address>1.1.1.1</address>
                    </config>
                </server>
            </servers>
        </dns>
    </system>
</config>
"""

cfg_interface_ethernet3_description = """
<config>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>Ethernet3</name>
            <config>
                <description>This is the best</description>
            </config>
        </interface>
    </interfaces>
</config>
"""

from ncclient import manager

with manager.connect(
    host="198.51.100.221",
    port="830",
    timeout=30,
    username="arista",
    password="arista",
    hostkey_verify=False,
) as eos:
    with eos.locked("candidate"):
        eos.edit_config(
            target="candidate", config=cfg_system, default_operation="merge"
        )
        eos.edit_config(
            target="candidate",
            config=cfg_interface_ethernet3_description,
            default_operation="merge",
        )
        eos.commit()
