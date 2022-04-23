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
        num = int(input('请输入您的选择：'))
        if num == 1:
            add_student()
        elif num == 2:
            find_student()
        elif num == 3:
            show_student()
        elif num == 4:
            count_student()
        elif num == 5:
            delete_student()
        elif num == 6:
            update_student()
        elif num == 7:
            sort_student()
        elif num == 8:
            break
        else:
            print('输入错误，请重新输入')
def add_student():
     stu_list = []
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
                    print('成绩不能为负数或大于100')
            except:
                print('成绩必须为数字')
                continue
            #print('姓名：%s\n学号：%s\n年龄：%s\n英语成绩：%s\n数学成绩：%s'%(name,id,age,engscore,mathscore))录入字典
            stu_dict={'姓名':name,'学号':id,'年龄':age,'英语成绩':engscore,'数学成绩':mathscore}
            stu_list.append(stu_dict)
            answer=input ('是否继续录入？（y/n）\n')
            if answer == 'n':
                break
     save(stu_list)
     print('录入成功')
def save(lis):
        try:
           stu_txt=open('/Users/xkg/Desktop/student.txt','a',encoding='utf-8')
        except:
           stu_txt=open('/Users/xkg/Desktop/student.txt','w',encoding='utf-8')
        for i in lis:
               stu_txt.write(str(i)+'\n')
        stu_txt.close()
def find_student():
    stu_list=[]
    try:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    except:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    for i in stu_txt:
        stu_list.append(eval(i))
    stu_txt.close()
    name=input('请输入查找学生姓名：')
    for i in stu_list:
        if i['姓名']==name:
            print('姓名：%s\n学号：%s\n年龄：%s\n英语成绩：%s\n数学成绩：%s'%(i['姓名'],i['学号'],i['年龄'],i['英语成绩'],i['数学成绩']))
            break
    else:
        print('没有找到该学生')
def show_student():
    stu_list=[]
    try:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    except:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    for i in stu_txt:
        stu_list.append(eval(i))
    stu_txt.close()
    for i in stu_list:
        print('姓名：%s\n学号：%s\n年龄：%s\n英语成绩：%s\n数学成绩：%s'%(i['姓名'],i['学号'],i['年龄'],i['英语成绩'],i['数学成绩']))
def count_student():
    stu_list=[]
    try:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    except:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    for i in stu_txt:
        stu_list.append(eval(i))
    stu_txt.close()
    print('学生总人数：%s'%len(stu_list))
def delete_student():
    stu_list=[]
    try:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    except:
        stu_txt=open('/Users/xkg/Desktop/student.txt','w',encoding='utf-8')
    for i in stu_txt:
        stu_list.append(eval(i))
    stu_txt.close()
    name=input('请输入删除学生姓名：')
    for i in stu_list:
        if i['姓名']==name:
            stu_list.remove(i)
            break
    else:
        print('没有找到该学生')
    save(stu_list)
    print('删除成功')
def modify_student():
    stu_list=[]
    try:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    except:
        stu_txt=open('/Users/xkg/Desktop/student.txt','w',encoding='utf-8') 
    for i in stu_txt:
        stu_list.append(eval(i))
    stu_txt.close()
    name=input('请输入修改学生姓名：')
    for i in stu_list:
        if i['姓名']==name:
            i['学号']=input('请输入学生学号：')
            i['年龄']=input('请输入学生年龄：')
            i['英语成绩']=input('请输入学生英语成绩：')
            i['数学成绩']=input('请输入学生数学成绩：')
            break
    else:
        print('没有找到该学生')
    save(stu_list)
    print('修改成功')
def update_student():
    stu_list=[]
    try:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    except:
        stu_txt=open('/Users/xkg/Desktop/student.txt','w',encoding='utf-8')
    for i in stu_txt:
        stu_list.append(eval(i))
    stu_txt.close()
    name=input('请输入修改学生姓名：')
    for i in stu_list:
        if i['姓名']==name:
            i['学号']=input('请输入学生学号：')
            i['年龄']=input('请输入学生年龄：')
            i['英语成绩']=input('请输入学生英语成绩：')
            i['数学成绩']=input('请输入学生数学成绩：')
            break
    else:
        print('没有找到该学生')
    save(stu_list)
    print('修改成功')
def sort_student():
    stu_list=[]
    try:
        stu_txt=open('/Users/xkg/Desktop/student.txt','r',encoding='utf-8')
    except:
        stu_txt=open('/Users/xkg/Desktop/student.txt','w',encoding='utf-8')
    for i in stu_txt:
        stu_list.append(eval(i))
    stu_txt.close()
    stu_list.sort(key=lambda x:x['姓名'])
    save(stu_list)
    print('排序成功')



        