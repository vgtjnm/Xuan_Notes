#加上DISTINCT之后，不会出现重复的内容
-- SELECT DISTINCT state
-- FROM customers;

-- Return all the products
-- name
-- unit price
-- new price (unit price * 1.1)
#下面是实现代码
-- SELECT 
-- 	name,
--  unit_price,
--  unit_price * 1.1 AS new_price
-- FROM products;

-- SELECT *
-- FROM Customers
#WHERE可以指定条件，条件有：
#>, >=, <, <=, =, !=, <>
#<>和!=一样，不过<>在更多的数据库中都支持
#对象的类型可以是整型，字符型等，如果是字符类我们一般用单引号，还有就是MySQL里没有大小写这种区别
-- WHERE points > 3000
-- WHERE state <> 'VA';
#顺带一提，你还可以进行生日查询
-- WHERE birth_date > '1990-1-1'

-- GET the orders placed this year
#下面是解决代码
-- SELECT *
-- FROM orders
-- WHERE order_date >= '2019-01-01';

#如果我想要2018年之内的怎么办？
#MySQL提供了混合条件：
#AND,OR
-- SELECT *
-- FROM orders
-- WHERE order_date >= '2018-01-01' AND order_date < '2019-01-01'
-- FROM customers
-- WHERE birth_date >= '1986-04-01' OR 
--	  (points >= 3000 AND state = 'TX');
      
#我们讲一下逻辑条件的优先级（上面＞下面）：
# NOT
# AND
# OR
#运算的优先级也顺便说了吧：
# ()
# *,/
# +,-

SELECT *
FROM order_items
WHERE order_id = 6 AND quantity * unit_price > 30
