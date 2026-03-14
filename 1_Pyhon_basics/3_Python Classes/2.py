#类是可以初始化的，如果所有的东西都要手动填写那工程量就太大了

class Employee:
    #我们来写一个方法用来初始化类
    #每个普通方法的第一个参数都必须要写来代表它本身，不然用它是就会报错

    def __init__(self,first,last,pay,):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '-' + last + '@company.com'

    def fullname(self):#第一个参数是他本身
        return f'{self.first} {self.last}'#self代表他本身
                                          #关于self的命名他不是一个关键字，但是是一个工程代码常用字

#我们下面就来给我们的员工快速的输入数据吧

emp_1 = Employee('Tom','John',5505)
emp_2 = Employee('Ana','Mei',7505)

#到这里我要解释一个很重要的点，你可能也会疑惑
#为什么我们写在类里的‘__init__’方法第一个参数self不用传
#原因是'__init___'这个名字在python的类中是个特殊字
#说明这个方法会在对象创建的时候自动执行，类似C++的'main'程序从主函数执行
#这个self的参数呢是跟'__init__'一样的，不用传参，所以可以把它忽略
#原视频里对self参数有介绍，可以去看一下
#还有就是'init'和'__init__'不一样，需要左右两边各有两个'_'

#下面我们使用之前学过的format函数来打印一下员工的名字

print('1-----------------')
print(f'{emp_1.first} {emp_1.last}')
print(f'{emp_2.first} {emp_2.last}')

#你可以发现我们打印一个员工的信息要输入很长的内容，非常不方便！
#所以我们们给类写了另一个普通方法fullname来快速使用

print('')
print('2-----------------')
print(emp_1.fullname())
print(emp_2.fullname())

#请注意一下，属性不需要括号，方法需要括号
#不然就会打印方法，而不是返回值

print('')
print('3-----------------')
print(emp_1.fullname)
print(emp_2.fullname)

#如果你使用类的名字+方法来查看一个对象，那你需要告诉python你要看哪个对象

print('')
print('4-----------------')
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))