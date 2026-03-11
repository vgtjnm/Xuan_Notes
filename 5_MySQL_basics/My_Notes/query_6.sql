#下面我们来学习限制条款
#运用场景比如在customer中我们只想得到前三个用户

#我们是用LIMIT来限制获取的数量
#如果LIMIT限制大于数据的总数，那么会直接获取所有数据
#限制是300，但是数据只有10，那么会直接获取10
-- SELECT *
-- FROM customers
-- LIMIT 300

#LIMIT可以设置偏移量
#下面这个LIMIT意思就是跳过前6个然后选3个
-- LIMIT 6,3;

#下面来写个练习，只获取积分最多的前三个用户
-- SELECT *
-- FROM customers
-- ORDER BY points DESC
-- LIMIT 3;

#然后是一个重点,SQL里LIMIT一般都是在最后，下面是SQL的正常语句顺序：
-- SELECT
-- FROM
-- WHERE
-- ORDER BY
-- LIMIT
#这个顺序很重要