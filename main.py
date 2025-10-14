from flask import Flask, jsonify, make_response, request
import hashlib
from werkzeug.serving import WSGIRequestHandler

app = Flask(__name__)

# 配置服务器标识和HTTP协议版本
WSGIRequestHandler.server_version = "nginx/1.29.2"
WSGIRequestHandler.protocol_version = "HTTP/1.1"

# MD5计算函数
def calculate_md5(input_string):
    # 创建一个 MD5 hash 对象
    md5_hash = hashlib.md5()
    # 对输入字符串进行编码
    input_bytes = input_string.encode('utf-8')
    # 更新 hash 对象的内容
    md5_hash.update(input_bytes)
    # 获取十六进制表示的 hash 值
    return md5_hash.hexdigest()

# 打印POST请求参数
@app.before_request
def print_post_parameters():
    if request.method == 'POST':
        print("\n" + "="*60)
        print(f"[POST Request] Path: {request.path}")
        
        # 提取表单参数
        form_params = request.form.to_dict()
        if form_params:
            print(f"Form Parameters: {form_params}")
        
        # 其他参数类型处理
        url_params = request.args.to_dict()
        if url_params:
            print(f"URL Parameters: {url_params}")
        
        json_params = request.get_json(silent=True)
        if json_params:
            print(f"JSON Parameters: {json_params}")
        
        if request.data and not (form_params or json_params):
            print(f"Raw Body: {request.data.decode('utf-8')}")
        print("="*60 + "\n")

# 统一设置响应头
@app.after_request
def set_response_headers(response):

    response.headers['Server'] = 'nginx/1.29.2'
    response.headers['Connection'] = 'keep-alive'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Method'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    
    return response

# 路由定义
@app.route('/admin/service/registration/validateDevice', methods=['GET', 'POST'])
def validate_device():
    return make_response(jsonify({
        "cacheExpirationDays": 365,
        "message": "Device Valid",
        "resultCode": "GOOD"
    }))

@app.route('/admin/service/registration/getStatus', methods=['GET', 'POST'])
def get_status():
    return make_response(jsonify({
        "deviceStatus": "0",
        "planType": "Lifetime",
        "subscriptions": {}
    }))

# 重点处理的路由：提取systemid并生成MD5作为key
@app.route('/admin/service/registration/validate', methods=['GET', 'POST'])
def validate():
    # 初始化默认key
    md5_key = ""  # 默认值，防止没有systemid的情况
    
    # 仅处理POST请求中的表单参数
    if request.method == 'POST':
        # 获取表单参数中的systemid
        form_params = request.form.to_dict()
        system_id = form_params.get('systemid')
        
        if system_id:
            print(f"提取到的systemid: {system_id}")
            # 计算MD5
            md5_key = calculate_md5(f'MBSupporter{system_id}Ae3#fP!wi')
            print(f"生成的MD5值: {md5_key}")
    
    # 返回结果，使用计算后的MD5作为key
    return make_response(jsonify({
        "featId": "",
        "registered": True,
        "expDate": "2099-01-01",
        "key": md5_key  # 替换为MD5处理后的值
    }))

if __name__ == '__main__':
    ssl_context = ('mb3admin.com.cert.pem', 'mb3admin.com.key.pem')
    app.run(
        host='0.0.0.0',
        port=443,
        ssl_context=ssl_context,
        debug=False
    )
    