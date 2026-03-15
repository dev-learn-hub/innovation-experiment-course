# 练习 3：Nginx 与端口映射

## 任务

运行 Nginx 容器，配置端口映射，在浏览器中访问。

## 要求

1. 运行 Nginx 容器，映射主机端口 8080 到容器 80
2. 给容器起个名字
3. 在浏览器中访问 http://localhost:8080
4. 查看容器日志
5. 清理容器

## 提示

```bash
# 运行 Nginx
docker run -d --name my-nginx -p 8080:80 nginx:latest

# 查看状态
docker ps

# 查看日志
docker logs my-nginx

# 浏览器访问
# http://localhost:8080

# 清理
docker stop my-nginx
docker rm my-nginx
```
