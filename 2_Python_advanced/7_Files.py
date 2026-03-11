#下面来学习如何对多个文件进行读写操作
#我们将用它来复制test文件,你可以先删除test2文件避免混淆
#下面我们来看如何操作

with open("test.txt","r") as rf:
    #没错with也是可以嵌套的
    with open("test_copy.txt", "w") as wf:
        #接下来要怎么做呢？其实非常简单，无脑for循环
        for line in rf:
            wf.write(line)
        #首先我们打开了原始文件，然后创建了复制文件
        #然后通过for循环逐行搬运原始文件到复制文件
        #运行之后你可以发现复制的文件和test文件一模一样

#当然我们还可以复制照片
#方法换汤跟换点小药，但是你得先准备一个照片在目录
#因为他们一个是文档一个是照片他们不是一个类型
#但是在二进制里人人都是一个样
#所以我们需要以二进制模式打开这些文件
#直接二进制读写字节，而不是单纯文本复制
#方法就是模式加个'b'
with open("tf.png","rb") as rf:
    with open("tf_copy.png", "wb") as wf:
        for line in rf:
            wf.write(line)
        #你可以发现成功复制了，是不是很不神奇

#你也可以使用while循环+增大读取来牺牲内存加快复制速度
with open("tf.png","rb") as rf:
    with open("tf_copy2.png", "wb") as wf:
        chunk_size = 1024
        f_read = rf.read(chunk_size)
        while len(f_read) > 0:
            wf.write(f_read)
            f_read = rf.read(chunk_size)#一定要记得这行，不然会死循环无限写