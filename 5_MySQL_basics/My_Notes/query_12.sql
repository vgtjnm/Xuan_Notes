#下面我们来学习USING

-- USE sql_store;

-- SELECT 
-- 	o.order_id,
--     c.first_name,
--     sh.name AS shipper
-- FROM orders o
-- JOIN customers c
-- -- 	ON o.customer_id = c.customer_id
--     #上面这个ON我们可以使用更简单更短的USING子句代替
--     USING (customer_id)#效果和上面的ON一样，而且更简单
-- LEFT JOIN shippers sh
-- 	USING (shipper_id)
    
#你也知道了，USING的使用前提是双方都有这个列才行

-- USE sql_invoicing;

-- SELECT 
-- 	p.date,
--     c.name AS clients,
--     p.amount,
--     pm.name AS name
-- FROM payments p
-- LEFT JOIN clients c USING (client_id)#如果是USING可以在同一行写美观一点
-- LEFT JOIN payment_methods pm
--  	ON p.payment_method = pm.payment_method_id;