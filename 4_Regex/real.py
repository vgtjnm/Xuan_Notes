#妈呀正则哪用搞这么麻烦，相信我看完这个注释，两小时搞定后端实用正则，不背天书

#首先在python中要使用正则需要导入re模块
import re

#下面我来给你看一下后端里使用正则的样子，我们一般写成一个函数，返回布尔值
#顺便说一下之前在教程没介绍的点，python函数的一些知识
#我们的python函数可以给参数规定类型，就比如下面的字符串类型，使用方法参数名+':'+类型名称（int,str）
#然后我们也可以规定返回值类型使用方法，'->'+返回类型名（list,str,bool），工程代码一般要写，方便接手
def is_phone(phone:str) -> bool:

#   我们一般会写个变量来作为正则，不然的话return太长真的很丑
#   可以看到正则就是这样写的，我来解释一下他们是什么意思
#   r"..."表示这是一个原始字符串，不翻译'\'
#   '^' + 字符 ，意思是以该字符开头，可以是数字或者字母
#   '['，意思是开始定义一个字符集
#   ']'，意思是结束一个字符集
#   '[3-9]'，指的是只能是3-9的数字
#   '\d'，意思是匹配一个数字，等价于[0-9]
#   '{数字}'，意思是将前面的表达式重复数字次
#   '{9}'，意思是将前面的表达式（文中是'\d'）重复9次
#   '$'，意思是匹配字符串的结束位置，后面不能有字符
    pattern = r"^1[3-9]\d{9}$"

#   下面我们会使用bool()将值转成布尔值
#   然后会使用re.match方法，使用方法是
#   re.match(正则，匹配的字符串)，匹配成功返回 True，失败返回 False
#   使用 bool(re.match()) 将匹配对象或 None 转换为布尔值

    return bool(re.match(pattern, phone))

#上面的is_phone就是匹配手机号了，现在我来学匹配邮箱

def is_email(email:str) -> bool:

#   下面我们来解析邮箱验证的正则
#   r和^同上，就是原始字符串和控制开头
#   '[]'同上，就是开始和结束一个字符集
#   '\w'意思是匹配字母数字下划线，等价于[a-zA-Z0-9_]
#   '.'匹配点号，'-'匹配连字符
#   '[\w.-]'意思就是匹配数字字母下划线(\w)，'.'号（.），'-'号（-）
#   '+'意思是前面的字符集（[\w.-]）会出现1次或多次（至少1次）
#   '@'意思是匹配'@'符号
#   '[\w.-]+'同上
#   '\.'匹配字面意义上的点号，需要用'\'转义，因为点号在正则中有特殊含义
#   '\w+'匹配一个或多个数字字母下划线（至少1次）
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

    return bool(re.match(pattern, email))

#然后是校验用户名，这里只是举例，具体数据看甲方需求

def is_username(username:str) -> bool:

#   如果你认真看完了上面的注释且尝试过，那么这个你都能自己翻译了
#   r是原始字符串不翻译'\'号，除了转义
#   '^'是必须以后面的字符开头
#   '\w'是数字字符下划线
#   '{6,12}'重复至少6次，最多12次
#   '$'结束匹配

#   但这里我要说一个额外的东西
#   就是r"^\w{6,12}$"可不可以写成r"\w{6,12}$"，去掉'^'号
#   答案是不行，原因是他们有很大区别
#
#       写法	          含义	                匹配方式
#   r"^\w{6,12}$"	 严格匹配	   整个字符串必须完全是6-12个单词字符
#   r"\w{6,12}$"	 松散匹配	   字符串结尾必须是6-12个单词字符，前面可以有其他内容

    pattern = r"^\w{6,12}$"
    return bool(re.match(pattern, username))

#然后就是关于一个文本提取所有URL了，这部分可以写的比较简单，也可以写的比较复杂
#我的建议是学简单的，复杂的需要再去查，不值得在它身上花太多精力
#下面我们来看简单版的实现
#因为我们是提取一个文本的所有URL所以返回一个列表

def extract_urls(text:str) -> list:

#   ok呀这个正则挺多东西前面没见过的，没关系我来慢慢解释
#   首先'http'意思是匹配字符串'http'
#   's?'意思是's'可出现0次或1次，这里意思是可以匹配'http'或者'https'
#   '://'匹配字符串'://'，这里不需要转义因为都是普通字符
#   '[^...]'是个否定字符集，表示不匹配括号里的任何内容
#   \s表示空白字符（空格，制表符，换行等）
#   '[^\s]'表示不匹配任何空白字符
#   '[^\s]+'表示不匹配任何空白字符，且其他匹配字符至少出现1次或多次
    pattern = r"https?://[^\s]+"

#   然后来说一下re.findall(pattern,str,flags)
#   pattern是我们的正则，str是我们要匹配的字符串，flags是可选参数，用于修改匹配行为
#   该函数会返回一个列表，如果没有匹配项会返回空列表
#   顺便说一下match,search,findall的区别
#
#   函数	           作用	            返回值	              适用场景
#   re.match	从开头匹配	    匹配对象或None	     检查字符串开头是否符合格式
#   re.search	搜索第一个匹配	匹配对象或None	        查找第一个匹配项
#   re.findall	搜索所有匹配	    列表	提取所有匹配项         提取所有匹配项
    return re.findall(pattern, text)

#现在我来写个关于一个文本提取所有数字

def extract_nums(text:str) -> list:

#   也可以写成r"[0-9]+"
#   但是不能写成r"^[0-9]+"，这样子会出问题
#   因为'^'意味着只能匹配数字开头的内容，findall碰到不是数字开头的字符串都会返回空列表
    pattern = r"\d+"
    return re.findall(pattern, text)

#现在我们来测试一下我们写的正则

real_phone = '13417429291'
fake_phone = '23417429291'

print("")
print(f"13417429291 is {is_phone(real_phone)} phone 23417429291 is {is_phone(fake_phone)} phone")
print("")

real_email = '123534@qq.com'
fake_email = 'disahdi@234124com'

print("")
print(f"123534@qq.com is {is_email(real_email)} email disahdi@234124com is {is_email(fake_email)} email")
print("")

real_username = '123456789'
fake_username = '123'

print("")
print(f"123456789 is {is_username(real_username)} name 123 is {is_username(fake_username)} name")
print("")

test_text1 = """
今天访问了以下网站：
1. 谷歌搜索：https://www.google.com
2. 百度：http://www.baidu.com
3. Python官网：https://python.org
4. GitHub：https://github.com
5. 哔哩哔哩：https://www.bilibili.com

顺便也看了 http://example.com 和 https://test.org
联系邮箱：admin@example.com（这个不是URL哦）
"""

urls = extract_urls(test_text1)

for url in urls:
    print(url)