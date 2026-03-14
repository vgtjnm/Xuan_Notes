#之前我们接触过INNER JOIN和OUTER JOIN
#下面我们要来具体学习一下

#以后要记得用USE
-- USE sql_store;

-- SELECT 
-- 	c.customer_id AS cd,
--     c.first_name,
--     o.order_id
-- FROM customers c

-- #下面我们来学习LEFT JOIN 和 RIGHT JOIN
-- #区别就是LEFT保左表，RIGHT保右表，简单来说：
-- #LEFT JOIN左边的全要，右边没有填空，RIGHT JOIN则相反，直接JOIN就是两边都有才要
-- #重点FROM决定左表，JOIN决定右表，不是ON决定
-- #实际开发中LEFT JOIN最常用，RIGHT JOIN 几乎可以用 LEFT JOIN 改写替代。

-- -- LEFT JOIN orders o

-- -- RIGHT JOIN orders o

-- -- 	ON c.customer_id = o.customer_id
--     
-- ORDER BY c.customer_id

-- USE sql_store;

-- SELECT
-- 	p.product_id,
--     p.name,
--     oi.quantity
-- FROM products p
-- LEFT JOIN order_items oi
-- 	ON p.product_id = oi.product_id;

#下面来教一下JOIN的嵌套，有点烧脑但是有个小秘诀：
#一次只看一个 JOIN，把前面的结果当成一张新表，再跟下一张表连。

-- USE sql_store;

-- SELECT
-- 	c.customer_id,
--     c.first_name,
--     o.order_id,
--     sh.name AS shipper
-- FROM customers c
-- LEFT JOIN orders o
-- 	ON c.customer_id = o.customer_id
-- #注意一个重点，下面这个JOIN的左表是c+o
-- #我们通过LEFT JOIN orders 保留下来的用户被这个JOIN过滤了
-- #所以要改成LEFT JOIN
-- LEFT JOIN shippers sh
-- #mosh在这里说了一个工程习惯，如果你在一次连接中同时RIGHT + LEFT
-- #你的代码就很难判断，最好的办法就是避免RIGHT而是用LEFT
-- 	ON o.shipper_id = sh.shipper_id
-- ORDER BY c.customer_id;

-- USE sql_store;

-- SELECT
-- 	o.order_date,
--     o.order_id,
--     c.first_name AS customer,
--     sh.name,
-- #这里mosh连了另一个表，而我使用IF来完成，也不是我想用的，我以为没这个表
--     IF (sh.name is NULL, 'Processed', 'Shipped') AS status
-- FROM orders o
-- LEFT JOIN customers c
-- 	ON o.customer_id = c.customer_id
-- LEFT JOIN shippers sh
-- 	ON o.shipper_id = sh.shipper_id
-- ORDER BY status;

#之前的老问题经理不存在可以解决了

USE sql_hr;

SELECT 
	e.employee_id,
    e.first_name,
    m.first_name
FROM employees e
LEFT JOIN employees m
	ON e.reports_to = m.employee_id
ORDER BY m.first_name;