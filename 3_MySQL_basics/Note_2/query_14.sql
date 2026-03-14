-- #在SQL中我们还可以将来自多个表的行合并在一起

-- USE sql_store;

-- SELECT 
-- 	order_id,
--     order_date,
--     'Active' AS status
-- FROM orders
-- #如果我们想获取今年的查询那么我们可能会这么写
-- WHERE order_date >= '2019-01-01'
-- #问题是到了明年我们就要手动更新
-- #所以我们需要创建一个列叫它Active

-- #我们可以使用UNION来合并两个SELECT表
-- #使用UNION可以合并多个计算的结果，这些查询可以针对同一张表，也可以针对不同的表

-- UNION

-- SELECT 
-- 	order_id,
--     order_date,
--     'Archived' AS status
-- FROM orders
-- WHERE order_date < '2019-01-01'

-- #但是如果这样使用UNION就不行

-- SELECT first_name, last_name
-- FROM customers
-- UNION
-- SELECT name
-- FROM shippers

-- #因为上个表有两列，而下个表只有一列
-- #使用UNION合并的表，第一个表的列为名字，你也可以用as去改名字

-- SELECT first_name as fn
-- FROM customers
-- UNION
-- SELECT order_id
-- FROM orders



#我真的服了mosh还没教CASE就叫写这个练习

USE sql_store;

SELECT 
	c.customer_id,
    c.first_name,
    c.points,
#mosh不教的我来教！
#CASE其实很简单，先写个CASE
#然后WHEN写条件，THEN写触发，ELSE写否则（也可以不写ELSE）
#WHEN+THEN,ELSE不用加，多个条件直接叠 WHEN，不能用 ELSE WHEN
#SQL的CASE从上往下判断，所以顺序极其重要
#最后END AS创建新的列整个过程不用写逗号
    CASE
		WHEN points < 2000  THEN 'Bronze'
        WHEN points <= 3000 THEN 'Silver'
        ELSE 'Gold'
	END AS 'type'
FROM customers c;