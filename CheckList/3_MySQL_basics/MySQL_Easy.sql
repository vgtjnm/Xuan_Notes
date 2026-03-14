#01
-- USE sql_store;
-- SELECT 
-- 	first_name,
--     last_name,
--     city
-- FROM customers
-- WHERE state = 'VA';

#02
-- USE sql_store;
-- SELECT *
-- FROM products
-- ORDER BY unit_price DESC
-- LIMIT 5;

#03
-- USE sql_store ;
-- SELECT
-- 	DISTINCT customer_id
-- FROM orders
-- ORDER BY customer_id;

#04
-- USE sql_store;
-- SELECT 
-- 	name,
--     unit_price
-- FROM products
-- WHERE unit_price BETWEEN 1 AND 5
-- 	AND quantity_in_stock > 20;

#05
-- USE sql_store;
-- SELECT 
-- 	CONCAT (first_name, '_', last_name) AS fullname,
--     phone
-- FROM customers
-- WHERE first_name REGEXP '^b';

#06
-- USE sql_store;
-- SELECT 
-- 	customer_id AS id,
--     first_name
-- FROM customers
-- WHERE phone IS NULL;

#MySQL 中常用的聚合函数如下：
-- | 函数 | 说明 | 示例 |
-- |------|------|------|
-- | `COUNT()` | 计算行数 | `COUNT(*)`、`COUNT(column)` |
-- | `SUM()` | 求总和 | `SUM(price)` |
-- | `AVG()` | 求平均值 | `AVG(score)` |
-- | `MAX()` | 求最大值 | `MAX(salary)` |
-- | `MIN()` | 求最小值 | `MIN(age)` |

#07
-- USE sql_store;
-- SELECT
-- 	COUNT(order_id) AS all_order,
-- 	MIN(order_date) AS zuizao,
--     MAX(order_date) AS zuiwan
-- FROM orders;

-- #08
-- USE sql_store;
-- SELECT 
-- 	name,
--     unit_price AS '单价',
--     unit_price * 1.1 AS '含税价'
-- FROM products;