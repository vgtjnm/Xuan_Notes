#使用type可以查看变量类型

print('1----------------')
num = 3
print(type(num))

#常见的+，-，*就不介绍了，下面说几个不一样的

print('')
print('2----------------')
print(3/2)#这是python里面的普通除法，结果一定是浮点数
print(-3//2)#这是python的整除，结果去掉小数部分向下取整，负数向负无穷取整
print(3**2)#这是python的次方，这里是3的2次方
print(3%2)#这是python里的取余

#python有运算优先级

print('')
print('3----------------')
print(3+1*2)
print(3*(2+1))

#下面是python中对数字的常见操作函数

print('')
print('4----------------')
print(abs(-3))#abs函数取绝对值
print(round(3.14))#round函数四舍五入
print(round(3.14,1))#在后面填入参数可以精确到位数

#打印比较会返回布尔值

print('')
print('5----------------')
print(3 == 2)

#python中的类型转换非常简单，只需要类型名字的函数即可

print('')
print('6----------------')
num1 = "100"
num2 = "200"

num1 = int(num1)
num2 = int(num2)

print(num1 + num2)