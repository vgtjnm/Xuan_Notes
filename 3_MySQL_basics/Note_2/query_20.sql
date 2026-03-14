#最后一站CRUD之DELETE

-- USE sql_invoicing;

-- #DELETE的使用非常简单，直接DELETE FROM
-- DELETE FROM invoices
-- #我们当然可以搭配WHERE去指定目标了
-- -- WHERE invoice_id = 1
-- #也可以搭配子查询
-- WHERE client_id IN
-- 		(SELECT client_id#外面需要什么就选择什么，外面需要id就选id
--         FROM clients
--         WHERE name = 'Myworks')
