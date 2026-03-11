#上下文管理器打开文件是多数情况下处理文件的方式
#他的好处是允许我们在这个代码块内操作文件，退出代码块后他会自动关闭文件
#使用with关键字来实现
#如果你的文件里有中文，记得用utf-8去读

with open('test.txt','r',encoding='utf-8') as f:
    f_contents = f.read()
    print('1-------------')
    print(f_contents)

    #在用其他方法之前拓展一个知识，python读文件有一个指针
    #因为我们已经读过一次文件了，所以指针指到了末尾，如果我们再读一次文件，他会读不到
    #所以我们可以使用seek函数把指针拉回去

    f.seek(0)

    #还有一个是它的兄弟，tell函数，可以查看当前指针在哪个位置

    print('')
    print('2-------------')
    print(f.tell())

    #如果你要读一个非常大的文件，但不想将文件的所有内容打印出来
    #你可以使用readlines函数

    print('')
    print('3-------------')
    f_reads = f.readlines()
    print(f_reads)#你可以看到他直接平铺在了运行框

    #readline是它的小弟，只能读一行

    print('')
    print('4-------------')
    f.seek(0)#记得指针
    f_read1 = f.readline()
    print(f_read1,end='')

    #下面拓展一个知识，python的print会自动打印换行符，你可以手动设置它
    #使用方法就像这样

    print('')
    print('5-------------')
    print(1,end='')
    print(2)

    #现在我们要解决一个问题，因为read还是readline的读取还是会进入运行内存，进入我们的内存卡
    #我们如果一次性读取整个文件，可能会直接耗尽内存
    #所以我们可以只是简单遍历文件的每一行，使用简单的for循环

    print('')
    print('6-------------')
    f.seek(0)
    for line in f:
        print(line,end='')#对的就是这么简单
    print('')
    #下面我来解释为什么，这样和之前有什么区别？
    #因为这样for循环不会一次性读取文件中的所有内容，所以我们不必担心内存问题
    #他会逐行读取文件每一行，但有时你可能需要更精确地控制读取内容
    #所以下面我们要介绍read函数的参数用法
    #read的参数可以控制一次的读取量

    print('')
    print('7-------------')
    f.seek(0)
    f_contents = f.read(15)
    print(f_contents)#我们打印了前15个字符包括空格

    #这个用法可以跟循环搭配，控制每次读入的字符数量

    print('')
    print('8-------------')
    f.seek(0)
    size_to_read = 10
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents,end='*')#用结束符号可以清除地看到每次读到的内容
        f_contents = f.read(size_to_read)#这行很重要，相当于i--，不然死循环