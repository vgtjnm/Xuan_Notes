#下面我们将要学习IN这个好用的东西

-- SELECT *
-- FROM customers

#如果没有IN，我们写判断就会很麻烦
-- WHERE state = 'VA' OR state = 'FL' OR state = 'GA';
#但是有了IN，我们可以这么写
-- WHERE state IN ('VA','FL','GA');
#它也可以搭配NOT去使用
-- WHERE state NOT IN ('IN','FL','GA');

-- SELECT *
-- FROM products
-- WHERE quantity_in_stock IN (49,38,72);

#下面我们来学BETWEEN
-- SELECT *
-- FROM customers
#如果没有BETWEEN会变成这样
-- WHERE birth_date >= '1990-01-01' AND birth_date <= '2000-01-01'
#有了BETWEEN之后会更方便，要搭配AND去使用
-- WHERE birth_date BETWEEN '1990-01-01' AND '2000-01-01';

#下面我们来学LIKE
-- SELECT *
-- FROM customers
#LIKE 就是指定开头的意思，用法有点像正则
#下面这个代码的意思就是匹配'b'开头，'%'表示之后可以接任意字符，0个或者100个
-- WHERE last_name LIKE 'b%'
-- WHERE last_name LIKE 'brush%';
#在前面也可以加'%'，下面代码匹配有个'b'就行
-- WHERE last_name LIKE '%b%';
#还有'_'这个字符，意思是匹配一个字符
#下面代码的意思是匹配两个字符的名字且第二个是y
#显然没有人叫这么奇怪的名字
-- WHERE last_name LIKE '_y';
#但是五个字符加'y'的就有
-- WHERE last_name LIKE '_____y';

-- SELECT *
-- FROM customers
-- WHERE address LIKE '%TRAIL%' OR
-- address LIKE '%AVENUE%';
      
-- WHERE phone LIKE '%9';

#还有一个东西叫做REGEXP
#REGEXP 是正则表达式（Regular Expression）的缩写
#用于按照复杂的模式匹配字符串，比 LIKE 强大得多
-- SELECT *
-- FROM customers
#他的效果等同于LIKE'%field%'
-- WHERE last_name REGEXP 'field'

#在这里还有说个极其重要的知识点：
#LIKE 只支持两种通配符：%（任意多个字符）和 _（单个字符）
#正则符号如 ^、$ 只能在 REGEXP 中使用

#当你在匹配里加上'^'时，意味着必须以它去开头
-- SELECT *
-- FROM customers
-- WHERE last_name REGEXP '^brushfield';

#当你在匹配中使用'$'时，意味着必须以它去结尾
-- WHERE last_name REGEXP 'field$';

#使用'|'可以帮助我们搜索多个词类似或者的意思
-- WHERE last_name REGEXP 'field$|^mac|^rose';

#使用'[]'可以帮助我们在一个字符的前面或者后面匹配东西
-- WHERE last_name REGEXP '[gim]e[ly]'

#想用'[]'匹配abcdefg，可以直接a-g
-- WHERE last_name REGEXP '[a-g]e'

#我来汇总一下目前的REGEXP正则
-- ^ 必须以它开头
-- $ 必须以它结尾
-- | 或
-- [abcd]
-- [a-f]
-- 以上是REGEXP里最常用的几个了

-- SELECT *
-- FROM customers
-- WHERE 
-- first_name REGEXP 'ELKA|AMBUR';
-- last_name REGEXP 'EY$|ON$';
-- last_name REGEXP '^MY|SE';
-- last_name REGEXP 'B[RU]';