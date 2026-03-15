# 示例 2：Ubuntu 容器

## 运行步骤

```bash
# 交互式运行 Ubuntu 容器
docker run -it ubuntu:20.04 /bin/bash

# 在容器内执行命令
ls
pwd
echo "Hello from Ubuntu!"
exit
```

## 常用命令

```bash
# 查看运行中的容器
docker ps

# 查看所有容器
docker ps -a

# 启动已停止的容器
docker start <container_id>

# 进入运行中的容器
docker exec -it <container_id> /bin/bash

# 停止容器
docker stop <container_id>

# 删除容器
docker rm <container_id>
```
