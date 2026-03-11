#取名要规范，让别人有阅读你代码的能力是很重要的
#如果想在字符串中打‘符号，可以用双引号或者\来使用

message = 'Hello_World!'

#使用print函数可以直接打印

print('1----------------')
print(message)

#len函数可以读取字符串长度

print('')
print('2----------------')
print(len(message))

#使用索引可精确定位

print('')
print('3----------------')
print(message[0])

#另外一种索引用法，称为切片

print('')
print('4----------------')
print(message[0:5])
print(message[6:11])

#upper和lower可以更改字符串大小写

print('')
print('5----------------')
print(message.upper())
print(message.lower())

#使用count和find可以统计和查找字符

print('')
print('6----------------')
print(message.count('o'))
print(message.find('o'))

#使用replace可以替换字符串中的字符，但是注意它是个返回值函数，并非直接替换

print('')
print('7----------------')
a=message.replace('o','oo')
print(a)
print(message)

#字符串使用+来组合是一种非工程代码常见用法

print('')
print('8----------------')
greeting = 'Hello!'
name = 'Tom'
howdy = greeting + ' ' + name
print(howdy)

#下面两种用法建议养成习惯，在工程类代码中很常见

print('')
print('9----------------')
howdyy = '{},{}.Welcome'.format(greeting,name)
print(howdyy)
howdyyy = f'{greeting},{name}.Welcome'
print(howdyyy)

#使用help了解更多详细内容

print('')
print('10----------------')
print(help(name))
print(help(name.upper()))
