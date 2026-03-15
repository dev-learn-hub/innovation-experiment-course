# Docker 演示示例

本目录包含 Docker 课程的完整演示代码。

## 示例列表

| 示例 | 名称 | 说明 |
|------|------|------|
| 01 | Hello World | 验证 Docker 安装 |
| 02 | Ubuntu | 基础容器操作 |
| 03 | Nginx | Web 服务器 + 端口映射 |
| 04 | MySQL | 数据库 + 数据卷 |
| 05 | Python | Python 环境 + 脚本运行 |
| 06 | Dockerfile | 自定义镜像构建 |

## 前置检查

在运行示例前，请确保：

```bash
# 检查 Docker 版本
docker --version

# 验证 Docker 运行
docker info
```

## 快速开始

进入每个示例目录，按照 README.md 中的步骤操作即可。

## 常用命令速查

```bash
# 镜像操作
docker images              # 查看镜像
docker pull <image>       # 拉取镜像
docker rmi <image>        # 删除镜像

# 容器操作
docker ps                  # 查看运行中的容器
docker ps -a               # 查看所有容器
docker run <image>         # 运行容器
docker start <container>   # 启动容器
docker stop <container>    # 停止容器
docker rm <container>      # 删除容器
docker exec -it <container> /bin/bash  # 进入容器

# 数据卷
docker volume ls           # 查看数据卷
docker volume create <name>  # 创建数据卷
docker volume rm <name>    # 删除数据卷
```

## 注意事项

1. **Windows PowerShell**：使用 `${PWD}` 表示当前目录
2. **Windows CMD**：使用 `%cd%` 表示当前目录
3. **Linux/Mac**：使用 `$(pwd)` 表示当前目录
4. **端口占用**：如果 8080 或 3306 被占用，修改映射端口
