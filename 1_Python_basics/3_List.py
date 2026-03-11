#下面是python的列表定义

courses = ['12','23']

#我们可以打印它

print('1----------------')
print(courses)

#使用len可以查看他的元素数量

print('')
print('2----------------')
print(len(courses))

#使用索引可进行单元素访问，访问除了-1以外不存在的值会报错

print('')
print('3----------------')
print(courses[0])

#列表的-1索引可以返回列表的最后一个值

print('')
print('4----------------')
print(courses[-1])

#当然他也支持切片,如果你在开头或者结尾参数为空，那么他会默认你到开头或者结尾

print('')
print('5----------------')
print(courses[0:])

#使用append函数可以给列表末尾添加新的值

print('')
print('6----------------')
courses.append('34')
print(courses)

#使用insert函数可以直接插入新的值在索引的位置，原索引的值会后退

print('')
print('7----------------')
courses.insert(0,'01')
print(courses)

#使用extend函数不仅可以添加多个值，还可以把添加的列表拆成单个值

print('')
print('8----------------')
courses.extend(['1','2'])
print(courses)
courses_2 = ['55','66']
courses.extend(courses_2)
print(courses)

#下面是区别，如果你不用extend添加列表，他会直接把列表视为一个单位
#拓展一下为什么列表可以存列表，因为python的列表的值实际上是引用
#当用到列表当中的某个值的时候，引用会去找到对象

print('')
print('9----------------')
courses_3 = ['123','234']
courses.append(courses_3)
print(courses)

#使用remove函数可以删除列表当中的值

print('')
print('10----------------')
courses.remove('01')
print(courses)

#使用pop函数会返回并移出列表的最后一个值

print('')
print('11----------------')
courses.pop()
print(courses)
a = courses.pop()
print(courses)

#使用reverse函数可以反转列表中的值

print('')
print('12----------------')
courses.reverse()
print(courses)

#使用sort函数可以对列表进行排序，字符列表按字母排序，整型列表按升序排序

print('')
print('13----------------')
courses.sort()
print(courses)
nums = [1,2,3,4,5]
nums.sort()
print(nums)

#想要降序排序可以搭配reverse函数，也可以直接在sort函数后参数使用reverse

print('')
print('14----------------')
nums.sort(reverse=True)
courses.sort(reverse=True)
print(nums)
print(courses)

#如果你只是想要一个返回值而不修改原函数去排序，可以使用sorted函数

print('')
print('15----------------')
fruits = ['apple','banana','orange']
fruits.sort(reverse=True)#注意！！！我这里使用了反转！！！
sorted_fruits = sorted(fruits)
print(sorted_fruits)
print(fruits)

#下面演示min,max,sum三个常规操作

print('')
print('16----------------')
nums = [1,2,3,4,5]
print(min(nums))#返回列表最小值
print(max(nums))#返回列表最大值
print(sum(nums))#返回列表综合

#使用index函数可以找到值的第一个索引，若值不存在它会报错

print('')
print('17----------------')
nums = [1,2,3,4,5,5,5]
print(nums.index(5))

#想检测某个值是否在某个列表，可以使用in来连接。他会返回布尔值

print('')
print('18----------------')
print(5 in nums)

#python中的for循环可以遍历列表

print('')
print('19----------------')
nums = [1,2,3,4,5]
nums.sort(reverse=True)
for num in nums:
    print(num)

#上面的for每次循环只会返回值，想要返回索引，可以使用enumerate函数

print('')
print('20----------------')
nums = [10,9,5,4,1]
for index,num in enumerate(nums):#这么操作之后，每次循环会返回索引和值，我们用两个循环变量来接收
    print("第"+str(index)+"个值是"+str(num))#想用+号连接循环转换同一类型

#在enumerate函数中添加start参数，只会改变初始索引的值，并不是从start的索引开始

print('')
print('21----------------')
for index,num in enumerate(nums,start=1):
    print("第" + str(index) + "个值是" + str(num))

#使用join函数可以为字符串列表添加分隔符号变成一个字符串,注意他会返回值而不是直接操作

print('')
print('22----------------')
courses = ['History','Math','Physics','Chemistry']
courses_str=' - '.join(courses)
print(courses_str)

#使用split函数可以反向操作，把一个字符串的小字符串提取出来变成列表

print('')
print('23----------------')
new_list = courses_str.split(' - ')#你的分隔符号是怎样，就填写怎样的值
print(new_list)