a = 45454
b = str(a)
a1, a2, a3, a4, a5 = [ * b]
print(a1, a2, a3, a4, a5, sep = "*") #sep可以设置分隔符
print(a1, a2, a3, a4, a5, end = "\n") #end可以设置结束符
c = a1 * 2
print(c)
a = 45454 #获取个位数。。。。。。
b = str(a)
a1, a2, a3, a4, a5 = [int( * i) for i in b]#!我的统一转换成int赋值
c = a1 ** 2
print(c)
print(a1, a2, a3, a4, a5, sep = "*") #sep可以设置分隔符
print(a1, a2, a3, a4, a5, end = "\n") #end可以设置结束符

#间隔执行
import s
import time
def job ():
   print('哈哈')
   schedule.every (3).seconds.do (job)
while True:
  schedule.run_pending()
  time.sleep(1)