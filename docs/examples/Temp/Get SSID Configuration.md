# Command

python py_gnmicli.py -m get -t \<AP-IP>  -user \<username> -pass \<password> -p \<port> -g -o openconfig.mojonetworks.com -x access-points/access-point[hostname=\<host>]/ssids/ssid[name=\<ssid-name>]/config

# Sample Output

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

  "openconfig-access-points:opmode": 
  "WPA2_PERSONAL", 
  
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
  
  "openconfig-access-points:name": 
  "OCWiFi1", 
  
  "openconfig-access-points:basic-data-rates-2g": [
  
    "openconfig-wifi-types:RATE_11MB", 
    "openconfig-wifi-types:RATE_12MB", 
    "openconfig-wifi-types:RATE_18MB", 
    "openconfig-wifi-types:RATE_24MB", 
    "openconfig-wifi-types:RATE_36MB", 
    "openconfig-wifi-types:RATE_48MB", 
    "openconfig-wifi-types:RATE_54MB"
  ], 
  
  "openconfig-access-points:wpa2-psk": 
  
  "0123456789", 
  
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
