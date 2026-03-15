# 示例 6：Dockerfile 构建镜像

## 构建步骤

```bash
# 构建镜像
docker build -t my-custom-image .

# 查看镜像
docker images

# 运行容器
docker run --rm my-custom-image
```

## Dockerfile 常用指令

| 指令 | 作用 |
|------|------|
| `FROM` | 指定基础镜像 |
| `RUN` | 执行命令 |
| `COPY` | 复制文件 |
| `WORKDIR` | 设置工作目录 |
| `EXPOSE` | 暴露端口 |
| `ENV` | 设置环境变量 |
| `CMD` | 启动命令 |
