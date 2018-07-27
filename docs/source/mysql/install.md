## 安装
```sh
# 拉取镜像
sudo docker pull mysql/mysql-server:5.7
# 从镜像中创建容器
sudo docker run \
    -v /home/key/data/mysql/data:/var/lib/mysql \
    -v /home/key/data/mysql/config/mysqld_charset.cnf:/etc/mysql/my.cnf \
    --name=mysql \
    -p 3306:3306 \
    -e MYSQL_ROOT_PASSWORD=root \
    -d mysql/mysql-server:5.7
```

### 字符集配置

- `mysqld_charset.cnf`
```
[mysqld]
character_set_server=utf8
character_set_filesystem=utf8
collation-server=utf8_general_ci
init-connect='SET NAMES utf8'
init_connect='SET collation_connection = utf8_general_ci'
skip-character-set-client-handshake
```
