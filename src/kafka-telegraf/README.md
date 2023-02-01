#### Start containerlab

containerlab -t initial.yaml deploy

Should look similar to the following...

```
root@dhertzberg:/home/dhertzberg/projects/kafkaout# docker ps
CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS          PORTS                                                                                                                                                                NAMES
733aa8bc40f2   bitnami/kafka:latest     "/opt/bitnami/script…"   20 minutes ago   Up 20 minutes   0.0.0.0:9000->9000/tcp, :::9000->9000/tcp, 0.0.0.0:9092->9092/tcp, :::9092->9092/tcp                                                                                 clab-kafka-kafka-server
db1b45ca5bfc   ceoslab:4.29.2F          "bash -c '/mnt/flash…"   20 minutes ago   Up 19 minutes   0.0.0.0:6040->6040/tcp, :::6040->6040/tcp, 0.0.0.0:888->80/tcp, :::888->80/tcp, 0.0.0.0:4444->443/tcp, :::4444->443/tcp, 0.0.0.0:4001->6030/tcp, :::4001->6030/tcp   clab-kafka-ceos1
4e3b3841ec14   telegraf:latest          "/entrypoint.sh tele…"   20 minutes ago   Up 20 minutes   8092/udp, 8125/udp, 8094/tcp                                                                                                                                         clab-kafka-telegraf-server
a498332de682   ceoslab:4.29.2F          "bash -c '/mnt/flash…"   20 minutes ago   Up 19 minutes   0.0.0.0:889->80/tcp, :::889->80/tcp, 0.0.0.0:4445->443/tcp, :::4445->443/tcp, 0.0.0.0:4002->6030/tcp, :::4002->6030/tcp, 0.0.0.0:6041->6040/tcp, :::6041->6040/tcp   clab-kafka-ceos2
4f90fdc4d811   wurstmeister/zookeeper   "/bin/sh -c '/usr/sb…"   20 minutes ago   Up 19 minutes   22/tcp, 2888/tcp, 3888/tcp, 0.0.0.0:2181->2181/tcp, :::2181->2181/tcp                                                                                                clab-kafka-zookeeper-server
```

#### Check to see the kafkaoutput
This may be a firehose of information..
cb bin
sudo chmod u+x kafakconsumer
./kafakconsumer --kafka-brokers 172.20.20.103:9092 -kafka-topic telegraf

Or if you want to make the updates not come out like a firehose

./kafakconsumer --kafka-brokers 172.20.20.4:9092 -kafka-topic telegraf kafka-time 1

### Example output

message at topic/partition/offset telegraf/0/6159: openconfig_bgp,host=telegraf-server,identifier=BGP,name=default,neighbor_address=10.0.0.1,openconfig:/network-instances/network-instance/protocols/protocol/name=BGP,path=openconfig:/network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/transport/state,source=clab-kafka-ceos2 neighbors/neighbor/transport/state/remote_address="10.0.0.1",neighbors/neighbor/transport/state/remote_port=0i 1674652981478679384

### Destroy when finished
containerlab -t initial.yaml destroy