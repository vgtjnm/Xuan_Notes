#集合是无序的值，而且不能有重复项
#下面看看集合的定义

cs_courses = {'History','Science','Math','English'}

#集合是无序的，你可以看到每次打印的值的顺序都不太一样

print('1----------------')
print(cs_courses)

#如果你给集合添加了重复的值，他也只会保留一个

print('')
print('2----------------')
num_list = {'1','2','3','4','1'}
print(num_list)

#如果你使用in在集合中判断存在，会比列表和元组效率更高！集合在这方面做了优化

print('')
print('3----------------')
print('1' in num_list)

#集合还有一个非常有用的功能，就是可以快速确定他们与其他集合共享或不共享哪些值
#我们使用intersection函数来进行查找共享的值

print('')
print('4----------------')
numa_list = {'1','2','3','4'}
numb_list = {'1','2','33','44'}
print(numa_list.intersection(numb_list))

#想找我有他没有的值，使用difference函数

print('')
print('5----------------')
print(numa_list.difference(numb_list))

#想要合并并且打印使用union函数，注意他会合并且覆盖相同的值

print('')
print('6----------------')
print(numa_list.union(numb_list))

#下面是拓展内容，如何创建空的列表，元组，集合

empty_list = list()
empty_tuple = tuple()
empty_set = set()

#当然还有另一种办法

empty_list = []
empty_tuple = ()
empty_sets = {}#空集合并不能这样创建，这样创建出来的是空字典