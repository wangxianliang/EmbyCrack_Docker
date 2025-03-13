# EmbyCrack_Docker

利用 Nginx 反代理实现 emby 高级会员解锁



## 1.安装证书GMCert_RSACA01并添加到受信任

证书服务端、客户端均需安装（证书在程序目录下）
`GMCert_RSACA01.cer` `GMCert_RSACA01.cert` 为同一证书，windows 安装 cer 后缀即可

## 2.将本仓库下载到本地并在本文件夹下打开终端



## 3.Docker安装nginx服务

```
# 第一步：拉取nginx镜像
docker pull nginx:latest

#第二步：使用docker-compose运行容器（一定要在本仓库文件夹内运行）
docker-compose up -d
```



## 4.在路由器设置 hosts 或修改本地 hosts

在 hosts 文件中添加的内容：`本机ip mb3admin.com` 

iOS、iPadOS 在未越狱状态下仅能通过路由器 hosts 或利用小火箭、圈 x 等工具解锁



## 5.在 emby 控制台随意输入激活码进行激活



可输入以下网址进行验证：

`https://mb3admin.com/admin/service/registration/validateDevice`

返回以下信息即成功

`{"cacheExpirationDays": 365,"message": "Device Valid","resultCode": "GOOD"}`


