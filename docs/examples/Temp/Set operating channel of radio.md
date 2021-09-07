# Command
python py_gnmicli.py -m set-replace-t \<AP-IP>  -user \<username> -pass \<password> -p \<port> -g -o openconfig.mojonetworks.com -x access-points/access-point[hostname=\<host>]/radios/radio[id=1][operating-frequency=FREQ_5GHZ]/config/channel -val 169

# Sample Output
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
