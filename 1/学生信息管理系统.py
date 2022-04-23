#欢迎使用Python脚本编辑器！我的一小步，人类一大步！
#@File    :   学生信息管理系统.py
#@Time    :   2022/04/23 21:53:56
#@Author  :   flow-laic 
#@Email   :
def main():
    print('学生信息管理系统')
    while True:
        print('\t\t\t\t\t\1.添加学生信息')#!添加学生信息"\t\t\t\t\t\"表示空格
        print('\t\t\t\t\t\2.查找学生信息')
        print('           3.显示学生信息')
        print('\t\t\t\t\t\4.统计学生总人数')
        print('\t\t\t\t\t\5.删除学生信息')
        print('\t\t\t\t\t\6.修改学生信息')
        print('\t\t\t\t\t\7.排序')
        print('\t\t\t\t\t\t8.退出系统')
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
    name = input('请输入学生姓名：')
    age = int(input('请输入学生年龄：'))
    score = int(input('请输入学生成绩：'))
    id = int(input('请输入学生学号：'))
    student = {'name':name,'age':age,'score':score,'id':id}
    with open('student.txt','a') as f:
        f.write(str(student)+'\n')

def find_student():
    name = input('请输入学生姓名：')
    with open('student.txt','r') as f:
        for line in f:
            student = eval(line)
            if student['name'] == name:
                print(student)
                break
def show_student():
    with open('student.txt','r') as f:
        for line in f:
            student = eval(line)
            print(student)
def count_student():
    count = 0
    with open('student.txt','r') as f:
        for line in f:
            count += 1
    print('学生总人数：',count)
def delete_student():
    name = input('请输入学生姓名：')
    with open('student.txt','r') as f1:
        with open('tmp.txt','w') as f2:
            for line in f1:
                student = eval(line)
                if student['name'] != name:
                    f2.write(str(student)+'\n')
    os.remove('student.txt')
    os.rename('tmp.txt','student.txt')
def update_student():
    name = input('请输入学生姓名：')
    with open('student.txt','r') as f1:
        with open('tmp.txt','w') as f2:
            for line in f1:
                student = eval(line)
                if student['name'] == name:
                    student['score'] = int(input('请输入学生成绩：'))
                f2.write(str(student)+'\n')
    os.remove('student.txt')
    os.rename('tmp.txt','student.txt')
def sort_student():
    with open('student.txt','r') as f:
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