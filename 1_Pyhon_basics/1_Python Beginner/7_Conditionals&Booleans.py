#布尔逻辑，True是对，False是错
#注意python里的True和False首字母要大写

#在python的判断语句中，!=,==,>,<,<=,>=同C++一样,不同的是is,后面会介绍
#if else 如果 否则，和C++的差不多，非常简单
#唯一注意的点是":"号，if和else,elif后面要加":"号

print('')
print('1----------------')
age = 32
if age == 18:
    print("人家刚满18岁！")
elif age < 18:
    print("人家还是小孩子！")
else:
    print("不是你什么意思？人家的年龄有那么重要吗？")

#下面介绍and,or,not
#and非常简单，用and连接的两个条件都是必要

print('')
print('2----------------')
xueli = '博士'
xuexiao = '假清华'

if xueli == '博士' and xuexiao == '清华':
    print('哈哈哈把公司当自己家！')
else:
    print('能接受996吗？')

#or也很简单，二者中满足一个即可

print('')
print('3----------------')
name = '王源'
xueli_a = '初中'

if name == '王源' or xueli_a == '博士':
    print('哥哥我好爱你！')
else:
    print('下头男！滚远点！')

#not就是和'不'相似的意思，转换True与False

print('')
print('4----------------')
age = 18
if not age == 18:#注意这里True反转成了False
    print('刚满18岁？骗人的吧')
else:
    print('这个年龄我们不收')

#下面介绍判断符号is，is与==的不同点是，is会判断两者是否在对象中是同一个位置
#举个简单的例子

print('')
print('5----------------')
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)#两者相等返回True
print(a is b)#两者虽然相等，但不是一个内存块
print(a[0] is b[0])#这是个易错点，为什么返回True?因为python有对象复用/缓存机制,python只会创造一个1对象在所有地方都引用它
                   #你可以把它们看作一个指针，指向同一个整数1，但这种说法也并不严谨
                   #更严谨的说法，两个引用指向同一个对象
                   #引用也是一种指针，底层“可能”是地址，但这对你是不可见、不可依赖的

#要是不放心is，你可以用id函数直接查看他们的地址
#这个地址明显被封装了，不是计算机的内存地址

print('')
print('6----------------')
print(id(a))
print(id(b))
print(id(a[0]),id(b[0]))

if id(a) == id(b):#这个判断条件等价于 a is b
    print('他们是同个地址')
else:
    print('他们不是同个地址')

#下面我们来介绍几种python中会被判断为False的值
#第一种最简单的False

print('')
print('7----------------')
if False:
    print('True')
else:
    print('False')

#第二种是None

print('')
print('8----------------')
if None:
    print('True')
else:
    print('False')

#第三种是0,所有不是0的数包括负数都会是True

print('')
print('9----------------')
if 0:
    print('True')
else:
    print('False')

#第四个种，空的字符串，列表，元组，字典，非空的都会是True

print('')
print('10----------------')
a = ''
b = []
c = ()
d = {}

if a:
    print(True)
else:
    print(False)

if b:
    print(True)
else:
    print(False)

if c:
    print(True)
else:
    print(False)

if d:
    print(True)
else:
    print(False)