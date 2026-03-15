# 第4-7周讲义：Docker 容器技术

---

## 一、Docker 简介

### 1.1 什么是 Docker？
Docker 是一个开源的容器化平台，可以将应用程序及其依赖打包到一个轻量级、可移植的容器中。

### 1.2 为什么使用 Docker？
- **一致性**：开发、测试、生产环境一致
- **轻量级**：容器共享内核，启动快速
- **隔离性**：应用之间相互隔离，互不影响
- **可移植**：一次构建，随处运行

### 1.3 核心概念
- **镜像（Image）**：应用程序的静态模板
- **容器（Container）**：镜像的运行实例
- **仓库（Registry）**：存储镜像的地方

---

## 二、Docker 安装

### 2.1 Windows 安装
1. 下载 Docker Desktop：https://www.docker.com/products/docker-desktop
2. 运行安装程序
3. 重启电脑
4. 启动 Docker Desktop

### 2.2 验证安装
```bash
docker --version
docker run hello-world
```

### 2.3 配置镜像源
在 Docker Desktop 设置中添加国内镜像源：
```json
{
  "registry-mirrors": [
    "https://docker.mirrors.ustc.edu.cn",
    "https://hub-mirror.c.163.com"
  ]
}
```

---

## 三、镜像管理

### 3.1 搜索镜像
```bash
docker search ubuntu
docker search mysql
```

### 3.2 拉取镜像
```bash
docker pull ubuntu:20.04
docker pull mysql:8.0
docker pull python:3.9
```

### 3.3 查看镜像
```bash
docker images
docker image ls
```

### 3.4 删除镜像
```bash
docker rmi ubuntu:20.04
docker image rm ubuntu:20.04
```

---

## 四、容器操作

### 4.1 运行容器
```bash
# 基本运行
docker run ubuntu:20.04

# 交互式运行
docker run -it ubuntu:20.04 /bin/bash

# 后台运行
docker run -d ubuntu:20.04 sleep 1000

# 端口映射
docker run -d -p 8080:80 nginx

# 数据卷挂载
docker run -d -v mydata:/data ubuntu:20.04
```

### 4.2 查看容器
```bash
# 查看运行中的容器
docker ps

# 查看所有容器
docker ps -a
```

### 4.3 容器生命周期
```bash
# 启动容器
docker start <container_id>

# 停止容器
docker stop <container_id>

# 重启容器
docker restart <container_id>

# 删除容器
docker rm <container_id>

# 强制删除运行中的容器
docker rm -f <container_id>
```

### 4.4 进入容器
```bash
# 进入运行中的容器
docker exec -it <container_id> /bin/bash

# 查看容器日志
docker logs <container_id>

# 查看容器详情
docker inspect <container_id>
```

---

## 五、数据管理

### 5.1 数据卷
```bash
# 创建数据卷
docker volume create mydata

# 查看数据卷
docker volume ls

# 使用数据卷
docker run -d -v mydata:/data ubuntu:20.04
```

### 5.2 绑定挂载
```bash
# 绑定主机目录到容器
docker run -d -v /host/path:/container/path ubuntu:20.04
```

### 5.3 端口映射
```bash
# 映射主机端口到容器端口
docker run -d -p 8080:80 nginx

# 查看端口映射
docker port <container_id>
```

---

## 六、实战：运行常用服务

### 6.1 MySQL
```bash
# 运行 MySQL 容器
docker run -d \
  --name mysql \
  -e MYSQL_ROOT_PASSWORD=123456 \
  -p 3306:3306 \
  -v mysql-data:/var/lib/mysql \
  mysql:8.0

# 进入 MySQL
docker exec -it mysql mysql -uroot -p
```

### 6.2 Python
```bash
# 运行 Python 容器
docker run -it --name python -v $(pwd):/app python:3.9 /bin/bash

# 在容器中运行 Python 脚本
docker run --rm -v $(pwd):/app python:3.9 python /app/script.py
```

### 6.3 Nginx
```bash
# 运行 Nginx 容器
docker run -d \
  --name nginx \
  -p 80:80 \
  -v ./html:/usr/share/nginx/html \
  nginx:latest
```

---

## 七、Dockerfile 基础

### 7.1 简单的 Dockerfile
```dockerfile
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3
COPY . /app
WORKDIR /app
CMD ["python3", "app.py"]
```

### 7.2 构建镜像
```bash
docker build -t myapp:1.0 .
```

---

## 八、课后练习

1. 安装 Docker Desktop并运行 hello-world
2. 拉取 Ubuntu、MySQL、Python 镜像
3. 运行 Ubuntu 容器并在其中安装软件
4. 运行 MySQL 容器并连接
5. 运行 Nginx 容器并访问

---

## 九、拓展阅读
- [Docker 官方文档](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker 入门教程](https://docs.docker.com/get-started/)
