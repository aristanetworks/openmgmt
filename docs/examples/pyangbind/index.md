
PyangBind is a pyang plugin.

## About Pyang

pyang is a python program.

We can use it to:

- Validate YANG modules against YANG RFCs
- Convert YANG modules into equivalent YIN module (XML)
- Generate a tree representation of YANG models for quick visualization

## About PyangBind

It generates Python classes from a YANG module.

It converts YANG module into a Python module, such that Python can be used to generate data which conforms with the data model defined in YANG.

## Install Pyang and Pyangbind

```shell
pip install pyang
pip install pyangbind
```

```shell
pip3 freeze | grep pyang
```

## We need yang modules

### Create a directory

```shell
mkdir yang_modules
```

### Clone the OpenConfig repository


```shell
git clone https://github.com/openconfig/public.git
```
```
ls public
```

### Copy all the YANG files from OpenConfig to the yang_modules directory

```shell
cp public/release/models/*.yang yang_modules/.
cp -R public/release/models/*/*.yang yang_modules/.
cp public/third_party/ietf/*.yang yang_modules/.
```

### Move to the yang_modules directory

It has all the YANG files published on the OpenConfig repository

```shell
cd yang_modules/
ls
```

## Use Pyangbind to generate a Python module from a YANG module

```shell
pyang --plugindir $HOME/.local/lib/python3.6/site-packages/pyangbind/plugin/ -f pybind -o oc_bgp.py openconfig-bgp.yang
```
The above command generated the python module `oc_bgp.py` from the `openconfig-bgp.yang` file
```shell
ls oc_bgp.py
```
## Use the new python module to generate an OpenConfig configuration file

The file [pyangbind_demo.py](../../../src/pyangbind/pyangbind_demo.py) uses the new python module `oc_bgp.py` and generates this OpenConfig configuration file [demo.json](demo.json)

```shell
python3 pyangbind_demo.py
```

## Use gNMI SET RPC to configure a device

This OpenConfig configuration file [demo.json](demo.json) can be loaded on a switch using the gNMI Set RPC

### Install gNMIc

```shell
curl -sL https://github.com/karimra/gnmic/raw/master/install.sh | sudo bash
```

To get the version run:

```shell
gnmic version
```

Output:

```shell
version : 0.17.0
 commit : 278661e
   date : 2021-07-14T07:29:14Z
 gitURL : https://github.com/karimra/gnmic
   docs : https://gnmic.kmrd.dev
```

### Device config

```shell

management api gnmi
   transport grpc default
   provider eos-native

ceos3# show management api gnmi
Octa:               enabled
Enabled:            Yes
Server:             running on port 6030
SSL Profile:        none
QoS DSCP:           none
Authorization Required:No
```

### Use gNMIc to configure the swicth

```shell
gnmic -a 10.73.1.117:6030 --insecure -u arista -p arista get   \
    --path '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp'
```
```shell
show run section bgp
```
```shell
gnmic -a 10.73.1.117:6030 --insecure -u arista -p arista set  \
    --replace-path '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp' --replace-file demo.json
```
```shell
gnmic -a 10.73.1.117:6030 --insecure -u arista -p arista get  \
    --path '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp'
```
```shell
show run section bgp
```