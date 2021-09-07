# Command
python py_gnmicli.py -m get -t \<AP-IP>  -user \<username> -pass \<password> -p \<port> -g -o openconfig.mojonetworks.com -x access-points/access-point[hostname=\<host>]/radios/radio[id=1][operating-frequency=FREQ_5GHZ]/state/channel

# Sample Output
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
