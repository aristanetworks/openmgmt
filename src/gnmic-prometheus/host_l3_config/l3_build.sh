#!/bin/bash


CMD1='cat /etc/hostname; \
sudo vconfig add team0 110; \
sudo ifconfig team0.110 10.1.10.101 netmask 255.255.255.0;\
sudo ip link set up team0.110; \
sudo ip route add 10.1.0.0/16 via 10.1.10.1 dev team0.110; \
sudo ifconfig team0.110; \
sudo route -n
'

CMD2='cat /etc/hostname; \
sudo vconfig add team0 111; \
sudo ifconfig team0.111 10.1.11.102 netmask 255.255.255.0; \
sudo ip link set up team0.111; \
sudo ip route add 10.1.0.0/16 via 10.1.11.1 dev team0.111; \
sudo ifconfig team0.111; \
sudo route -n'

CMD3='cat /etc/hostname; \
sudo vconfig add team0 110; \
sudo ifconfig team0.110 10.1.10.103 netmask 255.255.255.0; \
sudo ip link set up team0.110; \
sudo ip route add 10.1.0.0/16 via 10.1.10.1 dev team0.110; \
sudo ifconfig team0.110; \
sudo route -n
'

CMD4='cat /etc/hostname; \
sudo vconfig add team0 111; \
sudo ifconfig team0.111 10.1.11.104 netmask 255.255.255.0; \
sudo ip link set up team0.111; \
sudo ip route add 10.1.0.0/16 via 10.1.11.1 dev team0.111; \
sudo ifconfig team0.111; \
sudo route -n'

echo "[INFO] Configuring clab-aamh-client1"
docker exec -it  clab-aamh-client1 /bin/sh -c "$CMD1"

echo "[INFO] Configuring clab-aamh-client2"
docker exec -it  clab-aamh-client2 /bin/sh -c "$CMD2"

echo "[INFO] Configuring clab-aamh-client3"
docker exec -it  clab-aamh-client3 /bin/sh -c "$CMD3"

echo "[INFO] Configuring clab-aamh-client4"
docker exec -it  clab-aamh-client4 /bin/sh -c "$CMD4"

echo "[INFO] Completed"

echo "Use [ docker exec -it clab-aamh-client<x> /bin/sh ] to login in host."
