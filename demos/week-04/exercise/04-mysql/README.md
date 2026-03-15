# 练习 4：MySQL 与数据卷

## 任务

运行 MySQL 容器，使用数据卷持久化数据。

## 要求

1. 运行 MySQL 8.0 容器
2. 设置 root 密码
3. 映射 3306 端口
4. 使用数据卷存储数据
5. 进入 MySQL，创建数据库和表
6. 停止并删除容器（但保留数据卷）
7. 重新运行容器，验证数据仍然存在

## 提示

```bash
# 运行 MySQL
docker run -d \
  --name my-mysql \
  -e MYSQL_ROOT_PASSWORD=123456 \
  -p 3306:3306 \
  -v mysql-data:/var/lib/mysql \
  mysql:8.0

# 等待启动，查看日志
docker logs my-mysql

# 进入 MySQL
docker exec -it my-mysql mysql -uroot -p123456

# 在 MySQL 中
CREATE DATABASE testdb;
USE testdb;
CREATE TABLE users (id INT, name VARCHAR(20));
INSERT INTO users VALUES (1, 'Test');
SELECT * FROM users;
EXIT;

# 停止删除容器（保留数据卷）
docker stop my-mysql
docker rm my-mysql

# 重新运行，验证数据
docker run -d \
  --name my-mysql2 \
  -e MYSQL_ROOT_PASSWORD=123456 \
  -p 3307:3306 \
  -v mysql-data:/var/lib/mysql \
  mysql:8.0

# 再次进入查询，数据应该还在！
```
