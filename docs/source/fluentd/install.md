## install
```sh
sudo docker run \
    -p 24224:24224 \
    -p 24224:24224/udp \
    -v /home/key/data/fluentd/config:/fluentd/etc \
    -e FLUENTD_CONF=fluentd.conf \
    -v /home/key/data/fluentd/data:/fluentd/log \
    --link es:elasticsearch \
    --name=fluentd \
    fluent/fluentd
```
