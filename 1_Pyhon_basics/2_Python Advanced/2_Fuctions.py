#函数是把一堆程序集合到一起复用的东西，方便我们重复使用
#下面我们来看Python中函数的定义

def hello_func():#记得加上括号！
    print('hello world')

#如果你想先定义一个函数稍后再写可以用到pass方法
#使用pass之后，代码不会报错

def paly_func():
    pass

#想要运行函数就直接在函数名字后面加上括号就行了

print('1-------------')
def sayhello():
    print('hello!')
    return 233
sayhello()

#如果没有加括号，说明你想要函数的内存地址

print('')
print('2-------------')
print(sayhello)

#函数会返回值，如果没有返回值会返回None

print('')
print('3-------------')
print(sayhello())
def kong():
    a = 1
print(kong())

#小结一下函数的用法，在很多需要重复代码的地方，可以写一个函数替换掉，这样使用和修改起来非常方便

#关于函数返回值的机制跟C++类似的就不再赘述
#我们下面说点Python特有的
#第一是Python可以返回字符串

print('')
print('4-------------')
def name():
    return 'Tom'
print(name())

#第二是Python的返回值可以搭配方法使用

print('')
print('5-------------')
print(name().upper())
print(name().lower())

#现在来介绍python的函数如何设置参数
#Python的函数参数特别的一点是不需要设置类型

print('')
print('6-------------')
def howdy(greeting):
    return f'{greeting}!'
print(howdy('hello'))

#还有一点是可以设置默认值，设置了之后，即使没有填写也不会报错

print('')
print('7-------------')
def courses(ca,cb='English'):
    return f'您选择的课程是{ca}和{cb}'
print(courses('Chinese'))

#下面的内容有点难理解需要认真看

print('')
print('8-------------')
def student_info(*args,**kwargs):#这样子取名是工程规范
    print(args)
    print(kwargs)

student_info('Math','Art',name='John',age=22)

#为什么会这样子？
#首先，我们的函数是接收一个列表+一个字典，对应args和kwargs
#*其实就相当于解包，例如把a列表变成[1,2,3,4,5]
#字典需要解包两次所以是**
#下面举一个更通透的例子

print('')
print('9-------------')
course = ['Math','Art']
info = {'name':'John','age':22}#注意name要加引号！排错排了好久还以为bug了

student_info(course,info)
#可以发现，我们输入的和之前的输入的最终解包是一样的，但是结果却不一样
#说明的初始解包状态不一样，还需要解包
#就像下面这样

print('')
print('10-------------')
student_info(*course,**info)

#这段知识点可以慢慢消化，就像当初学指针一样，不着急
#虽然现在已经理解了呵呵：》

#原视频在这里介绍了一些内容，概括一下就是你如果已经理解了目前所学的知识，你就已经可以写出或者理解一些较为专业的东西了

#如果你学到了这里恭喜你！你已经不能被称为编程萌新，而是踏入菜鸟级别！
#所以加油吧！编程菜鸟：）