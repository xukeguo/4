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
import schedule
import time
def job ():
   print('哈哈')
   schedule.every (3).seconds.do (job)
while True:
  job()
   #schedule.run_pending()
  time.sleep(1)
  if time.time() > 10:
    break
  

import time#!计算时间差#间隔执行
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
       print('%02d:%02d:%02d'%(self._hour,self._minute,self._second))
       time.sleep(1)
a=Clock(23,59,59)
while True:
  a.run()
  if time.time() > 10:
    break
#累计递增问题
import time
class Clock(object):
    def __init__(self,hour=0,minute=0,second=0):
        self._hour=hour
        self._minute=minute
        self._second=second
        
a=Clock(23,59,59)

def run(self):
   a._hour=-1
   for i in range(24):
      self._hour+=1
      a._minute=-1   #!这里是累计递增，所以要设置为-1
      for j in range(60):
           self._minute+=1
           a._second=-1
           for k in range(60):
                   self._second+=1
                   print('%02d:%02d:%02d'%(self._hour,self._minute,self._second))
                   time.sleep(1) 
              
       
while True:
   run(a)
   if time.time() > 10:
        break
        