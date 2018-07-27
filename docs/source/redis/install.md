## install
```sh
docker run --name=redis \
    -p 6379:6379 \
    -v /home/key/data/redis:/data \
    -d redis redis-server
```
