FROM ubuntu:20.04

# 安装 Python
RUN apt-get update && apt-get install -y python3

# 设置工作目录
WORKDIR /app

# 复制脚本
COPY script.py .

# 启动命令
CMD ["python3", "script.py"]
