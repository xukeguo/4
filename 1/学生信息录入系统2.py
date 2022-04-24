#欢迎使用Python脚本编辑器！我的一小步，人类一大步！
#@File    :   学生信息录入系统2.py
#@Time    :   2022/04/23 21:54:16
#@Author  :   flow-laic 
#@Email   :
def main():
    print('\t\t\t\t\t学生信息管理系统')
    while True:
        print('\t\t\t\t\t 1.添加学生信息')#!添加学生信息"\t\t\t\t\t\"表示空格
        print('\t\t\t\t\t 2.查找学生信息')
        print('\t\t\t\t\t 3.显示学生信息')
        print('\t\t\t\t\t 4.统计学生总人数')
        print('\t\t\t\t\t 5.删除学生信息')
        print('\t\t\t\t\t 6.修改学生信息')
        print('\t\t\t\t\t 7.排序')
        print('\t\t\t\t\t 8.退出系统')
        print('\t\t\t\t\t请选择（1-8）：')
        try:
            choice=int(input())
        except:
            print('请输入数字！')
            continue
        if choice == 1:
            add_student()
        elif choice == 2:
            find_student()
        elif choice == 3:
            show_student()
        elif choice == 4:
            count_student()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            update_student()
        elif choice == 7:
            sort_student()
        elif choice == 8:
            print('感谢使用！')
            break
        else:
            print('请输入正确的数字！')
def add_student():
     stu_lista = []
     while True:
            name = input('请输入学生姓名：')
            if name == '':
                print('姓名不能为空，请重新输入')
                break
            id=input('请输入学生学号：')
            if not id:
                print('学号不能为空')
                break
            age=input('请输入学生年龄：')
            if not age:
                print('年龄不能为空')
                break
            try:      
                engscore=int(input('请输入学生英语成绩：'))
                mathscore=int(input('请输入学生数学成绩：'))
                if engscore<0 or engscore>100 or mathscore<0 or mathscore>100:
                 print('成绩必须在0-100之间')
                 continue
               
            except ValueError:# 判断输入的是否是数字
                print('成绩必须为数字!')
                continue
            except TypeError:   # 判断输入的是否是数字 
                print('成绩必须为数字')
                continue
          
                
                
            #print('姓名：%s\n学号：%s\n年龄：%s\n英语成绩：%s\n数学成绩：%s'%(name,id,age,engscore,mathscore))录入字典
            stu_dict={'姓名':name,'学号':id,'年龄':age,'英语成绩':engscore,'数学成绩':mathscore}
            stu_lista.append(stu_dict)
            answer=input ('是否继续录入？（y/n）\n')
            if answer == 'n':
                break
     save(stu_lista)
     print('录入成功')
def find_student():
    stu_listf=[]
    try:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    except:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    for i in stu_txt:
        stu_listf.append(eval(i))#eval()函数将字符串转换为字典
    stu_txt.close()
    name=input('请输入查找学生姓名：')
    for i in stu_listf:
        if i['姓名']==name:
            print('姓名：%s\n学号：%s\n年龄：%s\n英语成绩：%s\n数学成绩：%s'%(i['姓名'],i['学号'],i['年龄'],i['英语成绩'],i['数学成绩']))
            break
    else:
        print('没有找到该学生')
def show_student():
    stu_lists=[]
    try:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    except:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    for i in stu_txt:
        stu_lists.append(eval(i))
    stu_txt.close()
    for i in stu_lists:
         print('姓名：%s\t学号：%s\t年龄：%s\t英语成绩：%s\t数学成绩：%s'%(i['姓名'],i['学号'],i['年龄'],i['英语成绩'],i['数学成绩']))
def count_student():
    stu_listc=[]
    try:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    except:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    for i in stu_txt:
        stu_listc.append(eval(i))
    stu_txt.close()
    print('学生总人数：%s'%len(stu_listc))
def delete_student():
    stu_listd=[]
    try:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    except:
        stu_txt=open('/Users/xkg/Desktop/student.txt','w',encoding='utf-8')
    for i in stu_txt:
        stu_listd.append(eval(i))
    stu_txt.close()
    name=input('请输入删除学生姓名：')
    for i in stu_listd:
        if i['姓名']==name:
            stu_listd.remove(i)
            with open('/Users/xkg/Desktop/student.txt','w',encoding='utf-8') as file1:
                for i in stu_listd:
                    file1.write(str(i)+'\n')
            print('删除成功')
            break
    else:
        print('没有找到该学生')
def modify_student():
    stu_listm=[]
    try:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    except:
        stu_txt=open('/Users/xkg/Desktop/student.txt','w',encoding='utf-8') 
    for i in stu_txt:
        stu_listm.append(eval(i))
    stu_txt.close()
    name=input('请输入修改学生姓名：')
    for i in stu_listm:
        if i['姓名']==name:
            i['学号']=input('请输入学生学号：')
            i['年龄']=input('请输入学生年龄：')
            i['英语成绩']=input('请输入学生英语成绩：')
            i['数学成绩']=input('请输入学生数学成绩：')
            break
    else:
        print('没有找到该学生')
    file2=open('/Users/xkg/Desktop/student.txt','w',encoding='utf-8')
    for i in stu_listm:
        file2.write(str(i)+'\n')
    file2.close()
    print('修改成功')
def update_student():
    stu_listu=[]
    try:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    except:
        stu_txt=open('/Users/xkg/Desktop/student.txt','w',encoding='utf-8')
    for i in stu_txt:
        stu_listu.append(eval(i))
    stu_txt.close()
    name=input('请输入修改学生姓名：')
    for i in stu_listu:
        if i['姓名']==name:
            i['学号']=input('请输入学生学号：')
            i['年龄']=input('请输入学生年龄：')
            i['英语成绩']=input('请输入学生英语成绩：')
            i['数学成绩']=input('请输入学生数学成绩：')
            break
    else:
        print('没有找到该学生')
    file3=open('/Users/xkg/Desktop/student.txt','w',encoding='utf-8')
    for i in stu_listu:
        file3.write(str(i)+'\n')
    file3.close()
    print('修改成功')
def sort_student():
    stu_lists=[]
    try:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    except:
        stu_txt=open('/Users/xkg/Desktop/student.txt','w',encoding='utf-8')
    for i in stu_txt:
        stu_lists.append(eval(i))#将文件中的字符串转换成字典
    stu_txt.close()
    try:
        num1=int(input('请输入排序方式：1.按学号排序；2.按年龄排序；3.按英语成绩排序；4.按数学成绩排序'))
    except:
        print('输入错误，请重新输入')
    if num1==1:
        stu_lists.sort(key=lambda x:x['学号'])
    elif num1==2:
        stu_lists.sort(key=lambda x:x['年龄'],reverse=True)
    elif num1==3:
        stu_lists.sort(key=lambda x:x['英语成绩'],reverse=True)
    elif num1==4:
        stu_lists.sort(key=lambda x:x['数学成绩'])
    else:
        print('输入错误，请重新输入，返主菜单层')
    file4=open('/Users/xkg/Desktop/student.txt','w',encoding='utf-8')
    for i in stu_lists:
        file4.write(str(i)+'\n')
    file4.close()
    print('排序成功,请在显示学生信息查看')
def save(lis):
        try:
           stu_txt=open('/Users/xkg/Desktop/student.txt','a',encoding='utf-8')#追加
        except:
           stu_txt=open('/Users/xkg/Desktop/student.txt','w',encoding='utf-8')
        for i in lis:
               stu_txt.write(str(i)+'\n')#+'\n'什么意思？  字典转字符串 
        stu_txt.close()


main()