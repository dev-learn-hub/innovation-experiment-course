# 练习 5：Python 脚本运行

## 任务

1. 修改 `app.py`，把名字改成你的
2. 使用 Docker 运行这个 Python 脚本
3. 观察输出结果

## 要求

1. 编辑 `app.py`，修改名字
2. 用 Docker 运行 Python 3.9 容器
3. 挂载当前目录，执行脚本
4. 截图输出结果

## 提示

```bash
# 修改 app.py
# 把 name = "Your Name" 改成你的名字

# 运行脚本
docker run --rm -v ${PWD}:/app python:3.9 python /app/app.py
```
