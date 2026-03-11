#目前为止我们只是从单个表中选择列
#但在实际工作中我们要从经常多个表中选择列
#这也是我们下面要学习的东西，非常重点，建议多次复习

-- SELECT *
-- FROM orders
#JOIN关键字可以帮助我们达成不同表的列的比较
-- JOIN customers
#我们希望基于什么基础来连接这些表呢？
#因为两个表是并列的，所以需要对齐链接
#这里我们希望他在customer_id中对齐，对齐使用ON去实现
#这里的orders.customer_id就是orders表中的customer_id列的意思
-- ON orders.customer_id = customers.customer_id
#上面的JOIN和ON语句也是在告诉MySQL一件事
#无论何时访问订单表，在客户表中，确保客户id列正确无误

#现在这个表太长了，我们可以对它进行简化，仅选择结果集
-- SELECT 
--  order_id,
--  first_name,
-- last_name
-- FROM customers
-- JOIN orders
-- 	ON customers.customer_id = orders.customer_id
-- ORDER BY order_id;

#这里有个点是，你不能在SELECT中直接选择customer_id
#因为customer_id在两个表中都有，MySQL不知道你要用哪一个
#但是加上前缀就可以，就像下面这样，MySQL知道是谁之后就不报错了
-- SELECT orders.customer_id

#你可能会觉得每次调用都要一个长长的前缀很麻烦，所以想简化操作
#在MySQL中我们只需要在FROM和JOIN指向的表后加上别名，就可以直接使用
-- SELECT 
--	order_id,
--	o.customer_id,
--  first_name,
--  last_name
-- FROM orders o
-- JOIN customers c
-- 	ON o.customer_id = c.customer_id

#下面我们来做个练习
#你需要写个查询语句在order_items和products两个表中
#对齐product_id，展示oi表中的所有内容，oi为主表
#还有一个要求，简化代码使用别名

#*可以加前缀，帮助我们简化操作
SELECT oi.*
FROM order_items oi
JOIN products p
	ON oi.product_id = p.product_id