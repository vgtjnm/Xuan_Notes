-- USE sql_store;

-- SELECT *
-- FROM order_items oi
-- JOIN order_item_notes oin
-- #下面我们来学一下复合关节
-- 	ON oi.order_id = oin.order_id
-- #没错 ON 可以使用 AND 加条件
--     AND oi.product_id = oin.product_id
-- #然而并没有这样的项目，这不是你的错其实，是没有这样的数据

#还有就是MySQL中的隐式连接语法

-- Implpicit Join Syntax
-- SELECT *
-- FROM orders o, customers c
-- WHERE o.customer_id = c.customer_id
#这个代码，如果你去掉WHERE那么将会有100条记录
#因为每个o都会和c去连接，这就是我们说的交叉转身

