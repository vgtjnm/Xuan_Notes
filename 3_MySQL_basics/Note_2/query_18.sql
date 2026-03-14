#下面我们要来学习如何从一个数据库复制数据
#从一张表到另一张表

-- USE sql_store;

-- #首先我们先创建一个表

-- CREATE TABLE orders_archived AS
-- SELECT * FROM orders;

#这里运行完之后要点右上角刷新一下
#然后有个点要注意，创建完表之后，表是没有主键的，需要自己去设置
#建完表后右键Truncate可以清空表的内容

#下面我们来学复制到表怎么做
#首先先INSERT INTO
-- INSERT INTO orders_archived
-- #然后选择作为子句，选择想要复制的内容
-- SELECT *
-- FROM orders
-- WHERE order_date <'2019-01-01'

#mosh这里说他要布置一个非常酷的练习
#来到我们的sql发票数据库，查看发票表格，你可以看到有一系列的信息
#现在假设你想创建记录的副本，将他们放入此表中，并放入名为‘发票仓库’的新表
#在该表中显示的不是客户id而是客户名称列，所以需要将此表连接与clients表关联
#然后查询作为子查询用于创建表的语句中
#此外为了让练习更有趣，希望你复制那些已经付款的发票，支付日期决定了哪些支付完成了

#总结： 创建一个叫 invoices_archived（发票仓库）的新表，把已付款的发票数据复制进去。
#具体要求：
#从 invoices 表取数据
#和 clients 表 JOIN，把 client_id 替换成 client_name
#只复制已付款的发票（即 payment_date 不为空/有值的记录）
#用 CREATE TABLE ... AS SELECT ... 语法来建表

USE sql_invoicing;

CREATE TABLE invoices_archived AS
SELECT
	i.invoice_id,
    i.number,
    c.name AS client, 
    i.invoice_total,
    i.payment_total,
    i.invoice_date,
    i.payment_date,
    i.due_date
FROM invoices i
JOIN clients c
	USING (client_id)
WHERE payment_date IS NOT NULL;

#为了改个名字就把所有列列出来其实很麻烦
#不过有个稍微偷懒的办法，先看看 invoices 有哪些列：
#DESCRIBE invoices;
#然后把所有列复制过来，只把 i.client_id 那行换成 c.name AS client 就好了，其他列直接粘贴，不用自己一个个想。
#实际工作中也是这么干的，没人会背所有列名 