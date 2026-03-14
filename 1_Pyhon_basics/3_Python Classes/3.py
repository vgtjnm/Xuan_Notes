#员工们最近都开始抱怨加班了，所以要涨点工资来平息他们的愤怒

class Employee:

    #因为每个员工的涨薪幅度不同，所以写一个类变量控制加薪的幅度
    raise_amount = 1.04
    #设计一个变量来记录员工总数
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + ' ' + last +'@company.com'
        #每次新增一个员工都会使用一次init，所以在这里记录员工总数
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    #我们来写一个方法给员工们加工资,用上我们的涨薪变量
    #这里如果你直接复制粘贴会报错，因为python不知道他是谁的变量
    #所以你要加上本体或者类名称
    #注意使用本体和类是不一样的，看到下面你就会知道区别了

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

#设置员工的初始属性

emp_1 = Employee('Tom', 'John', 50000)
emp_2 = Employee('Ana','John', 50000)

#打印员工总数

print('1-----------------')
print(Employee.num_of_emps)

#给员工Tom涨一次薪

print('')
print('2-----------------')
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

#想要查看一个类变量的所有附带属性可以使用'__dict__'方法
#你可以发现他并没有涨薪幅度这个属性

print('')
print('3-----------------')
print(emp_1.__dict__)

#想要查看一个类的附带属性也是一样
#你可以看到他拥有涨薪幅度这个属性

print('')
print('4-----------------')
print(Employee.__dict__)

#我们可以更改一个类的某个属性，比如说涨薪幅度
#如果一个类的属性更改了，那么类变量的相同属性也会更改

print('')
print('5-----------------')
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)

#但是我们可以不改变类，直接改变类变量，这样这个属性就是独特的了

print('')
print('6-----------------')
emp_1.raise_amount = 1.10
print(emp_1.raise_amount)
print(Employee.raise_amount)

#你可以看到员工1的修改并没有影响到整个员工的修改
#到这里你可能会有个疑惑
#我之前用dict查看类变量的时候没有涨薪幅度这个属性啊
#因为当你给类变量的属性赋值时，他就创建了一个属性
#当一个类变量已经拥有了类的一个属性时，再通过修改类去修改就是无效的了
#你可以亲自尝试一下