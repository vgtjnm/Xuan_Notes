import java.util.Scanner;
import java.util.Random;

public class Main {

    //#08
//    public static boolean is_Prime(int num) {
//        for (int i = 2; i < num; i++) {
//            if (num % i == 0) return false;
//        }
//        return true;
//    }

    public static void main(String[] args){

        //#01
//        int num = 5;
//        double dnum = 3.14;
//        boolean is_true = true;
//        String str = "Hello!";
//
//        System.out.println(num);
//        System.out.println(dnum);
//        System.out.println(is_true);
//        System.out.println(str);

        //#02
//        Scanner scanner = new Scanner(System.in);
//
//        System.out.println("Enter your name：");
//        String name = scanner.nextLine();
//
//        System.out.println("Enter your age：");
//        int age = scanner.nextInt();
//
//        int time_21 = 2100-age;
//
//        System.out.println("你好，"+name+"!你今年"+age+"岁，");
//        System.out.println(time_21+"年后将迎来2100年。");
//
//        scanner.close();

        //#03
//        Scanner scanner = new Scanner(System.in);
//
//        System.out.printf("Enter your score：");
//        int score = scanner.nextInt();
//        System.out.printf("%n你的等级是：");
//        if(score>=90) System.out.println("A");
//        else if(score>=80) System.out.println("B");
//        else if(score>=70) System.out.println("C");
//        else if(score>=60) System.out.println("D");
//        else System.out.println("F");
//
//        scanner.close();

        //java中的Switch新写法

//        switch (day) {
//            case 1 -> System.out.println("Monday");
//            case 2 -> System.out.println("Tuesday");
//            case 3 -> System.out.println("Wednesday");
//            default -> System.out.println("Other");
//        }

        //#04
//        Scanner scanner = new Scanner(System.in);
//
//        System.out.println("跟据今天的星期输入1-7：");
//        int week = scanner.nextInt();
//
//        switch (week) {
//            case 1 -> System.out.println("星期一");
//            case 2 -> System.out.println("星期二");
//            case 3 -> System.out.println("星期三");
//            case 4 -> System.out.println("星期四");
//            case 5 -> System.out.println("星期五");
//            case 6 -> System.out.println("星期六");
//            case 7 -> System.out.println("星期七");
//            default -> System.out.println("你是外星人？");
//        }
//
//        scanner.close();

        //#05
//        for(int i=1;i<=9;i++){
//            for(int j=1;j<=9;j++){
//                int result = i*j;
//                System.out.printf(i+"x"+j+"="+result+"\t");
//            }
//            System.out.println("");
//        }


        //#06
//        Scanner scanner = new Scanner(System.in);
//        Random random = new Random();
//
//        int times = 0, number = random.nextInt(1,100);
//        while(true){
//            times++;
//            System.out.println("猜个数字：");
//            int num = scanner.nextInt();
//            if(num>number) System.out.println("大了");
//            else if(num<number) System.out.println("小了");
//            else{
//                System.out.println("恭喜猜对！");
//                System.out.println("你一共猜了"+times+"次。");
//                break;
//            }
//        }
//
//        scanner.close();

        //java的声明数组：
//        int[] arr = new int[5];          // 声明固定大小
//        int[] arr = {1, 2, 3, 4, 5};    // 初始化

        //#07
//        Scanner scanner = new Scanner(System.in);
//
//        double[] nums = new double[5];
//        double max_num=0,min_num=0,avg_num=0;
//        for(int i=0;i<5;i++){
//            System.out.println("Enter a number:");
//            nums[i] = scanner.nextDouble();
//            avg_num+=nums[i];
//            if(i==0){
//                max_num=nums[i];min_num=nums[i];
//            }
//            else{
//                if(nums[i]>max_num) max_num = nums[i];
//                if(nums[i]<min_num) min_num = nums[i];
//            }
//        }
//
//        avg_num/=5;
//        System.out.println("最大值是："+max_num);
//        System.out.println("最小值是："+min_num);
//        System.out.println("平均值是："+avg_num);
//
//
//        scanner.close();

        //java的函数这样写：
        // 无参数，无返回值
//        public static void sayHello() {
//            System.out.println("Hello!");
//        }
//
//        // 有参数，有返回值
//        public static int add(int a, int b) {
//            return a + b;
//        }
//
//        // 多个参数
//        public static double average(double a, double b, double c) {
//            return (a + b + c) / 3;
//        }
//
//        public static void main(String[] args) {
//            sayHello();                        // 调用
//            int result = add(3, 5);           // result = 8
//            double avg = average(1, 2, 3);    // avg = 2.0
//        }


        //#08
        //函数写在上面了

//        System.out.println("1-50之间的质数有：");
//        for(int i=2;i<=50;i++){
//            if(is_Prime(i))
//                System.out.println(i);
//        }

    }
}
