#GROUP BY 用于将查询结果按一个或多个列分组，通常配合聚合函数使用
-- 基本语法：
-- SELECT 列名, 聚合函数(列名)
-- FROM 表名
-- GROUP BY 列名;

#09
-- USE sql_store;
-- SELECT 
-- 	customer_id,
--     COUNT(customer_id) as orders
-- FROM orders
-- GROUP BY customer_id
-- ORDER BY orders DESC;

#10
-- USE sql_store;
-- SELECT 
-- 	o.order_id,
--     o.order_date,
-- 	c.first_name,
-- 	c.last_name
-- FROM orders o
-- JOIN customers c
--  	USING (customer_id);

#11
-- USE sql_store;
-- SELECT 
-- 	p.name,
--     oi.quantity,
--     p.unit_price,
--     o.order_date
-- FROM order_items oi
-- JOIN products p
-- 	USING (product_id)
-- JOIN orders o
-- 	USING (order_id);

#12
-- USE sql_store;
-- SELECT
-- 	c.customer_id AS id,
-- 	CONCAT(c.first_name, '_', c.last_name) AS fullname,
--     COUNT(o.order_id) AS orders
-- FROM customers c
-- LEFT JOIN orders o
-- 	USING (customer_id)
-- GROUP BY customer_id;

#13
-- USE sql_store;
-- SELECT 
-- 	name,
--     unit_price
-- FROM products
-- WHERE unit_price > 
-- 	(SELECT AVG(unit_price)
--     FROM products);

#14
-- USE sql_store;
-- SELECT 
-- 	CONCAT(c.first_name, '_', last_name) AS fullname
-- FROM customers c
-- WHERE customer_id IN ( #记得用IN
-- 	SELECT o.customer_id
--     FROM orders o
--     WHERE order_id IN ( #记得用IN
-- 		SELECT oi.order_id
--         FROM order_items oi
--         WHERE product_id = 3
--         )
-- 	)

#使用 UPPER() 函数可以转换大写

#15
-- USE sql_store;
-- SELECT 
-- 	CONCAT (
-- 		UPPER(last_name),
--         ', ',
-- 		UPPER(first_name)
--         ) AS fullname
-- FROM customers;

#MySQL中的日期函数：
-- 当前日期和时间
-- SELECT NOW();           -- 2024-01-15 14:30:25
-- SELECT CURRENT_TIMESTAMP(); -- 同上

-- -- 当前日期
-- SELECT CURDATE();       -- 2024-01-15
-- SELECT CURRENT_DATE();  -- 同上

-- -- 当前时间
-- SELECT CURTIME();       -- 14:30:25
-- SELECT CURRENT_TIME();  -- 同上

-- 计算两个日期相差的天数
-- SELECT DATEDIFF('2024-01-20', '2024-01-15');       -- 5

#16
-- USE sql_store;
-- SELECT 
-- 	order_id,
--     order_date,
--     DATEDIFF(CURDATE(),order_date) AS time_has_passed
-- FROM orders
-- WHERE YEAR(order_date) = 2019