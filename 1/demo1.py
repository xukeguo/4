class a:
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print("a")

a1=a(1,2,3)
a2=a(4,5,6)
a3=a(7,8,9)
a5=a(10,11,12)
a4=a(13,14,15)
a6=a(16,17,18)

for x in list:
    print(x.x,x.y,x.z)
b1=123
b1=str(b1)
for i in b1:
    print(i)
b2=(4,5,6)
b3=(7,8,9)
b5=(10,11,12)
b4=(13,14,15)
a7=a(*b1)#*b1 is a tuple *可以解包 *可以解析元组 *可以解析列表 *可以解析字典 *可以解析集合 *可以解析字符串 **可以解析字典 **可以解析集合 **可以解析字符串
list=[a1,a2,a3,a4,a5,a6,a7]
lis1=[b1,b2,b3,b4,b5]
for x,y,z in lis1:
    print(x,y,z)
for x in list:
    print(x.x,x.y,x.z)



