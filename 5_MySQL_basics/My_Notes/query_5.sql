#下面我们来学习IS
#IS 可以配合 WHERE 帮助我们寻找相关属性的数据
#但是IS一般不能用在数字，普通的值比较用=

#下面的代码就是使用IS来寻找没有手机号的数据
-- SELECT *
-- FROM customers
-- WHERE phone IS NULL
#NULL也可以搭配NOT去使用，将情况反转
-- WHERE phone IS NOT NULLorder_statusesorder_statuses

#下面是一个小练习，获取未发货订单
-- SELECT *
-- FROM orders
-- WHERE shipped_date IS NULL;

#下面我们来学一下排列
-- SELECT *
-- FROM customers
#默认情况下，如果你没有对查询目标去排序，会优先排列主键列
#怎么知道主键列是谁？在表右边三个按钮中的扳手按钮可以查看
#主键列是那个左边有黄色闪电的

#如果想要它按别的列去排序就要用到ORDER BY
-- ORDER BY first_name;

#想反转ORDER BY排序那就直接在目标后面加上DESC
-- ORDER BY first_name DESC;

#想设置排序次目标就在主目标后直接添加就行
#次排序的意思是，如果主排序相同就按次排序大小来排
-- ORDER BY state,first_name;

#设置排序多个目标的同时也可以同时设置反转，一般称之为降序排序
-- ORDER BY state DESC, first_name DESC;

#mysql有一个和其它数据库管理系统不同的点
#mysql可以按任何列（无论是否在SELECT子句中）获取数据
#举个例子，下面这个代码在其它数据库管理系统都是不允许的，但是mysql可以
#在SELECT里的AS作用就是用来起一个临时的列
-- SELECT first_name, last_name,10 AS points
-- FROM customers
-- ORDER BY points,first_name;

#claude说这个知识点很简单也很好理解
#10 AS points是什么意思？
#就是给每一行添加一个"临时列"，这列的名字叫 points，每行的值都是 10。
#为什么可以对它排序？
#因为 ORDER BY 是在 SELECT 之后执行的，所以它能"看到" SELECT 创建的所有列，包括你临时造的这个 points 列。
#Mosh 这里用的是固定值 10，所以排序没什么意义（大家都是10）。但真实用法通常是这样的：
-- SELECT first_name, last_name, points * 1.1 AS adjusted_points
-- FROM customers
-- ORDER BY adjusted_points;
#这样你就可以对计算结果起个名字，然后再排序——这才是这个语法真正有用的地方。

#然后是ORDER BY的简单用法
-- SELECT birth_date,first_name, last_name
-- FROM customers
#这里对1,2进行排序，就是对SELECT的第一和第二个对象进行排序
#不过这种用法在工程中比较少用，建议直接使用名称
-- ORDER BY 2,3


#下面是个练习，在order_items中选中订购id为2
#显示总价并按总价降序排列
SELECT
	order_id,
    product_id,
    quantity,
    unit_price,
    quantity * unit_price AS total_price
FROM order_items
#用=2而不是IS2，SQL中IS只用在特殊情况
WHERE order_id = 2
ORDER BY total_price DESC;