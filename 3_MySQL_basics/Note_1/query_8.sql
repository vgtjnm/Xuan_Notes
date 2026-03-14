#在真实任务里我们会需要操作多个数据库
#现在我们来学习数据库之间的交互

#注意之前我们学的是表与表中列的交互
#而现在是数据库之间的表的交互，这其实很简单

#现在我们有两个数据库sql_inventory和sql_store
#我们希望他们的共同表products的数据一样
#所以我们可以这样写

-- SELECT oi.*
-- FROM order_items oi
#我们在前缀里加上数据库名字，MySQL就知道我们要干嘛了
-- JOIN sql_inventory.products p
-- 	ON oi.product_id = p.product_id
    
#注意这里有一个重点，你可能也注意到了
#就是我们的order_items没有数据库前缀也正常运行了
#因为我们目前正在使用这个数据库，所以不用加前缀
#还记得吗以前我们使用USE去指定数据库
#如果你使用USE去指定sql_inventory然后order_items不加数据库前缀，那么会报错

-- USE sql_inventory;#这里记得分号
-- SELECT *
-- FROM order_items;

#加上数据库前缀就不报错了

-- USE sql_inventory;
-- SELECT oi.*
-- FROM sql_store.order_items oi;

#下午再战，这里mosh教了一个JOIN自身调用，感觉挺重要的

USE sql_hr;

SELECT
	e.first_name,
    e.last_name,
    m.first_name
FROM employees e
JOIN employees m
#这里链接对应的人的id，所以才能链接自己
	ON e.reports_to=m.employee_id