#下面来学习怎么创建多行数据

USE sql_store;

-- INSERT INTO shippers (name)#我们只输入name
-- #直接多个括号插入就行
-- VALUES  ('Shipper1'),
-- 		('Shipper2'),
--         ('Shippers3')

-- INSERT INTO products (
-- 	name,
--     quantity_in_stock,
--     unit_price
-- )
-- VALUES 
-- 	('apple', '123', '6.2'),
--     ('banana', '221', '3.6'),
--     ('pencil', '2318', '2.25');

-- INSERT INTO orders (customer_id, order_date, status)
-- VALUES (1, '2019-01-02', 1);

-- #MySQL里也有内置函数
-- #LAST_INSERT_ID() 返回当前会话中最近一次 INSERT 操作生成的自增主键值
-- #核心特性：
-- #1.会话级别隔离：每个连接只能看到自己的插入结果，不受其他并发连接影响，线程安全。
-- #2.只反映当前连接：即使其他用户同时插入数据，你的 LAST_INSERT_ID() 也不会改变。
-- #3.批量插入时：返回第一条记录的 ID，不是最后一条。

-- SELECT LAST_INSERT_ID()

INSERT INTO orders (customer_id, order_date, status)
VALUES (1, '2019-01-02', 1);

#LAST_INSERT_ID也可以这样去用
INSERT INTO order_items
VALUES
	(LAST_INSERT_ID(), 1, 1, 2.95),
    (LAST_INSERT_ID(), 2, 1, 3.95)