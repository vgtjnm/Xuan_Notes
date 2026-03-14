#这节将是我们类的最后一课，属性装饰器
#这个东西我们也接触过了，就是之前写类方法和静态方法的时候

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    #property是一个属性装饰器
    #他是用来装饰属性的，让程序把它当成一个属性
    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    #我们的fullname也可以使用它
    #这样就不用像方法一样打括号了
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    #下面是setter属性装饰器
    #他是用来反向设置的
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    #下面我们来看deleter属性装饰器
    #看名字就知道他是来删东西的
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None
    #删除器代码会在我们删除属性时运行

emp_1 = Employee('Corey', 'Schafer', 500)


#我们下面来测试一下，他们是否被视为属性了

print(emp_1.email)
print(emp_1.fullname)

#下面我们来看setter的作用

emp_1.fullname = 'Tom John'
print(f'{emp_1.first} {emp_1.last}')#可以看到直接修改成功了

#如何使用删除呢？很简单直接delete就行了
del emp_1.fullname

#恭喜看到这里的你！
#你可以去找几个项目练练手然后就去选择方向了
#方向有三个pandas，flask，和自动化
#先看你自己的兴趣去选择一个吧
#加油未来的程序员！