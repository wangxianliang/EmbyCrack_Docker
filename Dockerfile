# 使用官方Python镜像作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到工作目录
COPY . /app

# 如果有依赖项，可以使用pip安装
RUN pip install --no-cache-dir -r requirements.txt

# 当容器启动时运行的命令
CMD ["python", "main.py"]
    