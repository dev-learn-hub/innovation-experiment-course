# 示例 5：Python 环境

## 方式一：直接运行脚本

```bash
# 运行 Python 容器并执行脚本
docker run --rm -v ${PWD}:/app python:3.9 python /app/app.py
```

注意：Windows PowerShell 使用 `${PWD}`，CMD 使用 `%cd%`

## 方式二：交互式开发

```bash
# 交互式运行 Python 容器
docker run -it --rm -v ${PWD}:/app python:3.9 /bin/bash

# 在容器内
cd /app
python app.py
python
```

## 方式三：使用 Dockerfile

创建 `Dockerfile`：

```dockerfile
FROM python:3.9
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
```

构建并运行：

```bash
# 构建镜像
docker build -t my-python-app .

# 运行容器
docker run --rm my-python-app
```
