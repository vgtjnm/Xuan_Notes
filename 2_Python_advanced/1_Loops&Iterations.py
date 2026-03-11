#Python的循环和C++类似，且功能更加强大！
#下面是Python的for循环简单用法

print('1-------------')
for i in range(3):
    print(i)

#如果你的range可以设置初始和结尾

print('')
print('2-------------')
for i in range(1,3):#注意不包括3
    print(i)

#下面介绍Python的for循环强大之处，支持更多的遍历对象
#遍历对象包括字符串，列表等
#下面举几个例子
#这是遍历字符串

print('')
print('3-------------')
for c in 'abc':
    print(c)

#这是遍历整型列表

print('')
print('4-------------')
nums = [11,22,33]
for num in nums:#按照你列表的元素依次传入
    print(num)

#这是遍历字符串列表

print('')
print('5-------------')
string_a = ['a','b','c']
for c in string_a:
    print(c)

#break和continue与C++类似
#退出和跳过当前循环

print('')
print('6-------------')
for i in range(1,9):
    if i == 7:
        break
    if i % 2 == 0:
        continue
    print(i)

#while循环也非常的简单
#下面是简单的while循环用法

print('')
print('7-------------')
x = 9
while x > 5:
    print(x)
    x = x - 1

#你可以设置死循环，这样他会在输入框一直循环，按结束键可以结束，但是我目前好像找不到

#总结一下，除了for循环可以遍历字符串列表等等，都是其他高级语言共有的
#多多使用这个强大的功能吧！