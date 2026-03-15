# 示例 4：MySQL 数据库

## 运行步骤

```bash
# 运行 MySQL 容器
docker run -d \
  --name mysql-demo \
  -e MYSQL_ROOT_PASSWORD=123456 \
  -p 3306:3306 \
  -v mysql-data:/var/lib/mysql \
  mysql:8.0

# 等待 MySQL 启动（约 10-20 秒）
docker logs mysql-demo

# 进入 MySQL
docker exec -it mysql-demo mysql -uroot -p123456
```

## 在 MySQL 中执行

```sql
-- 创建数据库
CREATE DATABASE testdb;

-- 使用数据库
USE testdb;

-- 创建表
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
);

-- 插入数据
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com');

-- 查询数据
SELECT * FROM users;

-- 退出
EXIT;
```

## 清理

```bash
# 停止容器
docker stop mysql-demo

# 删除容器
docker rm mysql-demo

# 删除数据卷（可选）
docker volume rm mysql-data
```
