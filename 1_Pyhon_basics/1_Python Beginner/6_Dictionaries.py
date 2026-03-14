#字典类似于C++的map映射
#下面来看字典的定义

print('1----------------')
student_1 = {
    "name" : "John",
    "age" : 25,
    "courses" : ['Math','Chinese']
}
#你可以看到字典的键值可以是字符串，整数甚至列表
#左边的统称为键，右边的统称为键值

#你可以打印你的字典,查看它的对照关系

print('')
print('2----------------')
print(student_1)

#你也可以输入参数键打印查看键值，访问不存在的键会报错

print('')
print('3----------------')
print(student_1["name"])
print(student_1["age"])

#想要确定一个键是否存在键值，可以使用get函数
#存在会返回键值，不存在会返回None

print('')
print('4----------------')
print(student_1.get("name"))
print(student_1.get("phone"))

#get后面的第二个参数会对不存在的键返回第二个参数

print('')
print('5----------------')
print(student_1.get("courses","Not Found"))
print(student_1.get("course","hahaha"))

#如果想在字典定义外设置新的键与键值，用到下面的方法

print('')
print('6----------------')
student_1['phone'] = '123456'
print(student_1.get('phone'))

#重复设置存在的键会直接新键值覆盖旧键值

print('')
print('7----------------')
student_1['age'] = 33
print(student_1.get('age'))

#想要更新字典使用update函数会更方便

print('')
print('8----------------')
student_1.update({"name":"Tom","age":23})
print(student_1)

#想要删除一个字典的键与其对应键值，可以使用del方法

print('')
print('9----------------')
del student_1["age"]
print(student_1)

#当然你也可以使用pop函数去删除
#重复一遍pop函数的特点，会实际操作+返回值

print('')
print('10----------------')
student_1['age'] = 22#因为age删除了所以重新设置
age = student_1.pop("age")#注意python不关心你是单引号还是双引号
print(age)
print(student_1)
print(age)

#想要知道一个字典里有多少个键同样可以用len函数

print('')
print('11----------------')
student_2 = {
    "name" : "Mei",
    "age" : 28,
    "courses" : ['Math','English']
}
print(len(student_2))

#想要查看键的名字，可以使用keys函数

print('')
print('12----------------')
print(student_2.keys())

#想要查看键值，可以使用values函数

print('')
print('13----------------')
print(student_2.values())

#想要查看键与键值，可以使用items函数

print('')
print('14----------------')
print(student_2.items())

#你也可以遍历字典，之间遍历他会给循环变量键，没有键值

print('')
print('15----------------')
for key in student_2.keys():
    print(key)

#想要循环变量同时有键与键值，可以使用items函数

print('')
print('16----------------')
for key, value in student_2.items():
    print(str(key) + ":" + str(value))#想要用加号连接需要保证类型一致

#这么写也是可以的

print('')
print('17----------------')
for key, value in student_2.items():
    print(key, value)