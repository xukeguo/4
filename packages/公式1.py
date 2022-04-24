#欢迎使用Python脚本编辑器！我的一小步，人类一大步！
#@File    :   公式函数.py
#@Time    :   2022/04/19 23:27:39
#@Author  :   flow-laic 
#@Email   :
print(bool(6==7))#判断是否相等
#1.编写程序，输入一个数字，判断这个数字是否是素数（质数）。
input = int(input("请输入一个数字："))
for i in range(2,input):
    if input%i==0:
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
            ge = i#获取质数88
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
#判断是否为回文数 
def is_palindrome(n):
    if n<0:
        return False
    if n==0:
        return True
    if n==1:
        return True
    else:
        return is_palindrome(n//10) and n%10==n//10%10

print(is_palindrome(12321))
#判断是质数
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
    
print(is_prime(21))

def is_prime(n):
    for i in range(2,n):
        if n%i!=0:
            continue
        else:
           return False#结束程序并返回False
    else:
        return True
print(is_prime(17))
#质数序列
def myfun(N=100):#不可变参数
    list1=[]
    n=int(input("请输入一个数字："))
    for i in range(2,n):
       for j in range(2,i):
         if i%j==0:
            break
       else:
        list1.append(i) 
        
    global c
    c=list1

myfun()
print(c)

       
#素数 正向思维
dict1={}
for i in range(2,101):
    dict1[i]=True 
for i in range(2,101):
    for j in range(i*2,101,i):
      dict1[j]=False
print(dict1)
 


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

#递归函数
def fact(n):
    if n==101:
        return 0
    return n+fact(n+1)
print(fact(1))

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


    print ('字典中不包含name和张三')
#判断奇数偶数
dict1={'name':'张三','age':18,}
if dict1['age']%2==0:
    print ('字典中的age是偶数')
else:
    print ('字典中的age是奇数')
    #判断key是否匹配
dict1={'name':'张三','age':18,}
if dict1.keys()==('name','age'):
    print ('字典中的key是name和age')
else:
    print ('字典中的key不是name和age')
#判断value是否匹配
dict1={'name':'张三','age':18,}
if dict1.values()==('张三',18):
    print (dict1.values()) #('张三', 18)
dict1={'name':'张三','age':18,}
if dict1['name']=='张三':
        print ('字典中的value是name和张三')
else:
        print ('字典中的value不是name和张三')
#字典的排序
dict1={'name':'张三','age':18,}
print (sorted(dict1)) #['age', 'name']
print (sorted(dict1.items())) #[('age', 18), ('name', '张三')]

 #提取字典中的key
dict1={'name':'张三','age':18,}
score= (dict1.keys()) #dict_keys(['age', 'name'])
print (score) #('age', 'name')
#提取字典中的一个key用作变量？
dict1={'name':'张三','age':18,}
#提取字典中的value
dict1={'name':'张三','age':18,}
score= (dict1.values()) #dict_values([18, '张三'])         #提取字典中的一个value用作变量？



#创建学生信息字典
dict1={}
input_student = input('请输入学生姓名：')
dict1['name']=input_student
input_age = input('请输入学生年龄：')
dict1['age']=input_age
input_score = input('请输入学生成绩：')
dict1['score']=input_score
print (dict1)
#字典视图排序
dict1={'name':'张三','age':18,}
print (sorted(dict1.items())) #[('age', 18), ('name', '张三')]
print (sorted(dict1.keys())) #['age', 'name']
print (sorted(dict1.values())) #[18, '张三']
#字典的生成式
list1=[ '张三', '李四', '王五', '赵六', '田七', '钱八', '孙九', '周十']
list2=[18,19,20,21,22,23,24,25]
print (dict(zip(list1,list2))) #{'张三': 18, '李四': 19, '王五': 20, '赵六': 21, '田七': 22, '钱八': 23, '孙九': 24, '周十': 25}
print(type(list1)) #<class 'list'>
list3=[90,80,70,60,50,40,30,20]
dict1={ x:[y,z] for x,y,z in zip(list1,list2,list3)}
dict2={ x:y for x,y in zip(list1,list2)}
print(type(dict1)) #<class 'dict'>
print (dict1)
print (dict2)
#输出字典中键值最小的键值对
dict={'LiSi':9,'waiwu':5,'lili':5}
for x,y in dict.items():
    if x == min(dict,key=dict.get):#判断x是否在字典中
       min_sum=y
for x,y in dict.items():
    if y == min_sum:
         print(x,y)
#输出字典中键值最大的键值对
dict={'LiSi':9,'waiwu':5,'lili':5,'wangwu':8,'zhaoliu':9}
for x,y in dict.items():
    if x == max(dict,key=dict.get):#判断x是否在字典中
       min_sum=y
for x,y in dict.items():
    if y == min_sum:
         print(x,y)
          
list(dict.keys())[list(dict.values()).index('张三')]#输出字典中包含的某键值的对应键
#根据最小值返回对应的键
dict={2:1,3:9,4:5}
min(dict,key=dict.get)
#根据最大值返回对应的键
dict={2:1,3:9,4:5}
max(dict,key=dict.get)
#找出所有键值为男性的键对
persons={'ZhangSan':'male',
'LiSi':'male',
'WangHong':'female'}
males = filter(lambda x:'male'== x[1], persons.items())
for (key,value) in males:
  print('%s : %s' % (key,value))


'''输出如下：

LiSi : male

ZhangSan : male

注意：

字典中的value不保证唯一性，因此根据值查出来的是一个list.

不过字典中key的值是唯一的，因此根据key将可以查到唯一的一个value'''

print('李四的性别: %s'% persons['LiSi'])

'''输出如下

李四的性别: male'''
#编写计算圆周率的程序      可以使用math库

from unicodedata import name


s=3.14
def pi(n):#定义函数
    s = 0
    for i in range(n):
        s += 1/pow(16,i)*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
    return s#返回值,调用函数得到s的值
n=int(input('圆周率的多边形值:'))#调用
pi(n)#调用
print(s)#3.14,自定义函数的返回值不更改S的值
print(pi(n))#3.141592653589793,调用函数的返回值
print("%.100f"%pi(n))#输出精确到小数点后位
print("%.100f"%(1/3))#输出精确到小数点后位
#自己定义函数
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-10))
#自己定义函数
def my_abs(x):
    if not isinstance(x,(int,float)):#  判断x是否为整数或浮点数
        raise TypeError('bad operand type')#抛出异常
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-10))
#自己定义函数
def my1(x):#不可变参数
    global n1#全局变量
    n1=list(n)#将n转换为列表
    for i  in x:
      n1.send(i)#添加
    return n1#返回

m=[1,5,9,44]
n=list(m)
print(my1(m))
print(n)
print(m)
print(n1)
#自己定义函数
def my2():#不带参数
 return 'hello world'
print(my2())
#自己定义函数  可变参数 可以传入0个或多个参数 参数类型可以不同 不能传入关键字参数 不能传入可变参数 不能传入不可变参数 不能传入字典   可以传入关键字参数 可以传入可变参数  可以传入不可变参数  可以传入字典  
def my3(a,b=100):#带默认值的参数
    return a+b
print(my3(10))
print(my3(10,20))
#自己定义函数
def myfun(*args):#可变参数
    sum=0
    for i in args:
        sum+=i
    return sum
print(myfun(1,2,4,5))
#自己定义函数
def myfun(**kw):#关键字可变参数
  print(kw)
print(myfun(name='zhangsan',age=18,score=100))
#自己定义函数   
def myfun1(*a,**b):#可变参数与关键字参数 可以同时使用 可变参数必须在关键字参数之前 关键字参数必须在可变参数之后 
    print(a[0])
# print(b['name'])'''
    for i in b:
        if i=='name':
            print('%s' %i,b[i])#输出
        else:
           pass
dict1={'name':'zhangsan','age':18,'score':100} 
myfun1(1,2,dict1)#字典也不可以作为关键字可变参数
print(myfun1(1,2,3,4,5,name='zhangsan',age=18,score=110))

#自己定义函数
def myfun2(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z):
    print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)
#求最大值
#求两数的最大公约数
a = int(input('请输入第一个数字:'))
b = int(input('请输入第二个数字:'))
for i in range(a+b,1,-1):
    if a%i==0 and b%i==0:
        print(i)
        break
else:
    print('没有公约数')
#求两数的最小公倍数
a = int(input('请输入第一个数字:'))
b = int(input('请输入第二个数字:'))
for i in range(1,a*b+1):
    if i%a==0 and i%b==0:
        print(i)
        break



def max(list):#求最大值
    max=list[0]
    for i in list:
        if i>max:
            max=i
    return max
print(max(list_score))
c=min(list_age)#获取列表中的最小值
def my_min(list):
    min=list[0]
    for i in list:
        if i<min:
            min=i
    return min

#获取列表的平均值
def my_average(list):
    sum=0
    for i in list:
        sum+=i
    return sum/len(list)
list1=[x for x in range(1,10,2)]
a=sum(list1)/len(list1)
print(a)
print(my_average(list1))

#质因式分解
def my_zysfj(n=100):
    list_zysfj=[]    
    n=int(input('请输入一个数字:'))
    b=n
    a=0
    print(b)
    for i in range(2,n):
      for j in range(2,b):
                if n%i!=0:
                 break
                else:
                    print(i)
                    list_zysfj.append(i)           
                    n=n/i
                    a=1
    global c
    c=list_zysfj
    if a==0:
      print('%d是素数'%b)
    else:
      print('%d的因式分解为%s'%(b,c))#%s是字符串 %d是整数  %f是浮点数 %.2f是保留两位小数 %.3f是保留三位小数 
    return c

print(my_zysfj())
#因式分解二 优化
def my_zysfj(n=100):
    list_zysfj=[]    
    b=n
    for i in range(2,b+1):
      for j in range(2,b+1):
                if n%i!=0:
                 break#跳出当前循环
                else:
                    list_zysfj.append(i)           
                    n=n/i             
    global list_zysfj1
    list_zysfj1=list_zysfj
    return list_zysfj1
print(my_zysfj(97))
print(list_zysfj1,type(list_zysfj1))
#解yython中的练习题
#1.输入一个数字，判断是否是素数
def my_prime(n=100):    
    n=int(input('请输入一个数字:'))
    for i in range(2,n):
        if n%i==0:
            print('%d不是素数'%n)
            break
    else:
     print('%d是素数'%n)

my_prime()
#解方程
def my_equation(a,b,c):
    import math
    x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    print('x1=%f,x2=%f'%(x1,x2))
a=int(input('请输入a:'))
b=int(input('请输入b:'))
c=int(input('请输入c:'))
my_equation(a,b,c)
#输入几个数字，输出最大值
def my_max(list):
    max=list[0]
    for i in list:
        if i>max:
            max=i
    return max
list=[]
for i in range(3):
    list.append(int(input('请输入一个数字:')))
print(my_max(list))
#输入几个数字，输出最小值
def my_min(list):
    min=list[0]
    for i in list:
        if i<min:
            min=i
    return min

print(my_min(list))
#输入几个数字，输出平均值
def my_average(list):
    sum=0
    for i in list:
        sum+=i
    return sum/len(list)
list1=[]
for i in range(3):
    list1.append(int(input('请输入一个数字:')))
print(my_average(list1))
#输入一个数字，输出该数字的因式分解
def my_factor(n):
    b=n
    a=0
    for i in range(1,n+1):
     if n%i==0:
            list8.append(i)
            n=n/i
            a=1
list8=[]
n=int(input('请输入一个数字:'))
print(my_factor(n))
print(list8)
#输入几个数字，组成一个数
def my_factor(a,b,c):
    n=a*100+b*10+c
    return n
a=int(input('请输入第一个数字:'))
b=int(input('请输入第二个数字:'))
c=int(input('请输入第三个数字:'))
print(my_factor(a,b,c))
#输入一个数字，判断是否是质数
def my_prime(n):
    for i in range(2,n):
        if n%i==0:
            print('%d不是素数'%n)
            break
    else:
        print('%d是素数'%n)
n=int(input('请输入一个数字:'))
my_prime(n)
#核对用户输入的密码合法性
def my_password(password_a=0):
 for i in range(3):
 # if password_a==1:
    #break
  password=input('请输入密码:')
  if len(password)<6:
        print('密码长度不能小于6位')
  elif len(password)>12:
        print('密码长度不能大于12位')
  elif password.isdigit():
        print('密码不能全为数字')
  elif password.isalpha():
        print('密码不能全为字母')
    
  elif password=='123456':
            print('密码不能为123456')
     
  elif password=='abcdef':
                print('密码不能为abcdef')
  else:
        a=password
        print('密码可用，再次输入')
        password=input('请输入密码：')
        if password==a:
            print('密码可用')
            global   password_b
            password_b=1#用于判断是否需要核对密码
            password_a==1#打卡标记专用
            flag=1 #标记为1，退出循环地flag=1标记专用
            flag=True
            global  globalpassword
            globalpassword=password
            return globalpassword
            break#也s可以用在开头处判别打卡参数的方法
           
        else:
            print('两次输入不一致')
            return my_password(password)
 #return password

my_password(password_a=0)
print(globalpassword)
#try...except...else...finally
import traceback
try:#try...except...else...finally的使用方法   可以捕获异常 可以捕获异常后执行else 可以捕获异常后执行finally  
    a=int(input('请输入一个数字:'))
    b=int(input('请输入一个数字:'))
    print(a/b)
except ZeroDivisionError:#捕获除数为0的异常  
    print('除数不能为0')
except ValueError:
    print('输入的不是数字')
except:
    print('未知错误')    
else:
    print('输入正确')
finally:
    print('程序结束')
#class
class MyClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def my_print(self):
        print('%s的年龄是%d'%(self.name,self.age))
    def my_add(self,a,b):
        return a+b
    def my_sub(self,a,b):
        return a-b
    def my_mul(self,a,b):
        return a*b
    def my_div(self,a,b):
        return a/b
    def my_mod(self,a,b):
        return a%b
    def my_pow(self,a,b):
        return a**b
    def my_max(self,a,b):
        return max(a,b)
    def my_min(self,a,b):
        return min(a,b)
    def my_average(self,a,b):
        return (a+b)/2
    def my_factor(self,a):
        for i in range(1,a+1):
            if a%i==0:
                print('%d的因数是%d'%(a,i))
                break
    def my_prime(self,a):
        for i in range(2,a):
            if a%i==0:
                print('%d不是素数'%a)
                break
        else:
            print('%d是素数'%a)
   
class MyClass2(MyClass):
    def __init__(self,name,age,):
        super().__init__(name,age)
    def my_print(self):
        print('%s的年龄是%d'%(self.name,self.age))
    def my_add(self,a,b):
        return a+b
    def my_sub(self,a,b):
        return a-b
    def my_mul(self,a,b):
        return a*b
    def my_div(self,a,b):
        return a/b
        #继承
        #继承的基本原理 
        #父类的方法，子类的方法，父类的属性，子类的属性
        #父类的方法，子类的方法，父类的属性，子类的属性
        #实例化父类，实例化子类，调用父类的方法，调用子类的方法
        def eat(self):
            print('吃饭')
#静态方法  
    @staticmethod
    def my_static_method():
            print('静态方法')
#类方法
    @classmethod
    def my_class_method(cls):
        print('类方法')
'''#实例化类
class_1=MyClass('张三',18)
class_2=MyClass2('李四',19)
class_1.eat()
class_2.eat()
class_1.my_static_method()
class_2.my_static_method()
class_1.my_class_method()
class_2.my_class_method()'''
#继承
#继承的基本原理
list1=list(range(1,10))
a=min(list1)
print(a)

#类的继承
#继承的基本原理
#父类的方法，子类的方法，父类的属性，子类的属性
#父类的方法，子类的方法，父类的属性，子类的属性

class Student:
    def __init__(self,name,age,address):
        self.name=name
        self.__age=age
        self.addr=address
    def study(self):
        print('%s正在学习'%self.name)
    def whitename(self):
         print('%s'% self.name)
    def eat(self):
        print('%s正在吃饭'%self.name)
    def sleep(self):
        print('%s正在睡觉'%self.name)
    def whiteage(self):
        print('%s的年龄是%d'%(self.name,self.__age))
    def whteaddr(self):
        return '%s的地址是%s'%(self.name,self.addr)
class Teacher:
    def __init__(self,name,_age,address):
        self.name=name
        self.age=_age
        self.addr=address
    def teach(self):
        print('%s正在教学'%self.name)
    def eat(self):
        print('%s正在吃饭'%self.name)
    def sleep(self):
        print('%s正在睡觉'%self.name)
    def nameage(self):
        return '%s'% self.name
class Student_teacher(Student,Teacher):
        
        def __new__(cls, *args, **kwargs):
            #类方法
            print('__new__')
            return super().__new__(cls)#调用父类的__new__方法,返回父类的实例化对象,交给父类的__init__方法

        def __init__(self,name,age,address,address2):
            #继承父类的属性
               super().__init__(name,age,address)
               self.addr2=address2
stu1=Student('张三',18,'北京')
stu=Student(9,4,9)
stu2=Student_teacher('李四',19,'上海','广州')
print(stu1.whiteage())
stu.whitename()
stu.eat()
stu1.whitename()
stu1.eat()
stu1.sleep()
print(stu.whiteage())
print(stu.whteaddr())
print(dir(stu))#获取对象的属性和方法
print(stu._Student__age)#私有属性
#类的继承

import copy
#浅拷贝   只拷贝父类的属性
list1=[1,2,3,[4,5]]
list4=list1[2]
print(list4)
list2=copy.copy(list1)
list2[3][0]=100# list1[3][0]也会变成100
print(list1)#
print(list2)
#深拷贝           
list3=copy.deepcopy(list1)
list3[3][0]=200#
print(list1)#
print(list3)
#类的继承
#继承的基本原理
#父类的方法，子类的方法，父类的属性，子类的属性
#读秒程序
import time
def timer(func):#装饰器
    def wrapper(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print('the func run time is %s'%(stop_time-start_time))
    return wrapper
@timer
def test1():
    time.sleep(3)
    print('in the test1')
@timer
def test2():
    time.sleep(3)
    print('in the test2')
test1()
test2()

#读秒程序   
import time
class Clock(object):
    def __init__(self,hour=0,minute=0,second=0):
        self._hour=hour
        self._minute=minute
        self._second=second
    def run(self):
        self._second+=1
        if self._second==60:
            self._second=0
            self._minute+=1
            if self._minute==60:
                self._minute=0
                self._hour+=1
                if self._hour==24:
                    self._hour=0
    def show(self):
        return '%02d:%02d:%02d'%(self._hour,self._minute,self._second)

a=Clock( 23,59,59)
while True:
    print(a.show())
    time.sleep(1)
    a.run()
    if time.time()>=1570666799:
        break
# 微信群管理系统 
class Wechat(object):
    def __init__(self,name):
        self.name=name
        self.members=[]
    def add_member(self,member):
        self.members.append(member)
    def show_members(self):
        for member in self.members:
            print(member)
    def send_message(self,message):
        for member in self.members:
            member.receive_message(message)
    def __str__(self):
        return '%s'%self.name    
    def __repr__(self):
            return '%s'%self.name

class Member(object):
    def __init__(self,name):
        self.name=name
    def receive_message(self,message):
        print('%s收到消息：%s'%(self.name,message))
def main():
    wechat=Wechat('python')
    wechat.add_member(Member('张三'))
    wechat.add_member(Member('李四'))
    wechat.add_member(Member('王五'))
    wechat.send_message('你好')
    wechat.show_members()
if __name__=='__main__':
    main()

# 加入群组
# 退出群组
# 删除群组
# 查看群组
# 查看群成员
# 查看群消息
# 发送群消息
# 创建好友
# 删除好友
# 查看好友
# 发送好友消息
# 创建聊天室
# 加入聊天室
# 退出聊天室
# 删除聊天室
# 查看聊天室
# 查看聊天室成员
# 发送聊天室消息
# 创建聊天室管理员
# 删除聊天室管理员
# 查看聊天室管理员
# 创建聊天室成员
# 删除聊天室成员
# 查看聊天室成员
# 发送聊天室成员消息
#微积分
import math
def f(x):
    return x**3-2*x-1
def df(x):
    return 3*x**2-2
def newton(x):
    epsilon=0.00001
    while True:
        delta=f(x)/df(x)
        x=x-delta
        if abs(delta)<epsilon:
            break
    return x
print(newton(1))
# 分段函数
def f(x):
    if x<-2:
        return 1
    if x<=2:
        return x
    return 0
def trapezoidal(a,b,n):
    h=(b-a)/n
    s=0.5*(f(a)+f(b))
    for i in range(1,n):
        s+=f(a+i*h)
    return s*h
print(trapezoidal(-2,2,100))
# 梯形函数
def trapezoidal(a,b,n):
    h=(b-a)/n
    s=0.5*(f(a)+f(b))
    for i in range(1,n):
        s+=f(a+i*h)
    return s*h
print(trapezoidal(-2,2,100))
# 导数
def f(x):
    return x**3-2*x-1
def df(x):
    return 3*x**2-2
def newton(x):
    epsilon=0.00001
    while True:
        delta=f(x)/df(x)
        x=x-delta
        if abs(delta)<epsilon:
            break
    return x
print(newton(1))
#打一个圆
import turtle
turtle.circle(200)
#打一个正方形
import turtle
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
#打一个三角形
import turtle
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
#打一个五角形
import turtle
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
#打一抛物线
# import turtle
# turtle.penup()
#打一个椭圆
import turtle
turtle.circle(900,1000)
#打一个矩形
import turtle
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
#打一个烟花
def main():
    n = int(input('请输入烟花的数量：'))
    for i in range(n):
        for j in range(n-i):
            print(' ',end='')
        for k in range(i+1):
            print('*',end='')
        print()
    for i in range(n-1,-1,-1):
         for j in range(n-i):
            print(' ',end='')
         for k in range(i+1):
            print('*',end='')
         print()
main()
#圆形的烟花

#烟花的爆炸效果
def main():
    import turtle
    turtle.pensize(2)
    turtle.pencolor('red')
    turtle.circle(100)
    turtle.penup()
    turtle.goto(0,-50)
    turtle.pendown()
    turtle.pencolor('yellow')
    turtle.circle(50)
    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()    
    turtle.pencolor('blue')
    turtle.circle(10)
    turtle.done()
main()
from cmath import cos#   引入复数 cmath   引入复数的cos  引入复数的sin 引入复数的tan  引入复数的exp  引入复数的log  引入复数的sqrt 引入复数的pow 引入复数的phase 引入复数的conjugate  引入复数的rect  引入复数的ascii  引入复数的hex  引入复数的oct  引入复数的isreal  引入复数的iscomplex  引入复数的real  引入复数的imag  引入复数的conjugate  引入复数的as_integer_ratio  引入复数的as_integer  引入复数的as_tuple  引入复数的is_integer  引入复数的is_real  引入复数的is_imaginary  引入复数的is_finite  引入复数的is_infinite  引入复数的is_nan  引入复数的is_number  引入复数的is_zero  引入复数的is_nonzero  引入复数的is_positive  引入复数的is_negative  引入复数的is_nonpositive  引入复数的is_nonnegative  引入复数的is_integer  引入复数的is_extended_real  引入复数的is_extended_imaginary  引入复数的is_extended_negative  引入复数的is_extended_nonnegative  引入复数的is_extended_positive  引入复数的is_extended_nonpositive  引入复数的is_extended_zero  引入复数的is_extended_nonzero  引入复数的is_extended_finite  引入 复数的is_extended_infinite  引入复数的is_extended_nan  引入复数的is_extended_number  引入复数的is_extended_real  引入复数的is_extended_imaginary  引入复数的is_extended_negative  引入复数的is_extended_nonnegative  引入复数的is_extended_positive  引入复数的is_extended_nonpositive  引入复数的is_extended_zero  引入复数的is_extended_nonzero  引入复数的is_extended_finite  引入复数的is_extended_infinite  引入复数的is_extended_nan  引入复数的is_extended_number  引入复数的is_extended_real  引入复数的is_extended_imaginary  引入复数的is_extended_negative  引入复数的is_extended_nonnegative  引入复数的is_extended_positive  引入复数的is_extended_nonpositive  引入复数的is_extended_zero  引入复数的is_extended_nonzero  引入复数的is_extended_finite  引入复数的is_extended_infinite  引入复数的is_extended_nan  引入复数的is_extended_number  引入复数的is_extended_real  引入复数的is_extended_imag  
import datetime#时间模块
def main():#
    print(datetime.datetime.now())#当前时间
main()
#计算两个日期之间的天数
def main():
    import datetime
    d1 = datetime.datetime(2019,1,1)
    d2 = datetime.datetime(2019,1,2)
    print(d2-d1)
main()
#计算两个日期之间的天数
def main():
    import datetime
    d1 = datetime.datetime(2019,1,1)
    d2 = datetime.datetime(2019,1,2)
    print(d2-d1)    
main()

import email#邮件模块
#计算一个数的阶乘
def main():
    n = int(input('请输入一个数字：'))
    result = 1
    for i in range(1,n+1):
        result *= i
    print(result)
main()
#分解一个数字的质因数
def main():
    n = int(input('请输入一个数字：'))
    for i in range(2,n+1):
        while n%i == 0:
            print(i,end=' ')#end=' '表示不换行
            n = n//i
    print()
main()
#计算一个数是一定半径上的点的坐标
def main():
    import math
    r = float(input('请输入半径：'))
    n = int(input('请输入点的个数：'))
    for i in range(n):
        x = r*math.cos(2*math.pi*i/n)
        y = r*math.sin(2*math.pi*i/n)
        print('第%d个点的坐标为（%.2f,%.2f）'%(i+1,x,y))
main()
#用枚举类型来表示一个月份
def main():
    import enum
    class Month(enum.Enum):
        Jan = 1
        Feb = 2
        Mar = 3
        Apr = 4
        May = 5
        Jun = 6
        Jul = 7
        Aug = 8
        Sep = 9
        Oct = 10
        Nov = 11
        Dec = 12
    m = int(input('请输入一个月份：'))
    if m in [i.value for i in Month]:
        print(Month(m).name)
    else:
        print('输入有误')
main()
#用枚举类型来表示一个星期
def main():
    import enum
    class Week(enum.Enum):
        Sun = 1
        Mon = 2
        Tue = 3
        Wed = 4
        Thu = 5
        Fri = 6
        Sat = 7
    w = int(input('请输入一个星期：'))
    if w in [i.value for i in Week]:
        print(Week(w).name)
    else:
        print('输入有误')
main()
#用枚举类型来表示一个季节
def main():
    import enum
    class Season(enum.Enum):
        Spring = 1
        Summer = 2
        Autumn = 3
        Winter = 4
    s = int(input('请输入一个季节：'))
    if s in [i.value for i in Season]:
        print(Season(s).name)
    else:
        print('输入有误')
main()
#用枚举法解决一元二次方程
def main():
    import math
    a = float(input('请输入a：'))
    b = float(input('请输入b：'))
    c = float(input('请输入c：'))
    if a == 0:
        if b == 0:
            if c == 0:
                print('无解')
            else:
                print('无穷多个解')
        else:
            print('x = %.2f'%(-c/b))
    else:
        delta = b**2-4*a*c
        if delta < 0:
            print('无解')
        elif delta == 0:
            print('x = %5.2f'%(-b/(2*a)))
        else:
            print('x1 = %.2f'%((-b+math.sqrt(delta))/(2*a)),end=' ')
            print('x2 = %.2f'%((-b-math.sqrt(delta))/(2*a)))
main()
#用枚举法解决a*b*c的最大公约数
def main():
    import math
    a = int(input('请输入a：'))
    b = int(input('请输入b：'))
    c = int(input('请输入c：'))
    if a > b:
        a,b = b,a
    if a > c:
        a,c = c,a
    if b > c:
        b,c = c,b
    if a == b:
        print('%d'%c)
    elif a == c:
        print('%d'%b)
    elif b == c:
        print('%d'%a)
    else:
        for i in range(a,0,-1):
            if a%i == 0 and b%i == 0 and c%i == 0:
                print('%d'%i)
                break
main()

#用枚举法解决a*b的最小公倍数
def main():
    a = int(input('请输入a：'))
    b = int(input('请输入b：'))
    for i in range(a*b,0,-1):
        if a%i == 0 and b%i == 0:
            print('%d'%i)
            break
main()
#关键字可变参数 库函数enume

def main():
    import enum
    class 国家(enum.Enum):
        中国 = 1
        美国 = 2
        日本 = 3
        韩国 = 4
        德国 = 5
        法国 = 6
        英国 = 7
        意大利 = 8
        印度 = 9
        台湾 = 10
        泰国 = 11
        西班牙 = 12
        马来西亚 = 13
        越南 = 14
        澳大利亚 = 15
        印度尼西亚 = 16
        其他 = 17
    n = int(input('请输入一个国家：'))
    if n in [i.value for i in 国家]:
        print(国家(n).name)
    else:
        print('输入有误')
main()
    
    #用枚举法解决一个数字的百位数
def main():
    n = int(input('请输入一个数字：'))
    print(n//100)
main()
#0-1的随机数
def main():
    import random
    print(random.random())
main()

  
#0-1的线性同余随机数
def main():
    import random
    print(random.getrandbits(4))#获取4位的随机数（二进制）
main()


#线性随机数
try:
    import random
    print(random.randint(1,10))
except:
    print('请安装random库')
#0~360的线性随机数
def main():
    import random
    print(random.uniform(0,360))
main()
#解二元一次方程
def main():
    import math
    a = float(input('请输入a：'))
    b = float(input('请输入b：'))
    c = float(input('请输入c：'))
    if a == 0:
        if b == 0:
            if c == 0:
                print('无解')
            else:
                print('无穷多个解')
        else:
            print('x = %.2f'%(-c/b))
    else:
        delta = b**2-4*a*c
        if delta < 0:
            print('无解')
        elif delta == 0:
            print('x = %5.2f'%(-b/(2*a)))
        else:
            print('x1 = %.2f'%((-b+math.sqrt(delta))/(2*a)),end=' ')
            print('x2 = %.2f'%((-b-math.sqrt(delta))/(2*a)))
main()
#线性枚举解决二元一次方程
def main():
    import random
    a = float(input('请输入a：'))
    b = float(input('请输入b：'))
    while True:
        x = random.randint(1,10)#随机生成1-10的整数
        y = random.randint(1,10)
        if x*y == a  and x+y==b:
            print(x,y)
            break
main()
            

def main(a,b):
    import random
    while True:
     x=random.uniform(0,10)#生成0~a的随机数
     y=random.uniform(0,10)
     if x+y==a and x*y==b:
            print(x,y) 
            break
        
main(8,12)

#求解一元一次方程
def solv(func):#func是一个字符串类，可以做解析  如：'x**2+2x+1=0'
    p1,p2 = func.split('=')
    a1,a2 = p1.split('x')
   
    if a2 == '':
        a2=0
    x= (float(p2)-float(a2))/float(a1) 
    print(x)
solv('3x+2=-1')
#求解二元一次方程
def getParm(func):
    p1,p2 = func.split('=')
    a1,a2 = p1.split('x')
    b1,b2 = a2.split('y')
    if b2 == '':
        b2=0
    return float(a1),float(b1),float(b2),float(p2)
def solv2(func1,func2):
    a1,b1,c1,d1 = getParm(func1)
    a2,b2,c2,d2 = getParm(func2)
    x = ((d1-c1)*b2-(d2-c2)*b1)/(a1*b2-a2*b1)
    y = ((d1-c1)*a2-(d2-c2)*a1)/(-a1*b2+a2*b1)
    print(x,y)
solv2('3x+2y+1=2','2x+1y+1=1')
#求解三元一次方程（没有调试）
def getParm(func):
    p1,p2 = func.split('=')
    a1,a2 = p1.split('x')
    b1,b2 = a2.split('y')
    c1,c2 = b2.split('z')
    if c2 == '':
        c2=0
    return float(a1),float(b1),float(c1),float(p2)
def solv3(func1,func2,func3):
    a1,b1,c1,d1 = getParm(func1)
    a2,b2,c2,d2 = getParm(func2)
    a3,b3,c3,d3 = getParm(func3)
    x = ((d1-c1)*b2*c3-(d2-c2)*b1*c3-(d3-c3)*b1*c2)/(a1*b2*c3-a2*b1*c3-a3*b1*c2)
    y = ((d1-c1)*a2*c3-(d2-c2)*a1*c3-(d3-c3)*a1*c2)/(-a1*b2*c3+a2*b1*c3+a3*b1*c2)
    z = ((d1-c1)*a2*b3-(d2-c2)*a1*b3-(d3-c3)*a1*b2)/(a1*a2*c3-a1*a3*c2-a2*a3*c1)
    print(x,y,z)
solv3('3x+2y+1z+2=2','2x+1y+1z+1=1','1x+1y+1z+1=1')
#求解一元二次方程
def getParm(func):
    p1,p2 = func.split('=')
    a1,a2 = p1.split('x^2+')
    b1,b2 = a2.split('x')
    if a1=='':
        a1=1
    if b2=='':
        b2=0
    return float(a1),float(b1),float(b2),float(p2)
def solv4(func):
    a,b,c,d = getParm(func)
    dt=b*b-4*a*(c-d)
    if dt>=0:
     x1 = (-b+dt**(1/2))/(2*a)
     x2 = (-b-dt**(1/2))/(2*a)
     print(x1,x2)
     return x1,x2
    else:
      print('无解')

solv4('3x^2+60x+7=0')


    
#线性同余随机数
# ?range(start,stop)生成start~stop的整数
#uniform(start,stop)#生成start~stop的随机浮点数
#randint(start,stop)#生成start~stop的随机整数
#randrange(start,stop,step)#生成start~stop的随机整数，step为步长
#random()#生成0~1的随机浮点数   
#seed(x)#设置随机数种子
#shuffle(x)#将x的元素随机排序
#choice(x)#从x中随机选取一个元素
#sample(x,n)#从x中随机选取n个元素
#已和任意数相乘的方式生成随机数  如：random.randrange(1,10,2)
#random.randint(1,10)
#已知不在同一直线上三点坐标，求圆心坐标
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
 
def getCircle(p1, p2, p3):
    x21 = p2.x - p1.x
    y21 = p2.y - p1.y
    x32 = p3.x - p2.x
    y32 = p3.y - p2.y
    # three colinear
    if (x21 * y32 - x32 * y21 == 0):
        return None
    xy21 = p2.x * p2.x - p1.x * p1.x + p2.y * p2.y - p1.y * p1.y
    xy32 = p3.x * p3.x - p2.x * p2.x + p3.y * p3.y - p2.y * p2.y
    y0 = (x32 * xy21 - x21 * xy32) / (2 * (y21 * x32 - y32 * x21))
    x0 = (xy21 - 2 * y0 * y21) / (2.0 * x21)
    R = ((p1.x - x0) ** 2 + (p1.y - y0) ** 2) ** 0.5
    return x0, y0, R
 
 
p1, p2, p3 = Point(0, 0), Point(-4, 0), Point(0, -4)
print(getCircle(p1, p2, p3))
#

di={'a':1,'b':4,'c':3,'d':3}
di1=(sorted(di.items(),key=lambda x:x[1],reverse=True))#按照value值进行排序
di2=(sorted(di,key=lambda x:di[x],reverse=True))#按照key值进行排序
print(di1)
#排序赋值一
a=3 
b=2
c=1
d=4
e=5
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if a>d:
    a,d=d,a
if a>e:
    a,e=e,a
if b>c:
    b,c=c,b
if b>d:
    b,d=d,b
if b>e:
    b,e=e,b
if c>d:
    c,d=d,c
if c>e:
    c,e=e,c
if d>e:
    d,e=e,d
print(a,b,c,d,e)
#?排序赋值二
a=3 
b=2
c=1
d=6
e=5
a,b,c,d,e={a,b,c,d,e}#解包赋值 变量个数必须和包内的键值对个数相同
print(a,b,c,d,e)
a,b,c,d,e=sorted([a,b,c,d,e],reverse=True)#!排序赋值三 置换赋值
print(a,b,c,d,e)

a=98764433




#欢迎使用Python脚本编辑器！我的一小步，人类一大步！
#@File    :   demo1.py
#@Time    :   2022/04/19 23:25:21
#@Author  :   flow-laic 
#@Email   :

from email import header


header_charset = 'ISO-8859-1'
from asyncore import file_dispatcher
from base64 import encode
from urllib import request

#encode('utf-8')
a=100
sdf=200


def f():
    a=200
    print(a)
    if __name__=='__main__':
    
      print('b',sdf)
    return a


f()
#系统库
import sys
print(sys.path)
#自定义库
import urllib#
print(urllib.request.urlopen('http://www.baidu.com').read())
#time
import time
print(time.localtime(time.time()))
import sched#一定间隔执行
import time
def job():
    print('I am job')
    print(time.localtime(time.time()))
    s.enter(10,1,job)
s=sched.scheduler(time.time,time.sleep)
s.enter(3,1,job)
s.run()

import sched#!一定间隔执行
import time
if __name__=='__main__':# 只有在当前模块被直接执行时才会执行调用
 def job2():
    print('I am job2') 
    s.enter(3,1,job2)
s=sched.scheduler(time.time,time.sleep)
s.enter(3,1,job2)
s.run()
#pip intall requests 
from urllib import request
print(request.get('http://www.baidu.com'))
#读取文件
f=open('/Users/xkg/Documents/GitHub/-1/1/pageage/test.txt','r')
print(f.readline())
f.close()
#读取文件2
with open('/Users/xkg/Documents/GitHub/-1/1/pageage/test.txt','r') as f:
    print(f.read())




#写入文件
b=open('/Users/xkg/Documents/GitHub/-1/1/pageage/test.txt','a+')
b.write('good')
print('good,hello world',file=b)#任何语句都可赋值给=，也可以print
b.close()
















