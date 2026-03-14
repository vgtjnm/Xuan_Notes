#这次我们来学习类的特殊方法，而有的人称之为魔法
#什么是特殊方法呢？比如‘__init__’就是一个
#你也发现了，特殊方法的左右两边都有两个下划线

class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def apply_raise(self):
        self.pay = self.raise_amount * self.pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    #repr是一个特殊方法
    #他的用处是给程序员 / 调试器 / 交互环境看的对象说明书

    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.pay)

    #str也是一个特殊方法
    #他的用处是打印类成员时，直接打印str的返回值

    def __str__(self):
        return "{}-{}".format(self.fullname(), self.email)

    #小结一下，init,repr,str是最常用的三个特殊方法，请务必熟练掌握

    #下面介绍一些其他的特殊方法

    #add允许我们来控制两个类成员相加的结果

    def __add__(self, other):
        return self.pay + other.pay

    #想了解更多类的特殊方法，建议上网搜索python相关文档

emp_1 = Employee(first='Lucy', last='Smith', pay=100)
emp_2= Employee(first='Tom', last='John', pay=200)


#你可以用下面这个打印来测试repr和str的效果
print(emp_1)

#下面我们来看1+2=3
print(1+2)

#当我们像上面这样1+2=3时，他实际上在后台使用了名为下划线加法的特殊方法
#你可以直接访问这个方法就像这样

print(int.__add__(1,2))

#字符串也是同理

print(str.__add__('abc','aaa'))

#我们下面来测试我们写的add方法
#由于我们在add里设置返回他们的工资总和
#所以这里会打印他们的工资相加

print(emp_1+emp_2)