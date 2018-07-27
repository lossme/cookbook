## install
```sh
docker run \
  --name nginx \
  -d -p 80:80 \
  -v /home/key/git/cookbook/docs/build/html:/usr/share/nginx/html \
  nginx

```
