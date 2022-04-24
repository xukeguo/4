#欢迎使用Python脚本编辑器！我的一小步，人类一大步！
#@File    :   学生信息管理系统.py
#@Time    :   2022/04/23 21:53:56
#@Author  :   flow-laic 
#@Email   :
from errno import ESTALE


def main():
    print('+++++++++++++++++++++++学生信息管理系统+++++++++++++++++++++++')
    while True:
        print('\t\t\t1.添加学生信息')#!添加学生信息"\t\t\t\t\t\"表示空格
        print('\t\t\t2.查找学生信息')
        print('\t\t\t3.显示学生信息')
        print('\t\t\t4.统计学生总人数')
        print('\t\t\t5.删除学生信息')
        print('\t\t\t6.修改学生信息')
        print('\t\t\t7.排序')
        print('\t\t\t8.退出系统')
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
    while True:
        name = input('请输入学生姓名：如果输入q，则结束添加：')
        if name == 'q':
            break
        age = int(input('请输入学生年龄：'))
        score = int(input('请输入学生成绩：'))
        student = {'name':name,'age':age,'score':score}
        with open('/Users/xkg/Desktop/student2.txt','a') as f:
            f.write(str(student)+'\n')

def find_student():
    name = input('请输入学生姓名：')
    with open('/Users/xkg/Desktop/student2.txt','r') as f:
        for line in f:#遍历文件
            student = eval(line)#!eval()函数将字符串转换为字典
            if student['name'] == name:
                print('学生信息：%s 年龄：%d 成绩：%d'%(student['name'],student['age'],student['score']))
                break
            else:
                print('没有找到该学生,返回主菜单重新输入')
def show_student():
    with open('/Users/xkg/Desktop/student2.txt','r') as f:
        for line in f:
            student = eval(line)
            print('学生信息：%s 年龄：%d 成绩：%d'%(student['name'],student['age'],student['score']))
def count_student():
    count = 0
    with open('/Users/xkg/Desktop/student2.txt','r') as f:
        for line in f:
            count += 1
    print('学生总人数：',count)
def delete_student():
    import os
    name = input('请输入学生姓名：')
    with open('/Users/xkg/Desktop/student2.txt','r') as f1:
        with open('tmp.txt','w') as f2:
            for line in f1:
                student = eval(line)
                if student['name'] != name:
                    f2.write(str(student)+'\n')
    os.remove('/Users/xkg/Desktop/student2.txt')
    os.rename('tmp.txt','/Users/xkg/Desktop/student2.txt')
    print('删除成功')
def update_student():
    import os
    name = input('请输入学生姓名：')
    with open('/Users/xkg/Desktop/student2.txt','r') as f1:
        with open('tmp.txt','w') as f2:
            for line in f1:
                student = eval(line)
                if student['name'] == name:
                    student['score'] = int(input('请输入学生成绩：'))
                    student['age'] = int(input('请输入学生年龄：'))
                f2.write(str(student)+'\n')
    os.remove('/Users/xkg/Desktop/student2.txt')
    os.rename('tmp.txt','/Users/xkg/Desktop/student2.txt')
def sort_student():
    with open('/Users/xkg/Desktop/student2.txt','r') as f:
        students = []
        for line in f:
            student = eval(line)
            students.append(student)
    students.sort(key=lambda x:x['score'],reverse=True)
    print(students)
if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# Path: 2/学生信息管理系统.py