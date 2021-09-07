# Command

python py_gnmicli.py -m get -t \<AP-IP> -x /provision-aps -user \<username> -pass \<password> -p \<port> -g -o openconfig.mojonetworks.com

# Sample Output

{

  "openconfig-ap-manager:provision-ap": [
     
       {
          "mac": 
       "30:86:2D:B0:0F:EF", 
      
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
