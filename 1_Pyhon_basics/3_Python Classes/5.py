#这次我们来学习创建子类，就是类继承
#顾名思义，继承允许我们从父类继承属性和方法
#我们可以创造子类拥有父类的所有功能，然后可以重写和添加新的功能
#而且并不会影响到父类

#我们首先来创建一个类吧
class Employee:
    raise_amount = 1.10

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


#下面我们就要来使用类继承了
#使用方法非常地简单和创建类一样
#区别在类的名字后的括号是我们要写的父类

class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super.__init__(first, last, pay)
        self.prog_lang = prog_lang

#用子类创建两个开发者

dev_1 = Developer('Tom', 'John', 550,'Python')
dev_2 = Developer('Ana', 'John', 550,'C++')

#验证方法是否可用

print(dev_1.fullname())
print(dev_2.fullname())

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

#help函数可以帮助我们理解这些内容，你可以自己查看它
#print(help(Developer))
#打印出来后，你可以看到很多有用的信息
#你可以看到他的搜索路径，首先是方法解决方案
#他会首先在dev类中找init函数，如果找不到就去Emp类，如果还没有，他就回去object类
#python中的每个类都继承自基类object
#除了搜索路径，还有我们在Emp类中的方法和属性等等

#总结来说就是类继承是个方便的功能
#它的价值不在于写看不懂的代码，而是本身就是为了方便