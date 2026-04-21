# lucyGit
# 记录学习相关编程的信息资料


#部分git代码网址
1） https://github.com/xufive/ways2grow
2） https://github.com/bainingchao/PyDataPreprocessing

163邮箱的授权码：QGwTGKJUNgbdFKGR

#  ---------------mysql----------
abc123
1)验证安装
管理员权限启动CMD
net start mysql     # 启动服务  
mysql -u root -p    # 输入密码登录
SELECT VERSION();   # 显示版本号即成功

net start mysql57     # 启动服务 
net stop mysql57     # 停止服务 

C:\Windows\system32>net start mysql57
MySQL57 服务正在启动 .
MySQL57 服务已经启动成功。

常见问题： 服务启动失败：检查 my.ini  配置文件路径或端口占用。 密码遗忘：通过 --skip-grant-tables 模式重置。


3.4 用户权限管理
-- 创建用户并授权 
CREATE USER 'admin'@'%' IDENTIFIED BY 'Admin123!';
GRANT ALL PRIVILEGES ON shop.* TO 'admin'@'%';
FLUSH PRIVILEGES;  -- 刷新权限

4. 进阶操作推荐
4.1 备份与恢复

AI代码解释
mysqldump -u root -p shop > shop_backup.sql   # 备份 
mysql -u root -p shop < shop_backup.sql       # 恢复 


   

3. MySQL基础操作教程
3.1 数据库管理
CREATE DATABASE shop;    -- 创建数据库
USE shop;                 -- 切换数据库 
SHOW DATABASES;          -- 查看所有数据库 
DROP DATABASE test;      -- 删除数据库

3.2 数据表操作
-- 创建表（含主键、自增、非空约束）
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE
);
 
-- 修改表结构 
ALTER TABLE users ADD age INT;     -- 新增字段 
ALTER TABLE users DROP COLUMN age; -- 删除字段 

3.3 数据增删改查（CRUD）
-- 插入数据
INSERT INTO users (name, email) VALUES ('张三', 'zhangsan@example.com'); 
 
-- 查询数据 
SELECT * FROM users WHERE name LIKE '张%';  -- 模糊查询
 
-- 更新数据 
UPDATE users SET email='new@example.com'  WHERE id=1;
 
-- 删除数据
DELETE FROM users WHERE id=2;

   
