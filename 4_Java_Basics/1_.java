public class Main {

    public static void main(String[] args){

        //之前学过C++的简单语法来写算法题所以看到Java的一些相似的东西还是蛮亲切的
        //不过听说Java有很多复杂的特性，没关系会慢慢攻克的

        //首先就是注释变成了"//"不是"#",多行注释用"/* 内容 */"，单字符用''，字符串用""

        //输出的话就是System.out.print(内容);->要加分号
        System.out.print("I like apple!");

        //想从下一行开始输出就要给print加上ln变成println
        //println会在输出结束时输出换行符，而不是开始前
        //如果前面没有换行那么就需要输入"\n"去手动换行
        System.out.println("\nI like banana!");

        //在Intellij这个IDE里打出sout+tab可以快速打出"System.out.println"
        System.out.println("sout+tab可以快速打出System.out.println");

        //下面是Java中变量的定义，跟C++还是有点类似的

        //首先是整型，还是熟悉的int，不直接使用的情况下可以先不声明，这时值是不确定的，不能直接使用
        int a,b=1;

        //Java的变量和字符串输出跟C++有些不同
        System.out.println("b的值是:"+b);

        //double是双精度，跟C++一样
        double pai = 3.1415926;

        System.out.println("π的值是"+pai+"...");

        //char是字符类型，只能存储一个字符，记得要用单引号

        char c = 'a';

        System.out.println("c的值是"+c);

        //在Java里bool是boolean

        boolean is_phone = true;
        boolean is_num = false;

        System.out.println("这个手机号对了吗？结果是"+is_phone);

        //String是字符串类型

        String str = "这是个字符串";

        System.out.println(str);

        //判断的话还是if，个人感觉跟C++差不多

        boolean is_boy = true;

        if(is_boy){
            System.out.println("是个男孩");
        }
        else{
            System.out.println("是个女孩");
        }

    }
}
