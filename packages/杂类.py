

#from email.headerregistry import Address
#from sys import flags
#from typing import Dict


from datetime import date, datetime
from logging.config import dictConfig
from pickle import DICT

from money import fib


print
#hfghfghfghfghfghghh
print ("f")

print ((5**2)**2)
print(9+6)

555555
print(9-3)
class a:
    def __init__(self):
        print("a")
''' def __init__(self,a):
        print(a)'''
    
   
a1=a()
a2=a()
a3=a()
a4=a()
a5=a()
a2
a1
a3
a4
a5
dir(a1)
a




a=int(input('请输入：'))
if a==1:
   pass
elif a==2:
    pass
elif a==3:
    pass
else:
    pass
#range()函数
i=range(1,10) #range(start,stop,step)
print(i)
print(list(i))
for i in range(1,10):
    print(i)
i=range(1,10,2)
for j in i:
    print(j)
#while循环
i=0 #初始化循环变量 
num_a=0  #初始化工作变量
while i<101: #循环条件
  num_a+=i #工作变量的操作（表达式）
  i+=1     #循环变量操作与定义（表达式），   循环变量的操作（表达式）与工作变量的操作（表达式）统称为循环体
print(num_a)  #循环结束后执行
#break
i=0
while i<10:
    print(i)
    i+=1
    if i==5:
        break
#continue
i=0
while i<10:
    i+=1
    if i==5:
        continue
    print(i)
#pass
i=0
while i<10:
    i+=1
    if i==5:
        pass
    print(i)
#for循环
for i in range(1,10):
    print(i)
#for循环
for i in range(1,10,2):
    print(i)
#for循环
for i in range(1,10,2): #多重定义，变化赋值
    print(i) 
    #累加
sum1=0
for i in range(2,101,2):
 sum1+=i #sum=sum+i sum1实现了迭代累加（累积）
print(sum1)  #2550
#累加
sum2=0
for i in range(1,101,2):
 sum2+=i
print(sum2)  #2500
sum3=sum1+sum2
print(sum3)  #5050
#累加偶数
i=0   #初始化循环变量
sum4=0  #初始化工作变量
while i<101:     #循环条件
 if i%2==0: #i%2!=0 求奇数
  sum4+=i   #sum4=sum4+i
 i+=1
print(sum4)  #2550
#累加偶数
i=0
sum5=0
while i<101:
 if not bool(i%2!=0): #bool()函数，返回值为True或False 不加not取反,求奇数
  sum5+=i
 else:
  pass
 i+=1
print(sum5)  #2550
 #累加奇数
i=0
sum6=0
while i<50:

        sum6+=i*2+1 #sum6=sum6+i*2 求偶数
    
    
        i+=1
print(sum6)  #2500
#for循环

for _ in range(1,10):
    print("hello")
for i in 'hello':
    print(i,end="\t")
#for循环
for i in [1,2,3,4,5]:
    print(i)
#打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()
#打印水仙花数
for i in range(100,1000,1):#初始为100，终止为1000，步长为1
    a=i//100 #取百位数
    b=i%100//10#//取整除法（i//10%10）
    c=i%10  #取个位数
    if i==a**3+b**3+c**3:
        print(i)

#打印水仙花数
#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()#换行
#1到1000的质数
for i in range(2,1000):
    for j in range(2,i):
        if i%j==0:
            break #跳出循环
    else:
     print(i)


#打印1到100的偶数
for i in range(1,100):
    if i%2!=0:
        pass   
    else:
        print(i)
#打印1到100的奇数
for i in range(1,100):
    if i%2==0:
        continue#跳出本次循环
    else:
        print(i)
#for 循环 列表 元组 字典 字符串 其他 
#for循环
for i in [1,2,3,4,5]:#列表
    print(i)

#for循环元组
for i in (1,2,3,4,5):#元组
    print(i ,end="\t")

#for循环字典
for i in {'name':'zhangsan','age':18}:#字典
    print(i)
    #for循环字符串
for i in "hello":#字符串
    print(i)
#for循环其他
for i in range(1,10):
    print(i)
    
#1到100的质数的个数
sum=0
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum+=1  
print(sum)

# 解锁
# 判断用户输入的密码是否正确
# 如果正确，则输出“登录成功”
# 如果不正确，则输出“密码错误”
# 如果用户输入的密码错误超过三次，则输出“账户锁定”
# 如果用户输入的密码正确，则输出“登录成功”
inpu = input("请输入密码：")
if inpu == "123456":
    print("登录成功")
else:
    print("密码错误")
    inpu = input("请输入密码：")
    if inpu == "123456":
        print("登录成功")
    else:
        print("密码错误")
        inpu = input("请输入密码：")
        if inpu == "123456":
            print("登录成功")
        else:
            print("密码错误")
            inpu = input("请输入密码：")
            if inpu == "123456":
                print("登录成功")
            else:
                print("密码错误")
                inpu = input("请输入密码：")
                if inpu == "123456":
                    print("登录成功")
                else:
                    print("密码错误")
                    inpu = input("请输入密码：")
                    if inpu == "123456":
                        print("登录成功")
                    else:
                        print("密码错误")
                        inpu = input("请输入密码：")
                        if inpu == "123456":
                            print("登录成功")
                        else:
                            print("密码错误")
                            inpu = input("请输入密码：")
                            if inpu == "123456":
                                print("登录成功")
                            else:
                                print("密码错误")
                                inpu = input("请输入")
      
#1.编写程序，输入一个数字，判断这个数字是否是素数（质数）。
inpu = int(input("请输入一个数字："))
for i in range(2,inpu):
    if inpu%i==0:
        print("不是素数")
        break #跳出循环
else:
     print("是素数")
#包含1到100的质数的集合
dict={}
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
            ge = i#获取质数
            dict[ge]=ge
print(dict)
#1到100的质数的和
sum=0
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum+=i
print(sum)
#1到100的质数的和
sum=0
for i in dict:
  sum+=i
print(sum)
#三次输入密码，如果密码正确，则输出“登录成功”，如果密码错误，则输出“密码错误”，如果密码错误超过三次，则输出“账户锁定”
pwb = input("请输入密码：")
for i in range(3):
    if pwb == "123456":
        print("登录成功")
        break
    elif i == 2:
        print("账户锁定")
    else:
        print("密码错误")
        pwb = input("请输入密码：")
print("账户锁定")
#三 次输入密码，如果密码正确，则输出“登录成功”，如果密码错误，则输出“密码错误”，如果密码错误超过三次，则输出“账户锁定”
pwb = input("请输入密码：")
for i in range(3):  
    if pwb == "123456":
        print("登录成功")
        break
    else:
        print("密码错误")
        pwb = input("请输入密码：")                          
print("账户锁定")
#1到50中5的倍数的和
sum=0
for i in range(1,51):
    if i%5==0:
        sum+=i
print(sum)
#1到50中5的倍数的和
sum=0
for i in range(1,51):
    if i%5!=0:
        continue#结束本次循环
    else:
        sum+=i
print(sum)
#三次输入密码，如果密码正确，则输出“登录成功”，如果密码错误，则输出“密码错误”，如果密码错误超过三次，则输出“账户锁定”
pwb = input("请输入密码：")
for i in range(3):
    if pwb == "123456":
        print("登录成功")
        break#跳出循环
    else:
        print("密码错误")
        pwb = input("请输入密码：")
        
else:
    print("账户锁定")   

    
#创建一个字典，存储学生信息，包括姓名、年龄、成绩，并且要求每个学生的信息都不能重复。
dict={}
while True:#循环录入信息
    name = input("请输入姓名：")
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    Addres=input("请输入地址：")
    dict[name]=[age,score,Addres]
    inpu = input("是否继续（y/n）")
    if inpu == "n":
        break
    inpu = input("是否继续（y/n）：")
    if inpu == "n":
        break
print(dict)
#创建一个字典，存储学生信息，包括姓名、年龄、成绩，并且要求每个学生的信息都不能重复。
dict1={}
name1=input("请输入1姓名：")
name2=input("请输入2姓名：")
name3 = input("请输入3姓名：")
age1=int(input("请输入1年龄："))
age2=int(input("请输入2年龄："))
age3=int(input("请输入3年龄："))
dict1['name']=[name1,name2,name3]
dict1['age']=[age1,age2,age3]
print(dict1)

str1 = "abcdefg"
str2 = str1.upper()

#格式化 花名册     证明                 
name=input(' 请输入姓名：')
age=int(input(' 请输入年龄：'))
score=int(input(' 请输入成绩：'))
print('%s的年龄是%10.3d,成绩是%d'%(name,age,score))
print('{}的年龄是{},成绩是{}'.format(name,age,score))
print('{0}的年龄是{1},成绩是{2}'.format(name,age,score))
print('{name}的年龄是{age},成绩是{score}'.format(name=name,age=age,score=score))
print(f'{name}的年龄是{age},成绩是{score}')
print('{0:>10}的年龄是{1:>10.3f},成绩是{2:>10}'.format(name,age,score))

 


  #7.编写程序，计算圆周        另一种写法
import math
r=float(input('请输入半径：'))
area=math.pi*r*r
print('半径为{}的圆的面积是{}'.format(r,area))
print('半径为{0}的圆的面积是{1}'.format(r,area))
print('半径为{0:.2f}的圆的面积是{1:.2f}'.format(r,area))
  #7.编写程序，

    
#找数列 最大数
list1=[1,5,5,9,11,88,102]
sum=-100#若干小
for i in list1:
    if i> sum:
        sum=i
print(sum)
#找数列 最小数
list1=[1,5,5,9,11,88,102]
sum=1000#若干大
for i in list1:
    if i< sum:
        sum=i
print(sum)



class Foo(object):

    


    def __init__(self, price):
        self.price = price

    def how_much_of_book(self, n):
        print(self)
        return self.price * n

#导入模块

l=[1,2,3,4,5]
l2=[6,7,8,9,10]
l.extend((11,12,13))
print(l)
l3=l+l2
print(l3)

class a:
    def __new__(cls, *args,**kwargs):
        print('new')
        global a2
        global a4
        a4=super().__new__(cls)
        a2=super().__new__(cls)
        return a2
    def __init__(self, a,b):

        self.na=a
        self.b=b
    def name(self):
        print(self.na)

a1=a(3,8)
a3=a(4,5)
print(type(a1),type(a2),type(a4))
print((a2.b))
print(a2.name())

        
  






























































































































































































































































































  #练习                                       
    #1.编写程序，输入一个整数，输出该整数的阶乘
a=int(input('请输入一个整数：'))
b=1
for i in range(1,a+1):
        b=b*i
print(b)
    #2.编写程序，输入一个整数，输出该整数的绝对值
a=int(input('请输入一个整数：'))
if a>=0:
    print(a)
else:
    print(-a)
    #3.编写程序，输入一个整数，输出该整数的绝对值
a=abs(float(input('请输入一个整数：')))
print(a)
    #4.编写程序，输入一个整数，输出该整数的绝对值  另一种写法             
a=int(input('请输入一个整数：'))
print(abs(a))   
    #5.编写程序，输入一个整数，输出该整数的绝对值  另一种写法   
    #6.编写程序，计算圆周率π的值 另一种写法  

       
import math
a=math.pi
print(a)
    #7.编写程序，计算圆周  另一种写法


'''
@File    :   3.py
@Time    :   2022/04/19 23:14:25
@Author  :   flow-laic 
'''# coding=utf-8
# 编写计算圆周率的程序      可以使用math库

from unicodedata import name

s = 3.14


def pi(n):  # 定义函数
    s = 0
    for i in range(n):
        s += 1 / pow(16, i) * (4 / (8 * i + 1) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6))
    return s  # 返回值,调用函数得到s的值


n = int(input('圆周率的多边形值:'))  # 调用
pi(n)  # 调用
print(s)  # 3.14,自定义函数的返回值不更改S的值
print(pi(n))  # 3.141592653589793,调用函数的返回值
print("%.100f" % pi(n))  # 输出精确到小数点后位
print("%.100f" % (1 / 3))  # 输出精确到小数点后位


# 自己定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-10))


# 自己定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):  # 判断x是否为整数或浮点数
        raise TypeError('bad operand type')  # 抛出异常
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-10))


# 自己定义函数
def my1(x):  # 不可变参数
    global n1  # 全局变量
    n1 = list(n)  # 将n转换为列表
    for i in x:
        n1.send(i)  # 添加
    return n1  # 返回


m = [1, 5, 9, 44]
n = list(m)
print(my1(m))
print(n)
print(m)
print(n1)


# 自己定义函数
def my2():  # 不带参数
    return 'hello world'


print(my2())


# 自己定义函数  可变参数 可以传入0个或多个参数 参数类型可以不同 不能传入关键字参数 不能传入可变参数 不能传入不可变参数 不能传入字典   可以传入关键字参数 可以传入可变参数  可以传入不可变参数  可以传入字典
def my3(a, b=100):  # 带默认值的参数
    return a + b


print(my3(10))
print(my3(10, 20))


# 自己定义函数
def myfun(*args):  # 可变参数
    sum = 0
    for i in args:
        sum += i
    return sum


print(myfun(1, 2, 4, 5))


# 自己定义函数
def myfun(**kw):  # 关键字可变参数
    print(kw)


print(myfun(name='zhangsan', age=18, score=100))


# 自己定义函数
def myfun1(*a, **b):  # 可变参数与关键字参数 可以同时使用 可变参数必须在关键字参数之前 关键字参数必须在可变参数之后
    print(a)
    print(b)


myfun1(1, 2, 3, 4, 5, name='zhangsan', age=18, score=100)
print(myfun1(1, 2, 3, 4, 5, name='zhangsan', age=18, score=100))
# 自己定义函数
# 字典的使用的查找  字典的使用的添加  字典的使用的删除  字典的使用的修改
dict1 = {'name': 'zhangsan', 'age': 18, 'score': 100}
print(dict1['name'])
print(dict1['age'])
print(dict1['score'])
dict1['name'] = 'lisi'
print(dict1['name'])
# 输出字典中的包含某个值的所有键  
print(dict1.keys())
# 输出字典中的包含某个值的所有值
print(dict1.values())
# 输出字典中包含的某键值的对应键
# print字典中包含的某键值的对应键
# 输出字典中键值最小的键值对
dict = {'LiSi': 9, 'waiwu': 5, 'lili': 5}
for x, y in dict.items():
    if x == min(dict, key=dict.get):  # 判断x是否在字典中
        min_sum = y
for x, y in dict.items():
    if y == min_sum:
        print(x, y)
# 输出字典中键值最大的键值对
dict = {'LiSi': 9, 'waiwu': 5, 'lili': 5, 'wangwu': 8, 'zhaoliu': 9}
for x, y in dict.items():
    if x == max(dict, key=dict.get):  # 判断x是否在字典中
        min_sum = y
for x, y in dict.items():
    if y == min_sum:
        print(x, y)

list(dict.keys())[list(dict.values()).index('张三')]  # 输出字典中包含的某键值的对应键
# 根据最小值返回对应的键
dict = {2: 1, 3: 9, 4: 5}
min(dict, key=dict.get)


# 根据最大值返回对应的键
dict = {2: 1, 3: 9, 4: 5}
max(dict, key=dict.get)
# 找出所有键值为男性的键对
persons = {'ZhangSan': 'male',
           'LiSi': 'male',
           'WangHong': 'female'}
males = filter(lambda x: 'male' == x[1], persons.items())
for (key, value) in males:
    print('%s : %s' % (key, value))

'''输出如下：

LiSi : male

ZhangSan : male

注意：

字典中的value不保证唯一性，因此根据值查出来的是一个list.

不过字典中key的值是唯一的，因此根据key将可以查到唯一的一个value'''

print('李四的性别: %s' % persons['LiSi'])

'''输出如下

李四的性别: male'''
#欢迎使用Python脚本编辑器！我的一小步，人类一大步！
#@File    :   8.py
#@Time    :   2022/04/20 15:09:15
#@Author  :   flow-laic 
#@Email   :
from email import header
import demo
demo.f()
import math
print(dir(math)) #查看模块的方法
import builtins
print(dir(builtins)) #查看内建模块的方法 
#查看模块的方法

import builtins
print(dir(builtins))#查看内建模块的方法
import os
os.system('/System/Applications/Calculator.app/Contents/MacOS/Calculator')
os.system('/Applications/WeChat.app/Contents/MacOS/WeChat')
os.getlogin()#返回当前登录用户名
os.system('dir')
os.aborter()#终止当前进程
os.system()#执行命令
os.access()#检查文件是否可访问
os.chdir()#改变当前工作目录
os.chmod()#修改文件的权限
os.chown()#修改文件的所有者
os.close()#关闭文件 
os.closerange()#关闭所有文件
os.dup()#复制文件句柄
os.dup2()#复制文件句柄
os.fchdir()#通过文件句柄改变当前工作目录
os.fchmod()#修改文件的权限
os.fchown()#修改文件的所有者
os.fdatasync()#同步文件数据
os.fstat()#返回文件状态
os.fsync()#同步文件数据
os.ftruncate()#截断文件
os.getcwd()#返回当前工作目录
os.getcwdu()#返回当前工作目录
os.getegid()#返回当前进程的用户组ID
os.geteuid()#返回当前进程的用户ID
os.getgid()#返回当前进程的组ID
os.getgroups()#返回当前进程的组列表
os.getlogin()#返回当前登录用户名
os.getpgid()#返回一个进程组的ID
os.getpgrp()#返回当前进程组ID
os.getpid()#返回当前进程ID
os.getppid()#返回当前进程的父进程ID
os.getresuid()#返回当前进程的运行时用户ID
os.getresgid()#返回当前进程的运行时组ID
os.getrlimit()#返回进程的资源限制
os.initgroups()#初始化组
os.isatty()#检查文件是否是一个终端设备
os.kill()#结束进程
os.killpg()#结束进程组
os.lchown()#修改文件的所有者
os.link()#创建硬链接
os.listdir()#返回指定目录下的文件和目录名
os.lseek()#设置文件指针位置
os.lstat()#返回文件状态
os.major()#返回设备的主设备号
os.makedev()#创建一个设备号
os.minor()#返回设备的次设备号
os.mkdir()#创建目录
os.mknod()#创建一个名字符设备文件（包括字符、块设备、管道）
os.open()#打开一个文件，用于读写
os.openpty()#打开一个新的伪终端
os.pathconf()#返回相关文件的系统配置信息
os.pipe()#创建一个管道
os.popen()#打开一个命令行程序，用于读写
os.read()#从文件读取数据
os.readlink()#返回软链接所指向的文件
os.remove()#删除一个文件
os.rename()#重命名文件或目录
os.renames()#递归地对目录进行更名
os.rmdir()#删除目录
os.setegid()#设置进程的用户组ID
os.seteuid()#设置进程的用户ID
os.setgid()#设置进程的组ID
os.setgroups()#设置进程的组列表
os.setpgid()#设置进程组ID
os.setpgrp()#设置进程组ID
os.system()#执行系统命令
os.symlink()#创建软链接
os.tcgetpgrp()#返回一个进程组的ID
os.tcsetpgrp()#设置一个进程组的ID
os.tempnam()#返回一个指定目录的临时文件名
os.tmpfile()#返回一个打开的模式为(w+b)的文件对象
os.tmpnam()#返回一个打开的模式为(w+b)的文件对象
os.ttyname()#返回一个文件的终端设备名
os.unlink()#删除文件
os.utime()#设置访问和修改时间
os.wait()#等待子进程结束
os.wait3()#等待子进程结束，并返回一个元组
os.wait4()#等待子进程结束，并返回一个元组
os.write()#向文件写入数据
os.dup()#复制文件描述符
os.dup2()#复制文件描述符
os.fstat()#返回一个文件的状态
os.lstat()#返回文件状态，和stat()相同，但是没有软链接
os.mkfifo()#创建命名管道，在UNIX中也可以创建特殊的管道文件
os.openpty()#打开一个新的伪终端
os.pipe()#创建一个管道
os.popen()#打开一个命令行程序，用于读写
os.read()#从文件读取数据
os.write()#向文件写入数据
os.fdopen()#打开一个文件描述符，用于读写

import os
#path1=os.path.abspath('text.txt')# 返回当前目录的绝对路径
#path2=os.path.split(path1)# 将一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
#print(path1)
lis=os.listdir('/Users/xkg/Documents/GitHub')# 返回指定的文件夹包含的文件或文件夹的名字的列表')
print(lis)
#os.path.isdir()# 如果path是一个存在的目录返回true，否则返回false
#os.path.isfile()# 如果path是一个存在的文件，返回true。否则返回false
#os.path.exists()# 如果path存在，返回true。否则返回false
#os.path.getsize()# 返回文件大小，如果文件不存在则返回错误
#os.path.getatime()# 返回最后一次进入文件系统的时间
#os.path.getmtime()# 返回最后一次修改文件的时间
#os.path.getctime()# 返回文件系统上的文件创建时间
#os.path.getsize()# 返回文件大小，如果文件不存在则返回错误
#os.path.isabs()# 如果path是绝对路径，返回true。否则返回false
#os.path.isfile()# 如果path是一个存在的文件，则返回true。否则返回false
path3=os.getcwd()# 返回当前工作目录
lis2=os.listdir(path3)# 返回指定的文件夹包含的文件或文件夹的名字的列表
print(lis2)
for file in lis2:
    if file.endswith('.py'):
        print(file)
#os.path.join()# 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.normpath()# 当path以//或C:开头时，返回正确的路径，其他情况下不做转换
# os.path.realpath()# 返回path的真实路径，规范化路径名，并解析或查看规范化路径的符号链接
# os.path.relpath()# 返回path相对于other的相对路径
# os.path.split()# 将path分割成目录和文件名二元组返回
# os.path.splitext()# 将path分割成目录和扩展名两元组返回
# os.path.splitdrive()# 将path分割成目录和文件路径二元组返回
# os.path.basename()# 返回path最后的文件名  
#os.path.dirname()# 返回path的目录。其实就是把最后一个目录分隔符'\'或斜杠'/'去掉
#os.path.commonprefix()# 返回path列表中第一个出现的目录前缀
#os.path.expanduser()# 将path中包含的"~"和"~user"转换成用户目录
#os.path.expandvars()# 将path中包含的"$name"转换成环境变量
#os.path.isabs()# 如果path是绝对路径，返回true。否则返回false

a1=os.path.splitdrive('/Applications/WeChat.app/Contents/MacOS/WeChat')# 将path分割成目录和文件路径二元组返回
print(a1)
a2=os.path.splitext('/Applications/WeChat.app/Contents/MacOS/WeChat')# 将path分割成目录和扩展名两元组返回
import os.path
print (os.path.abspath( 'demol3.py'))# 返回path规范化的绝对路径
print (os.path.exists ('demol3.py'), os. path. exists (' demo18. py'))# 如果path存在，返回true。否则返回false
print (os.path.join('E:\\Python','demo13.py'))
print (os.path.split('E:\\vipython\\chap15\\demo13.py'))#windows下的路径分割
print (os.path.splitdrive('E:/vipython/chap15/demo13.py'))#mac下的路径分割
print (os.path.splitext ( 'demol3.py'))

#取款  
import abc
import bdb
from cmath import e


monry=10000000   #账户余额
print('取款')
s=int(input('请输入取款金额：'))  #取款金额
if s>monry: #如果取款金额大于账户余额
    print('余额不足')   #余额不足
else:#分支  如果取款金额小于账户余额
    monry=monry-s #账户余额减去取款金额
    print('取款成功，余额为：',monry) #取款成功，输出余额
    存款
    print('存款')
    s=int(input('请输入存款金额：'))  #存款金额
    monry=monry+s #账户余额加上存款金额
    print('存款成功，余额为：',monry) #存款成功，输出余额
    #输出
    print('输出')
    print('你好')
    print('你好','你好')

    #输入
    print('输入')





# 取款
# monry=10000000   #账户余额
# print('取款')
# s=int(input('请输入取款金额：'))  #取款金额
# if s>monry: #如果取款金额大于账户余额
#    print('余额不足')   #余额不足
# else:
#   monry=monry-s #账户余额减去取款金额
#  print('取款成功，余额为：',monry) #取款成功，输出余额
#  #取款
#     多分支if-else
score=int(input('请输入分数：'))
if score>=90:
    print('优秀')
elif score>=80:
    print('良好')  
elif score>=70:
    print('中等')
elif score>=60:
    print('及格')
else:
    print('不及格')

         
#     多分支if-else
score=int(input('请输入成绩：'))
if score>=90 and score<=100:
    print('优秀')
elif score>=80 and score<=89:
    print('良好')
    print('良好')
elif score>=70 and score<=79:
    print('中等')
elif score>=60 and score<=69:
    print('及格')
elif score>=0 and score<=59:
    print( '不及格')
else:
    print('输入错误')
    #     多分支if-else
score=int(input('请输入成绩：'))
if 90<=score>=100:
    print('优秀')
elif 80<=score>=89:
    print('良好')
elif 70<=score>=79:
    print('中等')
elif 60<=score>=69:
    print('及格')
elif 0<=score>=59:
    print('不及格')
else:
    print('输入错误')
    #     多分支if-else
    #嵌套if-else
#判断是否为会员
#会员等级
#普通会员
#银牌会员
#金牌会员
#钻石会员
#输入
answer=input('是否为会员?：y/n')
money=float(input('请输入金额：'))
if answer=='y' or answer=='Y':
    if 2000>=money>=1000:
        print('普通会员') #普通会员
    elif  3000>= money>=2000:
        print('银牌会员')
    elif 4000>=money>=3000:
        print('金牌会员')
    elif money>=4000:
        print('钻石会员')
    else:
        print('输入错误')
else:
    print('输入错误')
    #嵌套if-else
#判断是否为会员
answer=input('是否为会员?：y/n')
money=float(input('请输入金额：'))
if answer=='Y' or answer=='y':
    if money>=5000:
        print('钻石会员五折',money*0.5)          
    elif money>=4000:
        print('金牌会员六折',money*0.6)
    elif money>=3000:
        print('银牌会员七折',money*0.7)
    elif money>=2000:
        print('普通会员八折',money*0.8)
    elif money>=1:
        print('普通会员九折',money*0.9)
    else:
        print('普通会员',money)
elif answer=='N' or answer=='n':
    print('普通会员',money)
else:
    print('输入错误')
    #黑白名单
    name=input('请输入姓名：')
    if name in ['张三','李四','王五']:#判断是否为黑名单
        print('黑名单') #黑名单
    else: #不是黑名单
        print('白名单') #白名单
#比较大小
num_a=int(input('请输入第一个数字：'))
num_b=int(input('请输入第二个数字：'))
'''if num_a>num_b:
    print('第一个数字大')
elif num-a<num-b:
    print('第二个数字大')
else:
    print('两个数字相等')
print('程序结束')'''
#比较大小
num_a=int(input('请输入第一个数字：'))
num_b=int(input('请输入第二个数字：'))
print('第一个数字大' if num_a>num_b else '两个数字相等' if num_a==num_b else '第二个数字大')
print (num_a>num_b and '第一个数字大' or num_a==num_b and '两个数字相等' or '第二个数字大')
print ((num_a,'>',num_b) if num_a>num_b else  (num_a,'=',num_b) if num_a==num_b else (num_a,'<',num_b))
print (str(num_a)+'>'+str(num_b) if num_a>num_b else (num_a,'=',num_b) if num_a==num_b else (num_a,'<',num_b))
print (num_a>num_b and str(num_a)+'>'+str(num_b) or num_a==num_b and str(num_a)+'='+str(num_b) or '第二个数字大')
#素数 逆向思维 
    #素数 逆向思维 判定条件一
dict1={}
for i in range(2,101):
    dict1[i]=True
    for j in range(2,i):
        if i%j==0:
            dict1[i]=False
            break
    else:
        dict1[i]=True 
print(dict1)
    #素数 逆向思维 判定条件二
set1={x for x in range(2,100)}
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
          set1.discard(i)
print(set1)

list1=[]
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        list1.append(i) 
        
print(list1)

       
#素数 正向思维
dict1={}
for i in range(2,101):
    dict1[i]=True 
for i in range(2,101):
    for j in range(i*2,101,i):
      dict1[j]=False
print(dict1)
 #创建一个数列，后面的数字是所有数的和
list1=[1,1,2,3,5,8,13,21,34,55,89, 144, 233, 377, 610, 987, 1597, 2584, 4181]#生成式  列表生成式
list2=[x for x in range(1,101) if x%2==0]#生成式  列表生成式
list3=[x for x in range(1,101) if x%2==1]#生成式  列表生成式
list4=[x for x in range(1,101) if x%2==0 and x%3==0]#生成式  列表生成式
list5=[x for x in range(1,101) if x%2==0 and x%3==0 and x%5==0]#生成式  列表生成式


print(sum(list1))#sum函数可以求和
print(len(list1))#len函数可以求长度
 #创建一个数列，后面的数字是两个数的和
list1=[x+y for x in range(1,101) for y in range(1,x)]#生成式  列表生成式
print(list1)#len函数可以求长度
list2=[x*y for x in range(1,101) for y in range(1,101) if x==y]#生成式  列表生成式
list3=[x*y for x in range(1,101) for y in range(1,101) if x>y]#生成式  列表生成式
list4=[x*y for x in range(1,101) for y in range(1,101) if x>y and x%y==0]#生成式  列表生成式
list1=[1,1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536]#生成式是：
#创建一个数列，后面的数字是两个数的和
list1=[1,1]
for i in range(2,15):
    list1.append(list1[-1]+list1[-2])#索引取值
print(list1)
#创建一个数列，后面的数字的两倍
list1=[1,2]
for i in range(2,7):
    list1.append(list1[-1]*2)#索引取值
print(list1)
#创建一个数列，后面的数字的两倍
list1=['a','b','c','d','e','f']
list2=[1,2,4,8,16,32,64]
dict1={x:y for x,y in zip(list1,list2)}
print(dict1)

#递归函数
def fact(n):
    if n==2:
        return 1
    return 2*fact(n-2)
print(fact(8))

def fact(n):
    return fact_iter(n,2)
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
print(fact(5))

#翡波那契数列
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(10))

list1=[1,1,2]
for i in range(3,10):
    list1.append(list1[-1]+list1[-2])
print(list1)



#from email.headerregistry import Address
#from sys import flags
#from typing import Dict


from datetime import date, datetime
from logging.config import dictConfig
from pickle import DICT

from money import fib


print
#hfghfghfghfghfghghh
print ("f")

print ((5**2)**2)
print(9+6)

555555
print(9-3)
class a:
    def __init__(self):
        print("a")
''' def __init__(self,a):
        print(a)'''
    
   
a1=a()
a2=a()
a3=a()
a4=a()
a5=a()
a2
a1
a3
a4
a5
dir(a1)
a



#00
'''b=open("/Users/xkg/Documents/test.txt", "a+")
print("ggg", file=b)
b.close()
b=open("/Users/xkg/Documents/test.txt", "a+")
print("ggg", file=b)
b.close()'''
#pass用于占位
a=int(input('请输入：'))
if a==1:
   pass
elif a==2:
    pass
elif a==3:
    pass
else:
    pass
#range()函数
i=range(1,10) #range(start,stop,step)
print(i)
print(list(i))
for i in range(1,10):
    print(i)
i=range(1,10,2)
for j in i:
    print(j)
#while循环
i=0 #初始化循环变量 
num_a=0  #初始化工作变量
while i<101: #循环条件
  num_a+=i #工作变量的操作（表达式）
  i+=1     #循环变量操作与定义（表达式），   循环变量的操作（表达式）与工作变量的操作（表达式）统称为循环体
print(num_a)  #循环结束后执行
#break
i=0
while i<10:
    print(i)
    i+=1
    if i==5:
        break
#continue
i=0
while i<10:
    i+=1
    if i==5:
        continue
    print(i)
#pass
i=0
while i<10:
    i+=1
    if i==5:
        pass
    print(i)
#for循环
for i in range(1,10):
    print(i)
#for循环
for i in range(1,10,2):
    print(i)
#for循环
for i in range(1,10,2): #多重定义，变化赋值
    print(i) 
    #累加
sum1=0
for i in range(2,101,2):
 sum1+=i #sum=sum+i sum1实现了迭代累加（累积）
print(sum1)  #2550
#累加
sum2=0
for i in range(1,101,2):
 sum2+=i
print(sum2)  #2500
sum3=sum1+sum2
print(sum3)  #5050
#累加偶数
i=0   #初始化循环变量
sum4=0  #初始化工作变量
while i<101:     #循环条件
 if i%2==0: #i%2!=0 求奇数
  sum4+=i   #sum4=sum4+i
 i+=1
print(sum4)  #2550
#累加偶数
i=0
sum5=0
while i<101:
 if not bool(i%2!=0): #bool()函数，返回值为True或False 不加not取反,求奇数
  sum5+=i
 else:
  pass
 i+=1
print(sum5)  #2550
 #累加奇数
i=0
sum6=0
while i<50:

        sum6+=i*2+1 #sum6=sum6+i*2 求偶数
    
    
        i+=1
print(sum6)  #2500
#for循环
for _ in range(1,10):
    print("hello")
for i in 'hello':
    print(i,end="\t")
#for循环
for i in [1,2,3,4,5]:
    print(i)
#打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()
#打印水仙花数
for i in range(100,1000,1):#初始为100，终止为1000，步长为1
    a=i//100 #取百位数
    b=i%100//10#//取整除法（i//10%10）
    c=i%10  #取个位数
    if i==a**3+b**3+c**3:
        print(i)

#打印水仙花数
#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()#换行
#1到1000的质数
for i in range(2,1000):
    for j in range(2,i):
        if i%j==0:
            break #跳出循环
    else:
     print(i)


#打印1到100的偶数
for i in range(1,100):
    if i%2!=0:
        pass   
    else:
        print(i)
#打印1到100的奇数
for i in range(1,100):
    if i%2==0:
        continue#跳出本次循环
    else:
        print(i)
#for 循环 列表 元组 字典 字符串 其他 
#for循环
for i in [1,2,3,4,5]:#列表
    print(i)

#for循环元组
for i in (1,2,3,4,5):#元组
    print(i ,end="\t")

#for循环字典
for i in {'name':'zhangsan','age':18}:#字典
    print(i)
    #for循环字符串
for i in "hello":#字符串
    print(i)
#for循环其他
for i in range(1,10):
    print(i)
    
#1到100的质数的个数
sum=0
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum+=1  
print(sum)

# 解锁
# 判断用户输入的密码是否正确
# 如果正确，则输出“登录成功”
# 如果不正确，则输出“密码错误”
# 如果用户输入的密码错误超过三次，则输出“账户锁定”
# 如果用户输入的密码正确，则输出“登录成功”
inpu = input("请输入密码：")
if inpu == "123456":
    print("登录成功")
else:
    print("密码错误")
    inpu = input("请输入密码：")
    if inpu == "123456":
        print("登录成功")
    else:
        print("密码错误")
        inpu = input("请输入密码：")
        if inpu == "123456":
            print("登录成功")
        else:
            print("密码错误")
            inpu = input("请输入密码：")
            if inpu == "123456":
                print("登录成功")
            else:
                print("密码错误")
                inpu = input("请输入密码：")
                if inpu == "123456":
                    print("登录成功")
                else:
                    print("密码错误")
                    inpu = input("请输入密码：")
                    if inpu == "123456":
                        print("登录成功")
                    else:
                        print("密码错误")
                        inpu = input("请输入密码：")
                        if inpu == "123456":
                            print("登录成功")
                        else:
                            print("密码错误")
                            inpu = input("请输入密码：")
                            if inpu == "123456":
                                print("登录成功")
                            else:
                                print("密码错误")
                                inpu = input("请输入")
      
#1.编写程序，输入一个数字，判断这个数字是否是素数（质数）。
inpu = int(input("请输入一个数字："))
for i in range(2,inpu):
    if inpu%i==0:
        print("不是素数")
        break #跳出循环
else:
     print("是素数")
#包含1到100的质数的集合
dict={}
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
            ge = i#获取质数
            dict[ge]=ge
print(dict)
#1到100的质数的和
sum=0
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum+=i
print(sum)
#1到100的质数的和
sum=0
for i in dict:
  sum+=i
print(sum)
#三次输入密码，如果密码正确，则输出“登录成功”，如果密码错误，则输出“密码错误”，如果密码错误超过三次，则输出“账户锁定”
pwb = input("请输入密码：")
for i in range(3):
    if pwb == "123456":
        print("登录成功")
        break
    elif i == 2:
        print("账户锁定")
    else:
        print("密码错误")
        pwb = input("请输入密码：")
print("账户锁定")
#三 次输入密码，如果密码正确，则输出“登录成功”，如果密码错误，则输出“密码错误”，如果密码错误超过三次，则输出“账户锁定”
pwb = input("请输入密码：")
for i in range(3):  
    if pwb == "123456":
        print("登录成功")
        break
    else:
        print("密码错误")
        pwb = input("请输入密码：")                          
print("账户锁定")
#1到50中5的倍数的和
sum=0
for i in range(1,51):
    if i%5==0:
        sum+=i
print(sum)
#1到50中5的倍数的和
sum=0
for i in range(1,51):
    if i%5!=0:
        continue#结束本次循环
    else:
        sum+=i
print(sum)
#三次输入密码，如果密码正确，则输出“登录成功”，如果密码错误，则输出“密码错误”，如果密码错误超过三次，则输出“账户锁定”
pwb = input("请输入密码：")
for i in range(3):
    if pwb == "123456":
        print("登录成功")
        break#跳出循环
    else:
        print("密码错误")
        pwb = input("请输入密码：")
        
else:
    print("账户锁定")   

    
#创建一个字典，存储学生信息，包括姓名、年龄、成绩，并且要求每个学生的信息都不能重复。
dict={}
while True:
    name = input("请输入姓名：")
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    Addres=input("请输入地址：")
    dict[name]=[age,score,Addres]
    inpu = input("是否继续（y/n）")
    if inpu == "n":
        break
    inpu = input("是否继续（y/n）：")
    if inpu == "n":
        break
print(dict)
#创建一个字典，存储学生信息，包括姓名、年龄、成绩，并且要求每个学生的信息都不能重复。
dict1={}
name1=input("请输入1姓名：")
name2=input("请输入2姓名：")
name3 = input("请输入3姓名：")
age1=int(input("请输入1年龄："))
age2=int(input("请输入2年龄："))
age3=int(input("请输入3年龄："))
dict1['name']=[name1,name2,name3]
dict1['age']=[age1,age2,age3]
print(dict1)
#创建列表
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = list([1,2,3,4,5,6,7,8,9,10])#
list3 = list(range(1,11))
list4 = [i for i in range(1,11)]
#列表推导式
#列表推导式：[表达式 for 变量 in 可迭代对象 if 条件] 
#列表推导式：[表达式 for 变量 in 可迭代对象]
#列表推导式：[表达式 for 变量 in 可迭代对象 if 条件 for 变量 in 可迭代对象 if 条件]
#列表推导式：[表达式 for 变量 in 可迭代对象 if 条件 for 变量 in 可迭代对象 if 条件 if 条件]
#列表推导式：[表达式 for 变量 in 可迭代对象 if 条件 for 变量 in 可迭代对象 if 条件 if 条件]
list5 = [i for i in range(1,11) if i%2==0]
list6 = [i for i in range(1,11) if i%2!=0]
list7 = [i for i in range(1,11) if i%2==0 if i%3==0]
print(list7)
list8 = [i for i in range(1,11) if i%2==0 if i%3!=0]
print(list8)


print(list1)
print(list2)
print(list3[0:5])#切片
print(list3[-5:])#索引
print(list3[::2])#步长
print(list3[::-1])#倒序
print(list3[::-2])#倒序
print(list3[::-3])#倒序
print(list3[::-4])#倒序
print(list3[::-5])#倒序
print(list3[::-6])#倒序
print(list3[::-7])#倒序
print(list3.index(3))#索引
print(list3.count(3))#统计
list3.append(11)#追加
list3.insert(0,15)#插入
list3.extend([11,22,33])#扩展
print(list3)
list3.remove(11)#删除
#list3.pop()#删除
##list3.pop(0)#删除
#list3.clear()#清空
list3.reverse()#反转
print(list3)
list3.sort()#排序
print(list3)
list3.sort(reverse=True)#倒序
print(list3)
list3.sort(reverse=True)#排序
list3.sort(reverse=False)#排序
list3.sort(key=None,reverse=True)#排序
list3.sort(key=None,reverse=False)#排序
#移除列表中的重复元素
list3.remove(11)
list3.remove(11)#删除
list3.pop(0)#删除
del list3[0]#删除
list3.clear()#清空
list3.reverse()#反转
#将字符串中的小写字母转换成大写字母
str1 = "abcdefg"
str2 = str1.upper()

#格式化 花名册     证明                 
name=input(' 请输入姓名：')
age=int(input(' 请输入年龄：'))
score=int(input(' 请输入成绩：'))
print('%s的年龄是%10.3d,成绩是%d'%(name,age,score))
print('{}的年龄是{},成绩是{}'.format(name,age,score))
print('{0}的年龄是{1},成绩是{2}'.format(name,age,score))
print('{name}的年龄是{age},成绩是{score}'.format(name=name,age=age,score=score))
print(f'{name}的年龄是{age},成绩是{score}')
print('{0:>10}的年龄是{1:>10.3f},成绩是{2:>10}'.format(name,age,score))

 


  #7.编写程序，计算圆周        另一种写法
import math
r=float(input('请输入半径：'))
area=math.pi*r*r
print('半径为{}的圆的面积是{}'.format(r,area))
print('半径为{0}的圆的面积是{1}'.format(r,area))
print('半径为{0:.2f}的圆的面积是{1:.2f}'.format(r,area))
  #7.编写程序，

    
#找数列 最大数
list1=[1,5,5,9,11,88,102]
sum=-100#若干小
for i in list1:
    if i> sum:
        sum=i
print(sum)
#找数列 最小数
list1=[1,5,5,9,11,88,102]
sum=1000#若干大
for i in list1:
    if i< sum:
        sum=i
print(sum)



class Foo(object):

    


    def __init__(self, price):
        self.price = price

    def how_much_of_book(self, n):
        print(self)
        return self.price * n

#导入模块
import demo1  #
demo1.f()
#导入包
from pageage import demo1
demo1.f()



























































































































































































































































































  #练习                                       
    #1.编写程序，输入一个整数，输出该整数的阶乘
a=int(input('请输入一个整数：'))
b=1
for i in range(1,a+1):
        b=b*i
print(b)
    #2.编写程序，输入一个整数，输出该整数的绝对值
a=int(input('请输入一个整数：'))
if a>=0:
    print(a)
else:
    print(-a)
    #3.编写程序，输入一个整数，输出该整数的绝对值
a=abs(float(input('请输入一个整数：')))
print(a)
    #4.编写程序，输入一个整数，输出该整数的绝对值  另一种写法             
a=int(input('请输入一个整数：'))
print(abs(a))   
    #5.编写程序，输入一个整数，输出该整数的绝对值  另一种写法   
    #6.编写程序，计算圆周率π的值 另一种写法  

       
import math
a=math.pi
print(a)
    #7.编写程序，计算圆周  另一种写法



#from email.headerregistry import Address
#from sys import flags
#from typing import Dict


from datetime import date, datetime
from logging.config import dictConfig
from pickle import DICT

from money import fib


print
#hfghfghfghfghfghghh
print ("f")

print ((5**2)**2)
print(9+6)

555555
print(9-3)
class a:
    def __init__(self):
        print("a")
''' def __init__(self,a):
        print(a)'''
    
   
a1=a()
a2=a()
a3=a()
a4=a()
a5=a()
a2
a1
a3
a4
a5
dir(a1)
a



#00
'''b=open("/Users/xkg/Documents/test.txt", "a+")
print("ggg", file=b)
b.close()
b=open("/Users/xkg/Documents/test.txt", "a+")
print("ggg", file=b)
b.close()'''
#pass用于占位
a=int(input('请输入：'))
if a==1:
   pass
elif a==2:
    pass
elif a==3:
    pass
else:
    pass
#range()函数
i=range(1,10) #range(start,stop,step)
print(i)
print(list(i))
for i in range(1,10):
    print(i)
i=range(1,10,2)
for j in i:
    print(j)
#while循环
i=0 #初始化循环变量 
num_a=0  #初始化工作变量
while i<101: #循环条件
  num_a+=i #工作变量的操作（表达式）
  i+=1     #循环变量操作与定义（表达式），   循环变量的操作（表达式）与工作变量的操作（表达式）统称为循环体
print(num_a)  #循环结束后执行
#break
i=0
while i<10:
    print(i)
    i+=1
    if i==5:
        break
#continue
i=0
while i<10:
    i+=1
    if i==5:
        continue
    print(i)
#pass
i=0
while i<10:
    i+=1
    if i==5:
        pass
    print(i)
#for循环
for i in range(1,10):
    print(i)
#for循环
for i in range(1,10,2):
    print(i)
#for循环
for i in range(1,10,2): #多重定义，变化赋值
    print(i) 
    #累加
sum1=0
for i in range(2,101,2):
 sum1+=i #sum=sum+i sum1实现了迭代累加（累积）
print(sum1)  #2550
#累加
sum2=0
for i in range(1,101,2):
 sum2+=i
print(sum2)  #2500
sum3=sum1+sum2
print(sum3)  #5050
#累加偶数
i=0   #初始化循环变量
sum4=0  #初始化工作变量
while i<101:     #循环条件
 if i%2==0: #i%2!=0 求奇数
  sum4+=i   #sum4=sum4+i
 i+=1
print(sum4)  #2550
#累加偶数
i=0
sum5=0
while i<101:
 if not bool(i%2!=0): #bool()函数，返回值为True或False 不加not取反,求奇数
  sum5+=i
 else:
  pass
 i+=1
print(sum5)  #2550
 #累加奇数
i=0
sum6=0
while i<50:

        sum6+=i*2+1 #sum6=sum6+i*2 求偶数
    
    
        i+=1
print(sum6)  #2500
#for循环
for _ in range(1,10):
    print("hello")
for i in 'hello':
    print(i,end="\t")
#for循环
for i in [1,2,3,4,5]:
    print(i)
#打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()
#打印水仙花数
for i in range(100,1000,1):#初始为100，终止为1000，步长为1
    a=i//100 #取百位数
    b=i%100//10#//取整除法（i//10%10）
    c=i%10  #取个位数
    if i==a**3+b**3+c**3:
        print(i)

#打印水仙花数
#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()#换行
#1到1000的质数
for i in range(2,1000):
    for j in range(2,i):
        if i%j==0:
            break #跳出循环
    else:
     print(i)


#打印1到100的偶数
for i in range(1,100):
    if i%2!=0:
        pass   
    else:
        print(i)
#打印1到100的奇数
for i in range(1,100):
    if i%2==0:
        continue#跳出本次循环
    else:
        print(i)
#for 循环 列表 元组 字典 字符串 其他 
#for循环
for i in [1,2,3,4,5]:#列表
    print(i)

#for循环元组
for i in (1,2,3,4,5):#元组
    print(i ,end="\t")

#for循环字典
for i in {'name':'zhangsan','age':18}:#字典
    print(i)
    #for循环字符串
for i in "hello":#字符串
    print(i)
#for循环其他
for i in range(1,10):
    print(i)
    
#1到100的质数的个数
sum=0
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum+=1  
print(sum)

# 解锁
# 判断用户输入的密码是否正确
# 如果正确，则输出“登录成功”
# 如果不正确，则输出“密码错误”
# 如果用户输入的密码错误超过三次，则输出“账户锁定”
# 如果用户输入的密码正确，则输出“登录成功”
inpu = input("请输入密码：")
if inpu == "123456":
    print("登录成功")
else:
    print("密码错误")
    inpu = input("请输入密码：")
    if inpu == "123456":
        print("登录成功")
    else:
        print("密码错误")
        inpu = input("请输入密码：")
        if inpu == "123456":
            print("登录成功")
        else:
            print("密码错误")
            inpu = input("请输入密码：")
            if inpu == "123456":
                print("登录成功")
            else:
                print("密码错误")
                inpu = input("请输入密码：")
                if inpu == "123456":
                    print("登录成功")
                else:
                    print("密码错误")
                    inpu = input("请输入密码：")
                    if inpu == "123456":
                        print("登录成功")
                    else:
                        print("密码错误")
                        inpu = input("请输入密码：")
                        if inpu == "123456":
                            print("登录成功")
                        else:
                            print("密码错误")
                            inpu = input("请输入密码：")
                            if inpu == "123456":
                                print("登录成功")
                            else:
                                print("密码错误")
                                inpu = input("请输入")
      
#1.编写程序，输入一个数字，判断这个数字是否是素数（质数）。
inpu = int(input("请输入一个数字："))
for i in range(2,inpu):
    if inpu%i==0:
        print("不是素数")
        break #跳出循环
else:
     print("是素数")
#包含1到100的质数的集合
dict={}
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
            ge = i#获取质数
            dict[ge]=ge
print(dict)
#1到100的质数的和
sum=0
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum+=i
print(sum)
#1到100的质数的和
sum=0
for i in dict:
  sum+=i
print(sum)
#三次输入密码，如果密码正确，则输出“登录成功”，如果密码错误，则输出“密码错误”，如果密码错误超过三次，则输出“账户锁定”
pwb = input("请输入密码：")
for i in range(3):
    if pwb == "123456":
        print("登录成功")
        break
    elif i == 2:
        print("账户锁定")
    else:
        print("密码错误")
        pwb = input("请输入密码：")
print("账户锁定")
#三 次输入密码，如果密码正确，则输出“登录成功”，如果密码错误，则输出“密码错误”，如果密码错误超过三次，则输出“账户锁定”
pwb = input("请输入密码：")
for i in range(3):  
    if pwb == "123456":
        print("登录成功")
        break
    else:
        print("密码错误")
        pwb = input("请输入密码：")                          
print("账户锁定")
#1到50中5的倍数的和
sum=0
for i in range(1,51):
    if i%5==0:
        sum+=i
print(sum)
#1到50中5的倍数的和
sum=0
for i in range(1,51):
    if i%5!=0:
        continue#结束本次循环
    else:
        sum+=i
print(sum)
#三次输入密码，如果密码正确，则输出“登录成功”，如果密码错误，则输出“密码错误”，如果密码错误超过三次，则输出“账户锁定”
pwb = input("请输入密码：")
for i in range(3):
    if pwb == "123456":
        print("登录成功")
        break#跳出循环
    else:
        print("密码错误")
        pwb = input("请输入密码：")
        
else:
    print("账户锁定")   

    
#创建一个字典，存储学生信息，包括姓名、年龄、成绩，并且要求每个学生的信息都不能重复。
dict={}
while True:
    name = input("请输入姓名：")
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    Addres=input("请输入地址：")
    dict[name]=[age,score,Addres]
    inpu = input("是否继续（y/n）")
    if inpu == "n":
        break
    inpu = input("是否继续（y/n）：")
    if inpu == "n":
        break
print(dict)
#创建一个字典，存储学生信息，包括姓名、年龄、成绩，并且要求每个学生的信息都不能重复。
dict1={}
name1=input("请输入1姓名：")
name2=input("请输入2姓名：")
name3 = input("请输入3姓名：")
age1=int(input("请输入1年龄："))
age2=int(input("请输入2年龄："))
age3=int(input("请输入3年龄："))
dict1['name']=[name1,name2,name3]
dict1['age']=[age1,age2,age3]
print(dict1)
#创建列表
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = list([1,2,3,4,5,6,7,8,9,10])#
list3 = list(range(1,11))
list4 = [i for i in range(1,11)]
#列表推导式
#列表推导式：[表达式 for 变量 in 可迭代对象 if 条件] 
#列表推导式：[表达式 for 变量 in 可迭代对象]
#列表推导式：[表达式 for 变量 in 可迭代对象 if 条件 for 变量 in 可迭代对象 if 条件]
#列表推导式：[表达式 for 变量 in 可迭代对象 if 条件 for 变量 in 可迭代对象 if 条件 if 条件]
#列表推导式：[表达式 for 变量 in 可迭代对象 if 条件 for 变量 in 可迭代对象 if 条件 if 条件]
list5 = [i for i in range(1,11) if i%2==0]
list6 = [i for i in range(1,11) if i%2!=0]
list7 = [i for i in range(1,11) if i%2==0 if i%3==0]
print(list7)
list8 = [i for i in range(1,11) if i%2==0 if i%3!=0]
print(list8)


print(list1)
print(list2)
print(list3[0:5])#切片
print(list3[-5:])#索引
print(list3[::2])#步长
print(list3[::-1])#倒序
print(list3[::-2])#倒序
print(list3[::-3])#倒序
print(list3[::-4])#倒序
print(list3[::-5])#倒序
print(list3[::-6])#倒序
print(list3[::-7])#倒序
print(list3.index(3))#索引
print(list3.count(3))#统计
list3.append(11)#追加
list3.insert(0,15)#插入
list3.extend([11,22,33])#扩展
print(list3)
list3.remove(11)#删除
#list3.pop()#删除
##list3.pop(0)#删除
#list3.clear()#清空
list3.reverse()#反转
print(list3)
list3.sort()#排序
print(list3)
list3.sort(reverse=True)#倒序
print(list3)
list3.sort(reverse=True)#排序
list3.sort(reverse=False)#排序
list3.sort(key=None,reverse=True)#排序
list3.sort(key=None,reverse=False)#排序
#移除列表中的重复元素
list3.remove(11)
list3.remove(11)#删除
list3.pop(0)#删除
del list3[0]#删除
list3.clear()#清空
list3.reverse()#反转
#将字符串中的小写字母转换成大写字母
str1 = "abcdefg"
str2 = str1.upper()

#格式化 花名册     证明                 
name=input(' 请输入姓名：')
age=int(input(' 请输入年龄：'))
score=int(input(' 请输入成绩：'))
print('%s的年龄是%10.3d,成绩是%d'%(name,age,score))
print('{}的年龄是{},成绩是{}'.format(name,age,score))
print('{0}的年龄是{1},成绩是{2}'.format(name,age,score))
print('{name}的年龄是{age},成绩是{score}'.format(name=name,age=age,score=score))
print(f'{name}的年龄是{age},成绩是{score}')
print('{0:>10}的年龄是{1:>10.3f},成绩是{2:>10}'.format(name,age,score))

 


  #7.编写程序，计算圆周        另一种写法
import math
r=float(input('请输入半径：'))
area=math.pi*r*r
print('半径为{}的圆的面积是{}'.format(r,area))
print('半径为{0}的圆的面积是{1}'.format(r,area))
print('半径为{0:.2f}的圆的面积是{1:.2f}'.format(r,area))
  #7.编写程序，

    
#找数列 最大数
list1=[1,5,5,9,11,88,102]
sum=-100#若干小
for i in list1:
    if i> sum:
        sum=i
print(sum)
#找数列 最小数
list1=[1,5,5,9,11,88,102]
sum=1000#若干大
for i in list1:
    if i< sum:
        sum=i
print(sum)



class Foo(object):

    


    def __init__(self, price):
        self.price = price

    def how_much_of_book(self, n):
        print(self)
        return self.price * n

#导入模块
import demo1  #
demo1.f()
#导入包
from pageage import demo1
demo1.f()



























































































































































































































































































  #练习                                       
    #1.编写程序，输入一个整数，输出该整数的阶乘
a=int(input('请输入一个整数：'))
b=1
for i in range(1,a+1):
        b=b*i
print(b)
    #2.编写程序，输入一个整数，输出该整数的绝对值
a=int(input('请输入一个整数：'))
if a>=0:
    print(a)
else:
    print(-a)
    #3.编写程序，输入一个整数，输出该整数的绝对值
a=abs(float(input('请输入一个整数：')))
print(a)
    #4.编写程序，输入一个整数，输出该整数的绝对值  另一种写法             
a=int(input('请输入一个整数：'))
print(abs(a))   
    #5.编写程序，输入一个整数，输出该整数的绝对值  另一种写法   
    #6.编写程序，计算圆周率π的值 另一种写法  

       
import math
a=math.pi
print(a)
    #7.编写程序，计算圆周  另一种写法







