
PyangBind is a pyang plugin.

## About Pyang

Please visit [this link](../pyang/index.md) if you need help about Pyang.

## About PyangBind

It generates Python classes from a YANG module.

It converts YANG module into a Python module.
This Python module can be then used to generate data which conforms with the data model defined in YANG.

## Install Pyang and Pyangbind

```shell
pip install pyang
pip install pyangbind
```

```shell
pip3 freeze | grep pyang
```

## Get YANG modules

### Create a directory

```shell
mkdir yang_modules
```

### Clone the OpenConfig repository

```shell
git clone https://github.com/openconfig/public.git
```

Run this command to verify

```shell
ls public
```

### Copy all the YANG files from OpenConfig to the yang_modules directory

```shell
cp public/release/models/*.yang yang_modules/.
cp -R public/release/models/*/*.yang yang_modules/.
cp public/third_party/ietf/*.yang yang_modules/.
```

### Move to the yang_modules directory

```shell
cd yang_modules/
```

Verify it has all the YANG files published on the OpenConfig repository

```shell
ls
```

## Use Pyangbind to generate a Python module from a YANG module

```shell
pyang --plugindir $HOME/.local/lib/python3.6/site-packages/pyangbind/plugin/ -f pybind -o oc_bgp.py openconfig-bgp.yang
```

The above command generated the python module `oc_bgp.py` from the `openconfig-bgp.yang` file.
Run this command to verify:

```shell
ls oc_bgp.py
```

## Use the new python module to generate an OpenConfig configuration file

The file [pyangbind_demo.py](https://github.com/aristanetworks/openmgmt/tree/main/src/pyangbind/pyangbind_demo.py) uses the new python module `oc_bgp.py` and generates this OpenConfig configuration file [demo.json](demo.json)

```shell
python3 pyangbind_demo.py
```

## Use gNMI SET RPC to configure a device

This OpenConfig configuration file [demo.json](demo.json) can be loaded on a switch using the gNMI Set RPC
### Install gNMIc

Please visit [this link](../gnmi-clients/gnmic/index.md) if you need help with gNMIc installation
### Required device configuration

Please visit [this link](../gnmi-clients/gnmic/index.md) if you need help to configure EOS for gNMI

### Use gNMIc to configure the swicth
#### Check the device configuration before

```shell
gnmic -a 10.73.1.117:6030 --insecure -u arista -p arista get   \
    --path '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp'
```

```shell
show run section bgp
```

#### Use gNMIc to configure the swicth

```shell
gnmic -a 10.73.1.117:6030 --insecure -u arista -p arista set  \
    --replace-path '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp' --replace-file demo.json
```

#### Check the device configuration after

```shell
gnmic -a 10.73.1.117:6030 --insecure -u arista -p arista get  \
    --path '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp'
```

```shell
show run section bgp
```
