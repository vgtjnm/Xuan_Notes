#终于要学习update了，准备凑齐crud!

-- #更新的方法很简单，直接UPDATE指定表
-- UPDATE invoices
-- #然后SET选择列和修改
-- SET payment_total = 10, payment_date = '2019-03-01'
-- #使用WHERE来确定修改人群
-- WHERE invoice_id = 1
-- #运行+刷新修改就成功了，刷新在左上角

#这里如果更新不了，需要去edit把底部的safe给取消掉然后重启就行

#更新多个列的方法也很简单

-- UPDATE invoices
-- SET 	
-- 	payment_total = invoice_total * 0.5,
-- 	payment_date = due_date
-- -- WHERE client_id = 3
-- #也可以使用IN来更新多个
-- WHERE client_id IN (3,4)

-- USE sql_store;

-- UPDATE customers
-- SET points = points + 50
-- WHERE birth_date < '1990-01-01';

#下面我们来用一下子查询
#子查询是指位于另一个SQL语句内部的SELECT语句
#使用方法就像下面这样

-- USE sql_invoicing;

-- UPDATE invoices
-- SET 	
-- 	payment_total = invoice_total * 0.5,
-- 	payment_date = due_date
-- WHERE client_id IN#记得使用IN
-- 			(SELECT client_id
-- 			FROM clients
--             WHERE state IN ('CA', 'NY'))

#有黄色感叹符号说明运行成功了，但是有警告

USE sql_store;

UPDATE orders
SET comments = 'Gold-Customer'
WHERE customer_id IN
		(SELECT customer_id#这里要注意选择想应的列
        FROM customers
        WHERE points >= 3000)