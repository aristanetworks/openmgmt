---
layout: default
title: "WiFi"
date: 2021-10-10 12:17:00 --0600
categories:
---

## Overview 

Add overview


#### Get AP

```shell
python py_gnmicli.py -m get -t <AP-IP> -x /provision-aps -user <username> -pass <password> -p <port> -g -o openconfig.mojonetworks.com
```

<details><summary>Reveal output</summary>
<p>

```javascript
{
  "openconfig-ap-manager:provision-ap": [
    {
      "mac": "30:86:2D:B0:0F:EF", 
      "config": {
        "country-code": "IN", 
        "hostname": "arista"
      }, 
      "state": {
        "country-code": "IN", 
        "hostname": "arista"
      }
    }
  ]
}
```

</p>
</details>

#### Get operating frequencies (bands) of SSID

```shell
python py_gnmicli.py -m get -t <AP-IP>  -user <username> -pass <password> -p <port> -g -o openconfig.mojonetworks.com -x access-points/access-point[hostname=<host>]/ssids/ssid[name=<ssid-name>]/state/operating-frequency
```

<details><summary>Reveal output</summary>
<p>

```javascript
FREQ_2_5_GHZ
```

</p>
</details>

#### Get SSID Configuration

```shell
python py_gnmicli.py -m get -t <AP-IP>  -user <username> -pass <password> -p <port> -g -o openconfig.mojonetworks.com -x access-points/access-point[hostname=<host>]/ssids/ssid[name=<ssid-name>]/config
```

<details><summary>Reveal output</summary>
<p>

```javascript
{
  "openconfig-access-points:dva": true, 
  "openconfig-access-points:supported-data-rates-5g": [
    "openconfig-wifi-types:RATE_11MB", 
    "openconfig-wifi-types:RATE_12MB", 
    "openconfig-wifi-types:RATE_18MB", 
    "openconfig-wifi-types:RATE_24MB", 
    "openconfig-wifi-types:RATE_36MB", 
    "openconfig-wifi-types:RATE_48MB", 
    "openconfig-wifi-types:RATE_54MB"
  ], 
  "openconfig-access-points:opmode": "WPA2_PERSONAL", 
  "openconfig-access-points:okc": true, 
  "openconfig-access-points:supported-data-rates-2g": [
    "openconfig-wifi-types:RATE_11MB", 
    "openconfig-wifi-types:RATE_12MB", 
    "openconfig-wifi-types:RATE_18MB", 
    "openconfig-wifi-types:RATE_24MB", 
    "openconfig-wifi-types:RATE_36MB", 
    "openconfig-wifi-types:RATE_48MB", 
    "openconfig-wifi-types:RATE_54MB"
  ], 
  "openconfig-access-points:name": "OCWiFi1", 
  "openconfig-access-points:basic-data-rates-2g": [
    "openconfig-wifi-types:RATE_11MB", 
    "openconfig-wifi-types:RATE_12MB", 
    "openconfig-wifi-types:RATE_18MB", 
    "openconfig-wifi-types:RATE_24MB", 
    "openconfig-wifi-types:RATE_36MB", 
    "openconfig-wifi-types:RATE_48MB", 
    "openconfig-wifi-types:RATE_54MB"
  ], 
  "openconfig-access-points:wpa2-psk": "0123456789", 
  "openconfig-access-points:basic-data-rates-5g": [
    "openconfig-wifi-types:RATE_11MB", 
    "openconfig-wifi-types:RATE_12MB", 
    "openconfig-wifi-types:RATE_18MB", 
    "openconfig-wifi-types:RATE_24MB", 
    "openconfig-wifi-types:RATE_36MB", 
    "openconfig-wifi-types:RATE_48MB", 
    "openconfig-wifi-types:RATE_54MB"
  ]
}

```

</p>
</details>


#### Get clients for SSID

```shell
python py_gnmicli.py -m get -t <AP-IP>  -user <username> -pass <password> -p <port> -g -o openconfig.mojonetworks.com -x access-points/access-point[hostname=<host>]/ssids/ssid[name=<ssid-name>]/clients
```

<details><summary>Reveal output</summary>
<p>

```javascript
{
  "openconfig-access-points:client": [
    {
      "mac": "C2:2F:42:79:CB:BA", 
      "client-rf": {
        "state": {
          "phy-rate": 0, 
          "rssi": -52, 
          "frequency": 0, 
          "snr": 42, 
          "ss": 0
        }
      }, 
      "state": {
        "mac": "C2:2F:42:79:CB:BA", 
        "counters": {
          "tx-bytes": "34707", 
          "tx-retries": "0", 
          "rx-bytes": "19705", 
          "rx-retries": "18"
        }
      }, 
      "client-connection": {
        "state": {
          "username": "", 
          "client-state": "openconfig-wifi-types:AUTHENTICATED", 
          "hostname": "", 
          "operating-system": "", 
          "ipv6-addresses": [
            "fe80::c02f:42ff:fe79:cbba"
          ], 
          "ipv4-address": [
            "192.168.29.250"
          ], 
          "connection-time": "1628849487411018113"
        }
      }
    }
  ]
}

```
</p>
</details>

#### Get operating channel of radio


```shell
python py_gnmicli.py -m get -t <AP-IP>  -user <username> -pass <password> -p <port> -g -o openconfig.mojonetworks.com -x access-points/access-point[hostname=<host>]/radios/radio[id=1][operating-frequency=FREQ_5GHZ]/state/channel
```

<details><summary>Reveal output</summary>
<p>

```javascript
{
  timestamp: 1628855017049472718
  update {
    path {
      elem {
        name: "access-points"
      }
      elem {
        name: "access-point"
        key {
          key: "hostname"
          value: "arista"
        }
      }
      elem {
        name: "radios"
      }
      elem {
        name: "radio"
        key {
          key: "id"
          value: "1"
        }
        key {
          key: "operating-frequency"
          value: "FREQ_5GHZ"
        }
      }
      elem {
        name: "state"
      }
      elem {
        name: "channel"
      }
    }
    val {
      uint_val: 36
    }
  }
}

```

</p>
</details>

#### Get operating EIRP of radio

```shell
python py_gnmicli.py -m get -t <AP-IP>  -user <username> -pass <password> -p <port> -g -o openconfig.mojonetworks.com -x access-points/access-point[hostname=<host>]/radios/radio[id=1][operating-frequency=FREQ_5GHZ]/state/transmit-eirp
```
<details><summary>Reveal output</summary>
<p>

```javascript
{
  timestamp: 1628855017049472718
  update {
    path {
      elem {
        name: "access-points"
      }
      elem {
        name: "access-point"
        key {
          key: "hostname"
          value: "arista"
        }
      }
      elem {
        name: "radios"
      }
      elem {
        name: "radio"
        key {
          key: "id"
          value: "1"
        }
        key {
          key: "operating-frequency"
          value: "FREQ_5GHZ"
        }
      }
      elem {
        name: "state"
      }
      elem {
        name: "transmit-eirp"
      }
    }
    val {
      uint_val: 28
    }
  }
}
```

</p>
</details>

#### Set operating channel of radio

```shell
python py_gnmicli.py -m set-replace-t <AP-IP>  -user <username> -pass <password> -p <port> -g -o openconfig.mojonetworks.com -x access-points/access-point[hostname=<host>]/radios/radio[id=1][operating-frequency=FREQ_5GHZ]/config/channel -val 169
```

<details><summary>Reveal output</summary>
<p>

```javascript
response {
  path {
    elem {
      name: "access-points"
    }
    elem {
      name: "access-point"
      key {
        key: "hostname"
        value: "arista"
      }
    }
    elem {
      name: "radios"
    }
    elem {
      name: "radio"
      key {
        key: "id"
        value: "1"
      }
      key {
        key: "operating-frequency"
        value: "FREQ_5GHZ"
      }
    }
    elem {
      name: "config"
    }
    elem {
      name: "channel"
    }
  }
  op: REPLACE
}

```

</p>
</details>