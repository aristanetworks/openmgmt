# Command
python py_gnmicli.py -m get -t \<AP-IP>  -user \<username> -pass \<password> -p \<port> -g -o openconfig.mojonetworks.com -x access-points/access-point[hostname=\<host>]/ssids/ssid[name=\<ssid-name>]/clients

# Sample Output
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
