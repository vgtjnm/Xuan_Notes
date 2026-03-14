#17
-- USE sql_store;
-- SELECT 
-- 	c.last_name,
--     oi.quantity * oi.unit_price AS total
-- FROM customers c
-- LEFT JOIN orders o
-- 	USING (customer_id)
-- LEFT JOIN order_items oi
-- 	USING (order_id)
-- LIMIT 3;

#18
-- USE sql_store;
-- SELECT
-- 	p.name,
--     p.unit_price,
--     CASE
-- 		WHEN unit_price < 2 THEN 'Cheap'
--         WHEN unit_price <=5 THEN 'Average'
--         WHEN unit_price >5 THEN 'Expensive'
--         END AS Label
-- FROM products p;

#SQL执行顺序
-- FROM
-- WHERE
-- GROUP BY
-- HAVING
-- SELECT
-- ORDER BY

#SQL正确结构
-- SELECT
-- FROM
-- JOIN
-- WHERE
-- GROUP BY
-- HAVING
-- ORDER BY

#19
-- USE sql_store;
-- SELECT
-- 	CONCAT(c.first_name, ' ', c.last_name) AS fullname,
--     c.city
-- FROM customers c
-- LEFT JOIN customers b
-- 	USING (city)
-- WHERE CONCAT(c.first_name, ' ', c.last_name) != 'Babara MacCaffrey' AND
-- CONCAT(b.first_name, ' ', b.last_name) REGEXP 'Babara MacCaffrey'

#EXISTS 用于检查子查询是否返回至少一行数据，返回布尔值（TRUE/FALSE）
-- 基本语法
-- SELECT * FROM table1
-- WHERE EXISTS (
--     SELECT 1 FROM table2
--     WHERE 条件
-- );

#20
-- USE sql_store;
-- SELECT 
-- 	CONCAT(c.first_name,' ',c.last_name) AS fullname
-- FROM customers c
-- JOIN orders o USING(customer_id)
-- WHERE EXISTS (
-- 	SELECT 1 FROM order_items oi
-- 	WHERE oi.order_id = o.order_id AND
--     oi.quantity * unit_price > 90
-- );

#视图（View）:
#视图是一个虚拟表，它本身不存储数据，而是基于一条 SQL 查询语句定义的。
#每次访问视图时，数据库会动态执行该查询并返回结果。

#示例
-- CREATE VIEW active_users AS
-- SELECT id, name, email
-- FROM users
-- WHERE status = 'active';

#之后就可以像查询普通表一样使用它：
-- SELECT * FROM active_users;

#CREATE OR REPLACE VIEW保证重复执行不报错

#21
-- USE sql_store;
-- CREATE OR REPLACE VIEW vw_customer_orders AS 
-- SELECT 
-- 	c.customer_id,
--     CONCAT(first_name, ' ', last_name) AS fullname,
--     COUNT(order_id) AS order_num,
--     SUM(oi.unit_price*oi.quantity) AS total
-- FROM customers c
-- LEFT JOIN orders o
-- 	USING (customer_id)
-- LEFT JOIN order_items oi
-- 	USING (order_id)
-- GROUP BY customer_id, first_name, last_name;

-- SELECT * FROM vw_customer_orders
-- ORDER BY total DESC
-- LIMIT 1;

#存储过程（Stored Procedure）就是保存在数据库里的一段可复用的 SQL 代码，
#你给它起个名字，之后随时可以用 CALL 来执行它。

-- 它能做什么？
-- 接收参数（比如传入一个 customer_id）
-- 执行一段或多段 SQL 逻辑
-- 返回结果集

-- 基本语法长这样：

-- DELIMITER //

-- CREATE PROCEDURE 过程名(参数名 数据类型)
-- BEGIN
--     -- 你的 SQL 逻辑写在这里
--     SELECT * FROM orders WHERE customer_id = 参数名;
-- END //

-- DELIMITER ;

-- 调用时：
-- CALL 过程名(1);

#22

-- USE sql_store;
-- DROP PROCEDURE IF EXISTS get_customer_orders;#这一行保证重复运行不报错

-- DELIMITER //
-- CREATE PROCEDURE get_customer_orders(p_customer_id integer)
-- BEGIN
-- 	SELECT 
-- 		p.name,
--         oi.quantity,
--         oi.quantity * oi.unit_price AS total
--     FROM orders o
-- 	JOIN order_items oi USING (order_id)
-- 	JOIN products p USING (product_id)
-- 	WHERE o.customer_id = p_customer_id;
-- END //

-- DELIMITER ;#DELIMITER后面要有空格

-- CALL get_customer_orders(1)

#事务是什么？
-- 就是把多条 SQL 捆绑成"要么全成功，要么全失败"的一个整体。
-- 比如银行转账：A 扣钱 + B 收钱，必须同时成功，不能只执行一半。

#语法就三个关键词：
-- START TRANSACTION;   -- 开始事务

--     -- 你的 SQL 操作写在这里
--     INSERT INTO ...
--     UPDATE ...

-- COMMIT;              -- 全部成功 → 提交保存
-- -- 或者
-- ROLLBACK;            -- 出错了 → 撤销回滚

#23

-- USE sql_store;
-- START TRANSACTION;

-- INSERT INTO orders
-- 		(customer_id,
--         order_date,
--         status)
-- VALUES 
-- 	(2,
--     '2025-3-15',
--     1);
--     
-- INSERT INTO order_items
-- VALUES 
-- 	(LAST_INSERT_ID(),
--     1,
--     5,
--     4.15
--     );

-- UPDATE products
-- SET quantity_in_stock = quantity_in_stock - 5
-- WHERE product_id = 1;

-- COMMIT;              -- 全部成功 → 提交保存
-- ROLLBACK;            -- 出错了 → 撤销回滚	

#COMMIT 和 ROLLBACK 不能同时写
#COMMIT 执行后事务已结束，后面的 ROLLBACK 没有意义。
#实际项目中是在程序逻辑里二选一，但作业里通常这样处理

#24
-- SELECT 
-- 	c.customer_id,
--     c.first_name,
--     c.last_name,
-- 	COUNT(DISTINCT order_id) AS total_order,
--     SUM(oi.quantity * oi.unit_price) AS total_spend,
--     SUM(oi.quantity * oi.unit_price) / COUNT(order_id) AS order_avg,
--     DATEDIFF(CURDATE(),
-- 		(SELECT order_date
-- 		FROM orders
--         WHERE customer_id = c.customer_id
--         ORDER BY order_date DESC
--         LIMIT 1)
--         ) AS time_has_passed
-- FROM customers c
-- LEFT JOIN orders o
-- 	USING (customer_id)
-- LEFT JOIN order_items oi
-- 	USING (order_id)
-- GROUP BY customer_id
-- ORDER BY total_spend DESC;