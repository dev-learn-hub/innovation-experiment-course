# 练习 2：Ubuntu 容器基础操作

## 任务

1. 运行一个 Ubuntu 容器
2. 在容器中执行一些基本命令
3. 理解容器的生命周期

## 要求

1. 交互式运行 Ubuntu 20.04 容器
2. 在容器中执行：`ls`、`pwd`、`echo "Hello"`
3. 退出容器，查看容器状态
4. 再次启动容器，进入容器
5. 最后停止并删除容器

## 提示

```bash
# 交互式运行
docker run -it ubuntu:20.04 /bin/bash

# 查看所有容器
docker ps -a

# 启动容器
docker start <container_id>

# 进入容器
docker exec -it <container_id> /bin/bash

# 停止和删除
docker stop <container_id>
docker rm <container_id>
```
