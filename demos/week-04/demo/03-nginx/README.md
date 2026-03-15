# 示例 3：Nginx Web 服务器

## 运行步骤

```bash
# 运行 Nginx 容器，映射端口 8080:80
docker run -d --name nginx-demo -p 8080:80 nginx:latest

# 查看容器状态
docker ps

# 查看日志
docker logs nginx-demo
```

## 访问网站

在浏览器中打开：http://localhost:8080

## 清理

```bash
# 停止容器
docker stop nginx-demo

# 删除容器
docker rm nginx-demo
```
