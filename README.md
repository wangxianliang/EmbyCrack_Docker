# EmbyCrack_Docker

利用 Nginx 反代理实现 emby 高级会员解锁



## 1.安装证书GMCert_RSACA01并添加到受信任

**服务端**、**客户端**均需安装证书（本目录下`GMCert_RSACA01.crt` ）

Docker部署Emby请查看补充




## 2.将本仓库下载到本地并在本文件夹下打开终端



## 3.启动Nginx反向代理

### Emby v4.9.0.33及之后版本（感谢[@potatoru](https://github.com/potatoru)提供的方法）

#### 第一步：获取ServerID

​	方法一：通过日志获取，打开emby控制台，点击日志，下载embyserver.txt，查找serverID即可获取

![image-20250506211553008](https://github.com/AlanZhai/EmbyCrack_Docker/blob/main/pic/681a0b86693c2.png)

​	方法二：打开Emby配置文件夹，data目录下的device.txt文件获取

![image-20250506211643363](https://github.com/AlanZhai/EmbyCrack_Docker/blob/main/pic/681a0bb8ca3a4.png)

#### 第二步：获取key值并更新config/emby.conf文件

```
# 需要有python运行环境

# 在本程序目录下执行
python key.py

# 输入第一步获取到的ServerID，提示
```

![image-20250506212327851](https://github.com/AlanZhai/EmbyCrack_Docker/blob/main/pic/681a0d4d636cd.png)

#### 第三步：启动nginx反代

```
# 拉取nginx镜像
docker pull nginx:latest

# 使用docker-compose运行容器（一定要在本仓库文件夹内运行）
docker-compose up -d
```

### Emby v4.9.0.33之前的版本直接执行第三步即可

```
# 拉取nginx镜像
docker pull nginx:latest

# 使用docker-compose运行容器（一定要在本仓库文件夹内运行）
docker-compose up -d
```

### 

## 4.在路由器设置 hosts 或修改本地 hosts

在 hosts 文件中添加的内容：`本机ip mb3admin.com` 

iOS、iPadOS 在未越狱状态下仅能通过路由器 hosts 或利用小火箭、圈 x 等工具解锁



## 5.在 emby 控制台随意输入激活码进行激活

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

