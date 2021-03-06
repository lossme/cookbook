## 1. 创建网络
```sh
sudo docker network create kong-net
```

## 2. 启动数据库
```sh
sudo docker run -d --name kong-database \
              --network=kong-net \
              -p 9042:9042 \
              cassandra:3


# 或者使用 postgres
sudo docker run -d --name kong-database \
              --network=kong-net \
              -p 5432:5432 \
              -e "POSTGRES_USER=kong" \
              -e "POSTGRES_DB=kong" \
              postgres:9.6

```

## 3. 数据库准备
```sh
sudo docker run --rm \
    --network=kong-net \
    -e "KONG_DATABASE=postgres" \
    -e "KONG_PG_HOST=kong-database" \
    -e "KONG_CASSANDRA_CONTACT_POINTS=kong-database" \
    kong:latest kong migrations up
```


## 4. 启动kong
```sh
sudo docker run -d --name kong \
    --network=kong-net \
    -e "KONG_DATABASE=postgres" \
    -e "KONG_PG_HOST=kong-database" \
    -e "KONG_CASSANDRA_CONTACT_POINTS=kong-database" \
    -e "KONG_PROXY_ACCESS_LOG=/dev/stdout" \
    -e "KONG_ADMIN_ACCESS_LOG=/dev/stdout" \
    -e "KONG_PROXY_ERROR_LOG=/dev/stderr" \
    -e "KONG_ADMIN_ERROR_LOG=/dev/stderr" \
    -e "KONG_ADMIN_LISTEN=0.0.0.0:8001, 0.0.0.0:8444 ssl" \
    -p 8000:8000 \
    -p 8443:8443 \
    -p 8001:8001 \
    -p 8444:8444 \
    kong:0.13
```

## 5. 使用

```sh
curl -i http://localhost:8001/
```

## kong-dashboard

- https://github.com/PGBI/kong-dashboard
```sh
sudo docker run -d \
    --name=kong-dashboard \
    -p 8080:8080 \
    --network=kong-net \
    pgbi/kong-dashboard start \
    --kong-url http://kong:8001
```


- https://github.com/pantsel/konga
```sh
sudo docker run -p 1337:1337 \
             --network=kong-net \
             --name konga \
             -e "NODE_ENV=production" \
             pantsel/konga
```
