# 第4-7周：Docker 容器技术 - 详情页

---

## 📅 时间安排

| 周次 | 内容 | 地点 |
|------|------|------|
| 第4周 | Docker 基础 + 环境搭建 | 机房 |
| 第5周 | 镜像与容器操作 | 机房 |
| 第6周 | 数据持久化与网络 | 机房 |
| 第7周 | 实战应用 + Dockerfile | 机房 |

---

## 🎯 学习路径

```
环境搭建 → 镜像管理 → 容器操作 → 数据持久化 → 端口映射 → 实战应用
```

---

## 📚 资源导航

### 讲义
- [week-04-lecture.md](./week-04-lecture.md) - 详细讲义

### 练习
- [week-04-exercise.md](./week-04-exercise.md) - 练习题目

### 演示代码
- [demos/week-04/demo/](./demos/week-04/demo/) - 完整演示代码
- [demos/week-04/exercise/](./demos/week-04/exercise/) - 练习模板代码

---

## 🛠️ 工具准备

### 必需软件
- Docker Desktop（Windows/Mac）或 Docker Engine（Linux）
- 终端/命令行工具

### 参考资料
- [Docker 官方文档](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker 入门教程](https://docs.docker.com/get-started/)

---

## 💡 学习贴士

1. **先跑起来**：先运行 hello-world，建立信心
2. **理解概念**：镜像 vs 容器，这是核心
3. **多动手练**：Docker 是做会的，不是看会的
4. **善用 --help**：docker --help，docker run --help
5. **记录常用命令**：建个小抄，随时查阅

---

## ❓ 常见问题

### Q: Docker Desktop 启动报错？
A: 检查 BIOS 中虚拟化是否开启，Windows 需开启 Hyper-V/WSL2。

### Q: 拉取镜像特别慢？
A: 配置国内镜像源（中科大、网易等）。

### Q: 容器退出后数据没了？
A: 使用数据卷（-v）或绑定挂载来持久化数据。

### Q: 端口映射不生效？
A: 检查主机端口是否被占用，或者容器内服务是否监听 0.0.0.0。

---

## 📬 答疑与交流

- 课堂提问
- 课后讨论
- Docker 官方文档查阅

---

**开始你的容器化之旅吧！🐳**
