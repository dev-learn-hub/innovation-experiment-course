# 第4-7周练习：Docker 容器技术

---

## 练习目标

1. 掌握 Docker 环境的安装和配置
2. 掌握 Docker 镜像和容器的基本操作
3. 能够使用 Docker 运行常用服务（Linux、MySQL、Python）
4. 理解数据持久化和端口映射
5. 能够编写简单的 Dockerfile

---

## 基础练习（必做）

### 练习一：Docker 环境搭建
**目标**：安装并验证 Docker 环境

**要求**：
1. 下载并安装 Docker Desktop
2. 启动 Docker Desktop
3. 运行 `docker --version` 验证安装
4. 运行 `docker run hello-world` 测试

**提示**：
```bash
# 验证安装
docker --version
docker info

# 运行测试镜像
docker run hello-world
```

**验收标准**：
- [ ] Docker Desktop 成功启动
- [ ] `docker --version` 输出版本信息
- [ ] `docker run hello-world` 成功运行并输出欢迎信息

---

### 练习二：镜像管理
**目标**：掌握镜像的搜索、拉取、查看、删除

**要求**：
1. 搜索 Ubuntu、MySQL、Python、Nginx 镜像
2. 拉取以下镜像：
   - ubuntu:20.04
   - mysql:8.0
   - python:3.9
   - nginx:latest
3. 查看本地镜像列表
4. 尝试删除一个镜像（可选）

**提示**：
```bash
# 搜索镜像
docker search ubuntu
docker search mysql

# 拉取镜像
docker pull ubuntu:20.04
docker pull mysql:8.0

# 查看镜像
docker images

# 删除镜像
docker rmi ubuntu:20.04
```

**验收标准**：
- [ ] 成功搜索到目标镜像
- [ ] 成功拉取指定的4个镜像
- [ ] 能正确查看本地镜像列表

---

### 练习三：容器基本操作
**目标**：掌握容器的创建、运行、停止、删除

**要求**：
1. 运行一个 Ubuntu 容器（交互式）
2. 在容器中执行命令（如 ls、pwd、echo）
3. 退出容器，查看容器状态
4. 启动已停止的容器
5. 停止和删除容器

**提示**：
```bash
# 交互式运行 Ubuntu
docker run -it ubuntu:20.04 /bin/bash

# 在容器中执行命令
ls
pwd
echo "Hello Docker"
exit

# 查看所有容器
docker ps -a

# 启动容器
docker start <container_id>

# 进入运行中的容器
docker exec -it <container_id> /bin/bash

# 停止容器
docker stop <container_id>

# 删除容器
docker rm <container_id>
```

**验收标准**：
- [ ] 能成功运行交互式 Ubuntu 容器
- [ ] 能在容器中执行基本命令
- [ ] 能正确启动、停止、删除容器
- [ ] 理解容器的生命周期

---

### 练习四：数据持久化
**目标**：掌握数据卷和绑定挂载的使用

**要求**：
1. 创建一个数据卷
2. 运行容器并挂载数据卷
3. 在容器中创建文件
4. 停止并删除容器
5. 重新运行容器并验证数据仍然存在
6. 尝试绑定挂载主机目录

**提示**：
```bash
# 创建数据卷
docker volume create mydata

# 查看数据卷
docker volume ls

# 运行容器并挂载数据卷
docker run -it -v mydata:/data ubuntu:20.04 /bin/bash

# 在容器中创建文件
cd /data
echo "Persist me" > test.txt
ls
exit

# 删除容器
docker rm <container_id>

# 重新运行容器验证数据
docker run -it -v mydata:/data ubuntu:20.04 /bin/bash
cat /data/test.txt

# 绑定挂载（Windows 示例）
docker run -it -v C:\Users\YourName\host-folder:/container-folder ubuntu:20.04 /bin/bash
```

**验收标准**：
- [ ] 能成功创建和使用数据卷
- [ ] 数据在容器删除后仍然保留
- [ ] 能使用绑定挂载访问主机文件

---

### 练习五：端口映射
**目标**：掌握端口映射的使用

**要求**：
1. 运行 Nginx 容器，映射主机 8080 端口到容器 80 端口
2. 在浏览器中访问 http://localhost:8080
3. 查看容器端口映射
4. 停止并删除容器

**提示**：
```bash
# 运行 Nginx 容器并映射端口
docker run -d --name nginx -p 8080:80 nginx:latest

# 查看容器状态
docker ps

# 查看端口映射
docker port nginx

# 在浏览器访问
# http://localhost:8080

# 查看日志
docker logs nginx

# 停止并删除
docker stop nginx
docker rm nginx
```

**验收标准**：
- [ ] 能成功运行 Nginx 容器
- [ ] 端口映射配置正确
- [ ] 能在浏览器中访问 Nginx 默认页面

---

## 进阶练习（选做）

### 练习六：运行 MySQL 容器
**目标**：使用 Docker 运行 MySQL 数据库

**要求**：
1. 运行 MySQL 8.0 容器
2. 设置 root 密码
3. 映射 3306 端口
4. 使用数据卷持久化数据
5. 进入容器连接 MySQL
6. 创建数据库和表

**提示**：
```bash
# 运行 MySQL 容器
docker run -d \
  --name mysql \
  -e MYSQL_ROOT_PASSWORD=123456 \
  -p 3306:3306 \
  -v mysql-data:/var/lib/mysql \
  mysql:8.0

# 查看日志等待启动
docker logs mysql

# 进入 MySQL
docker exec -it mysql mysql -uroot -p123456

# 在 MySQL 中执行
CREATE DATABASE testdb;
USE testdb;
CREATE TABLE users (id INT, name VARCHAR(20));
INSERT INTO users VALUES (1, 'Alice');
SELECT * FROM users;
EXIT;
```

**验收标准**：
- [ ] MySQL 容器成功启动
- [ ] 能连接到 MySQL
- [ ] 能创建数据库和表
- [ - ] 数据持久化配置正确

---

### 练习七：运行 Python 环境
**目标**：使用 Docker 运行 Python 程序

**要求**：
1. 在主机上创建一个简单的 Python 脚本
2. 运行 Python 3.9 容器
3. 挂载主机目录到容器
4. 在容器中运行 Python 脚本
5. 尝试使用 Dockerfile 构建自定义镜像

**提示**：
```python
# app.py
print("Hello from Docker!")

for i in range(5):
    print(f"Count: {i}")
```

```bash
# 运行 Python 容器
docker run -it --rm -v $(pwd):/app python:3.9 /bin/bash

# 在容器中运行脚本
cd /app
python app.py

# 或者直接运行
docker run --rm -v $(pwd):/app python:3.9 python /app/app.py
```

**Dockerfile 示例**：
```dockerfile
FROM python:3.9
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
```

```bash
# 构建镜像
docker build -t mypythonapp .

# 运行
docker run mypythonapp
```

**验收标准**：
- [ ] 能在容器中运行 Python 脚本
- [ ] 理解目录挂载的使用
- [ ] （选做）能编写简单的 Dockerfile

---

## 挑战练习（拔高）

### 练习八：多容器协作
**目标**：使用 Docker Compose 运行多容器应用

**要求**：
1. 创建一个简单的 Web 应用（Python + Flask）
2. 使用 MySQL 作为数据库
3. 编写 docker-compose.yml
4. 使用 Docker Compose 启动应用
5. 测试应用功能

**提示**：
```yaml
# docker-compose.yml
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: 123456
      MYSQL_DATABASE: flaskdb
    volumes:
      - db-data:/var/lib/mysql
volumes:
  db-data:
```

**验收标准**：
- [ ] 能编写 docker-compose.yml
- [ ] 多容器能正常启动并协作
- [ ] 应用功能完整可用

---

## 提交要求

1. 将所有练习的命令记录整理为一个 Markdown 文件
2. 包含关键步骤的截图（可选但推荐）
3. 记录遇到的问题和解决方案
4. 提交到指定位置

---

## 评分标准

| 项目 | 分值 | 说明 |
|------|------|------|
| 练习一-环境搭建 | 10% | Docker 安装和验证 |
| 练习二-镜像管理 | 15% | 镜像搜索、拉取、管理 |
| 练习三-容器操作 | 20% | 容器基本操作 |
| 练习四-数据持久化 | 15% | 数据卷和绑定挂载 |
| 练习五-端口映射 | 10% | 端口映射和服务访问 |
| 进阶练习 | 20% | MySQL 或 Python 完成一个 |
| 挑战练习 | 10% | Docker Compose 多容器应用 |
| 文档质量 | 额外+10% | 记录完整、清晰、有思考 |
