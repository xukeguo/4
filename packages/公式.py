#欢迎使用Python脚本编辑器！我的一小步，人类一大步！
#@File    :   公式.py
#@Time    :   2022/04/23 10:18:48
#@Author  :   flow-laic 
#@Email   :
#*求解方程exp(x) + 10*x - 2 = 0首先根据李普希茨条件估计出迭代的次数

from math import*
def ite(x,k):
    if k!=0:
        return ite((2-exp(x))/10,k-1)
    else:
        return x
x=ite(0,12)
print(x)

a=5
print(bin(a))
#一百个不同类型的C语言趣味编程题 单位换算在此
#1.编写一个程序，输入一个整数，输出该整数的二进制表示。  例如：输入：5，输出：101  输入：10，输出：1010
def mybin(x):
    if x==0:
        return 0
    else:
        return x%2+10*mybin(x//2)
print(mybin(5))
#2.编写一个程序，输入二进制表示，输出该整数的十进制表示。 例如：输入：101，输出：5  输入：1010，输出：10
def mydecwhitbin(x):
    if x==0:
        return 0
    else:
        return x%10+2*mydecwhitbin(x//10)#2*dec(x//10)是为了把每一位的值乘以2，然后再相加
print(mydecwhitbin(100))
#输入一个整数，输出该整数的八进制表示。 例如：输入：16，输出：20
def myoct(x):
    if x==0:
        return 0
    else:
        return x%8+10*myoct(x//8)#10*oct(x//8)是为了把每一位的值乘以8，然后再相加
print(myoct(10))
#5.编写一个程序，输入一个整数八进制表示，输出该整数的十进制表示。 例如：输入：10，输出：8
def mydecwhitoct(x):
    if x==0:
        return 0
    else:
        return x%10+8*mydecwhitoct(x//10)
print(mydecwhitoct(20))
'''#6.编写一个程序，输入一个整数十进制表示，输出该整数的十六进制表示。 例如：输入：20，输出：14
def myhex(x):
    if x==0:
        return 0
    else:
        return x%16+10*myhex(x//16)
print(myhex(30))
#7.编写一个程序，输入一个整数十六进制表示，输出该整数的十进制表示。 例如：输入：14，输出：20
def mydecwithhex(x):
    if x==0:
        return 0
    else:
        return x%10+16*mydecwithhex(x//10)
print(mydecwithhex(14))'''
#4.第六题迭代求一元三次方程的根。 方程为：ax**3 + bx**2 + cx + d = 0,系数a,b,c,d由主函数输入。
def solv():
    a=int(input("请输入系数a:"))
    b=int(input("请输入系数b:"))
    c=int(input("请输入系数c:"))
    d=int(input("请输入系数d:"))
    x0=float(input("请输入初始值x0:"))
    x = x0

    i =1 #随机定义一个i的值，是其能够进入while循环语句
    while i >= 1e-5: #（1e-5 = 10**-5）
     x0 = x #用所得的x代替x0原来的值
     f = ((a*x0+b)*x0+c)*x0 +d #f用来描述方程的值

     fd = (3*a*x0 + 2*b)*x0 +c #fd用来描述方程求导之后的值

     x = x0 - f/fd #求得更接近方程根的x的值

     i = abs(x - x0)

    #print("第%d次迭代，x的值为：%f" %(i,x))

    print('方程的一个根为：{:7f}'.format(x)) #format的格式化输出，输出保留7位小数的浮点数。
solv()

'''解本问题有多种方法，此方法并不是标准答案，读者可以自己尝试各种方法

问题分析：

​牛顿迭代法是取x0之后，在这个基础上，找到比x0更接近的方程的根，一步一步迭代，从而找到更接近方程的近似根。

​设r是f(x)=0的根，选取x0作为r的初始近似值。过点（x0, f(x0))作为曲线y = f(x)的切线L，L的方程为y = f(x0) +f‘(x0)(x-x0)，
求出L于x轴交点的横坐标x1 = x0 -f(x0)/f’(x0)，称x1为r的一次近似值，过点（x1, f(x1))作为曲线y = f(x)的切线并求改切线于x轴的横坐标x2 = x1 -f(x1)/f’(x1)，
称x2为r的二次近似值，重复以上过程，得r的近似值xn。上述即为牛顿迭代法的求解过程。

​算法设计：

在1附近找任意一实数作为x0的初值，我们去1.5，即x0 = 1.5.

用初值x0带入方程中计算此时的f(x0)及f'(x0)；程序中f用来描述方程的值，fd用来描述方程求导之后的值。

计算增量h=f/fd。

计算下一个x （x = x0-h）。

用所得的x代替x0原来的值。

若|x - x0|>=1e-5,则转到第三步继续执行，否则转到步骤7

所求x就是方程的根，将其输出。'''
#5.迭代求一元二次或三次方程的根。 方程为：ax**3 + bx**2 + cx + d = 0,系数a,b,c，d由主函数输入。
def solv():
   a=int(input("请输入系数a:"))
   b=int(input("请输入系数b:"))
   c=int(input("请输入系数c:"))
   d=int(input("请输入系数d:")) 
   if (c**2-4*b*d)<0:
         print("此方程无解")
         return None
   for j in range(2):
        if j==0:
          x = -c/(2*b)+1e-5
         
          i =1
          while i >= 1e-5:
           x0 = x
           f = ((a*x0+b)*x0+c)*x0 +d
           fd = (3*a*x0 + 2*b)*x0 +c
           x = x0 - f/fd
           i = abs(x - x0)
          print('方程的一个根为：{:7f}'.format(x))
        else:
            x = -c/(2*b)-1e-5
            i=1
            while i >= 1e-5: #（1e-5 = 10**-5）
             x0 = x#用所得的x代替x0原来的值
             f = ((a*x0+b)*x0+c)*x0 +d #f用来描述方程的值

             fd = (3*a*x0 + 2*b)*x0 +c #fd用来描述方程求导之后的值

             x = x0 - f/fd #求得更接近方程根的x的值

             i = abs(x - x0)
            print('方程的一个根为：{:7f}'.format(x))
solv()
#人工智能   公式   
#人脸识别
#人脸识别是一种自然语言处理技术，它可以自动检测出人脸，并且可以自动检测出人脸的属性，如年龄、性别、颜色、脸型等。
#人脸识别代码
#抛物线和斜线交点坐标 列方程式 两边分别是  X的表达式，求解就可了

def myhex(x):
    if x==0:
        return 0
    else:
        return 3+40*myhex(x//10)
print('dddddd',e
