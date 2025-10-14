# EmbyCrack_Docker

利用 Python 反代理实现 emby 高级会员解锁，支持Emby4.9 +



## 1.安装证书GMCert_RSACA01并添加到受信任

**服务端**、**客户端**均需安装证书（本目录下`GMCert_RSACA01.crt` ）

Docker部署Emby请查看补充




## 2.将本仓库下载到本地并在本文件夹下打开终端



## 3.构建docker镜像

```
docker build -t embycrack:v1 .
```

## 4.更改docker-compose.yaml


```
services:
  dockge:
    image: embycrack:v1
    container_name: embycrack
    restart: always
    ports:
      - 443:443
```

使用docker部署emby建议使用下面配置
```
services:
  dockge:
    image: embycrack:v1
    container_name: mb3admin.com  # 容器名称使用mb3admin.com
    restart: always
    ports:
      - 443:443
    networks:
      - ipv4_ipv6      # 将networks修改成和emby的一致（不要用默认的bridge，新建一个	bridge使用）
networks:
  ipv4_ipv6:        # 这里改成和上面一样
    external: true
```

## 5.启动

```
# 使用docker-compose运行容器
docker-compose up -d
```

## 6.在路由器设置 hosts 或修改本地 hosts

在 hosts 文件中添加的内容：`本机ip mb3admin.com` 

iOS、iPadOS 在未越狱状态下仅能通过路由器 hosts 或利用小火箭、圈 x 等工具解锁



## 7.在 emby 控制台随意输入激活码进行激活

可输入以下网址进行验证：

`https://mb3admin.com/admin/service/registration/validateDevice`

返回以下信息即成功

`{"cacheExpirationDays": 365,"message": "Device Valid","resultCode": "GOOD"}`



# 补充

若使用Docker运行Emby，需将本程序下的`GMCert_RSACA01.crt`证书文件映射到Emby容器中`/etc/ssl/certs`目录下

```
# 在构建Emby容器时添加

# docker
-v your_path/GMCert_RSACA01.crt:/etc/ssl/certs/GMCert_RSACA01.crt

# docker-compose
volumes:
    - your_path/GMCert_RSACA01.crt:/etc/ssl/certs/GMCert_RSACA01.crt
```

