#下面准备要学的是如何编写代码时链接两个以上的表

-- USE sql_store;

-- SELECT 
-- 	o.order_id,
--     o.order_date,
--     c.first_name,
--     c.last_name,
--     os.name AS status
-- FROM orders o
-- JOIN customers c
-- 	ON o.customer_id = c.customer_id
-- #目前为止都是我们学过的，但是下面我们可以继续写JOIN
-- #这就是我们链接三个表的方法
-- JOIN order_statuses os
-- 	ON o.status = os.order_status_id

USE sql_invoicing;

SELECT 
	p.date,
    p.invoice_id,
    p.amount,
    c.name,
    pm.name AS payment_method
FROM clients c
JOIN payments p
	ON c.client_id = p.client_id
JOIN payment_methods pm
	ON p.payment_method = pm.payment_method_id