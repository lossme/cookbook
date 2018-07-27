## elasticsearch

```sh
sudo docker run \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -v /home/key/data/es/data:/usr/share/elasticsearch/data\
    -v /home/key/data/es/config/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml \
    --name=es \
    -d docker.elastic.co/elasticsearch/elasticsearch:5.5.3
```

```sh
sudo sysctl -w vm.max_map_count=262144
```



## kibana

```sh
sudo docker run \
    -p 5601:5601 \
    --link es:elasticsearch \
    --name=kibana \
    -d docker.elastic.co/kibana/kibana:5.5.3
```


## elasticsearch-head
```sh
sudo docker run \
    -p 9100:9100 \
    --name=head \
    -d mobz/elasticsearch-head:5
```
