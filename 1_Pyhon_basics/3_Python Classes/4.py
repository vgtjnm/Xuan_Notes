#这次我们将学习方法，关于之前的注释里其实我的某些描述是不准确的
#有时候说是函数，有时候又是方法，因为在开始学习的时候我并不知道他的名字
#这个注释是给我自己看的哈哈，如果有别人看到了可以按理解去修正
#最好直接去看corey在youtube的原片

#在3里我们学习的是实例变量和类变量
#这次学习普通方法，类方法，静态方法的区别

#在介绍他们的区别前，我们要先创造一个类

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    #这个方法就是典型的普通方法，他会将第一个参数作为他本身
    #习惯上我们把第一个参数叫做self，这是个工程习惯

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    #类方法与普通方法区别之一就是类方法专门用来操作类
    #那怎么创建呢？很简单
    #使用classmethod装饰器

    @classmethod
    #类变量也有一个规定，那就是cls
    #cls和self的区别是cls是类，self可以是对象
    #在这个方法中，我们操作的是类而不是对象
    #你也可以用普通方法来操作类，这是python给你的自由
    #但是我极不推荐，这不是一个工程的好习惯，你在公司这样写会被裁掉，而且你以后看也会乱
    #另外补充一下对象和类变量的区别，他们不是一个东西
    #类变量是写在类里面的，属于整个类
    #而对象是我们创建的，会使用init先默认的，他们大多有独特的属性

    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    #下面我们来写另一个类方法来方便用字符串创建我们的员工
    #cls代表我们的类

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    #下面我们要来开始创建静态方法了
    #静态方法不用将第一个函数视为本身或者类了
    #而是像普通函数一样

    @staticmethod
    def is_workday(day):
        if (day.weekday() == 5) or (day.weekday() == 6):
             return False
        return True

#创建我们的员工

emp_1 = Employee('Corey', 'John', 50000)
emp_2 = Employee('Test', 'User', 100000)

#现在我们来使用我们创建的类方法吧

print('')
print('1-----------------')
Employee.set_raise_amt(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

#你也可以从对象中使用类方法
#但是这不是一个工程的好习惯，别人会看不懂

print('')
print('2-----------------')
emp_1.set_raise_amt(1.15)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

#有个人介绍了一个新员工，我们想添加进系统，但是他是字符串类型的
#这时我们可以使用学过的split方法

print('')
print('3-----------------')
emp_str_3 = 'Li-Hua-3000'
first, last, pay = emp_str_3.split('-')
emp_3 = Employee(first, last, pay)
print(emp_3.email)
print(emp_3.pay)

#当然我们也可以写一个类函数来完成，让我们回到类部分

print('')
print('4-----------------')
emp_str_4 = 'Han-Hua-4000'
emp_4 = Employee.from_string(emp_str_4)

print(emp_4.email)
print(emp_4.pay)

#使用我们的静态方法前我们要导入一个模块

print('')
print('5-----------------')
import datetime
my_date = datetime.date(2022, 2, 22)
print(Employee.is_workday(my_date))