import hashlib

def write_conf(key):
    conf_str = f"""
server {{
    listen 443 ssl;
    listen [::]:443 ssl;  
    server_name mb3admin.com;
    ssl_certificate emby/mb3admin.com.cert.pem;
    ssl_certificate_key emby/mb3admin.com.key.pem;
    ssl_session_timeout 5m;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
    ssl_prefer_server_ciphers on;
    location = /webdefault/images/logo.jpg {{
        alias /usr/syno/share/nginx/logo.jpg;
    }}
    location @error_page {{
        root /usr/syno/share/nginx;
        rewrite (.*) /error.html break;
    }}
    location ^~ /.well-known/acme-challenge {{
        root /var/lib/letsencrypt;
        default_type text/plain;
    }}
    location / {{
        rewrite ^ / redirect;
    }}
    location ~ ^/$ {{
        rewrite / https://$host:5001/ redirect;
    }}
    add_header Access-Control-Allow-Origin *;
    add_header Access-Control-Allow-Headers *;
    add_header Access-Control-Allow-Method *;
    add_header Access-Control-Allow-Credentials true;
    location /admin/service/registration/validateDevice {{
        default_type application/json;
        return 200 '{{"cacheExpirationDays": 365,"message": "Device Valid","resultCode": "GOOD"}}';
    }}
    location /admin/service/registration/getStatus {{
        default_type application/json;
        return 200 '{{"deviceStatus":"0","planType":"Lifetime","subscriptions":{{}}}}';
    }}
    location /admin/service/registration/validate {{
        default_type application/json;
        return 200 '{{"featId":"","registered":true,"expDate":"2099-01-01","key":"{key}"}}';
    }}
}}
    """
    with open("config/emby.conf", "w") as f:
        f.write(conf_str)

def calculate_md5(input_string):
    # 创建一个 MD5 hash 对象
    md5_hash = hashlib.md5()
    # 对输入字符串进行编码
    input_bytes = input_string.encode('utf-8')
    # 更新 hash 对象的内容
    md5_hash.update(input_bytes)
    # 获取十六进制表示的 hash 值
    return md5_hash.hexdigest()

if __name__ == "__main__":
    input_string = input("请输ServerID: ")
    md5 = f'MBSupporter{input_string}Ae3#fP!wi'
    # 计算 MD5 hash
    md5_result = calculate_md5(md5)
    print(f"key计算结果: {md5_result}")
    # 生成conf文件
    write_conf(md5_result)
    print("""已更新emby.conf文件,请运行"docker-compose up -d"启动容器""")
    # 提示用户按任意键退出
    input("按任意键退出...")