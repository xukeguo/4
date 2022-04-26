# 欢迎使用Python脚本编辑器！我的一小步，人类一大步！
# @File    :   学生信息录入系统2.py
# @Time    :   2022/04/23 21:54:16
# @Author  :   flow-laic
# @Email   :



def main():
    print('{:^76}'.format('学生信息管理系统'))
    while True:
        print('{:^76}'.format('1.添加学生信息') )    # !添加学生信息"\t\t\t\t\t\"表示空格
        print('{:^76}'.format(' 2.查找学生信息'))
        print('{:^76}'.format(' 3.显示学生信息'))
        print('{:^76}'.format(' 4.统计学生总人数'))
        print('{:^76}'.format(' 5.删除学生信息'))
        print('{:^76}'.format(' 6.修改学生信息'))
        print('{:^76}'.format('  7.排序      '))
        print('              \t\t\t  8.退出系统') 
        print('{:^76}'.format('   请选择（1-8）：'))
        try:
            choice = int(input())
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
            modify_student()
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
            try:
                name = input('请输入学生姓名：')
                if name == '':
                    print('姓名不能为空，请重新输入')
                    break
                id = input('请输入学生学号：')
                if id == '':
                    print('学号不能为空，请重新输入')
                    break
                age = int(input('请输入学生年龄：'))
                engscore = int(input('请输入学生英语成绩：'))
                mathscore = int(input('请输入学生数学成绩：'))
                if engscore < 0 or engscore > 100 or mathscore < 0 or mathscore > 100:
                 print('成绩必须在0-100之间')
                 continue
            except ValueError:  # 判断输入的是否是数字
                print('成绩必须为数字!')
                continue
            except TypeError:   # 判断输入的是否是数字
                print('成绩必须为数字')
                continue

            # print('姓名：%s\n学号：%s\n年龄：%s\n英语成绩：%s\n数学成绩：%s'%(name,id,age,engscore,mathscore))录入字典
            stu_dict = {'姓名': name, '学号': id, '年龄': age,
                '英语成绩': engscore, '数学成绩': mathscore}
            stu_lista.append(stu_dict)
            answer = input('是否继续录入？（y/n）\n')
            if answer == 'n':
                break
     save(stu_lista)
     print('录入成功')
def find_student():
       import os
       stu_listf = []
       if os.path.exists('student.txt'):
           flag= 1
           while flag<100:
                flag+=1
                try:
                    a = int(input('请输入1：按学号查找\n2：按姓名查找\n3：按年龄查找\n4：按英语成绩查找\n5：按数学成绩查找\n'))#输入查找方式
            
                    if a == 1:
                        b = input('请输入学生学号：')
                        with open('student.txt', 'r', encoding='utf-8') as stu_txt:
                            for i in stu_txt:
                                dict_stu = eval(i)
                                if b == dict_stu['学号']:
                                    stu_listf.append(dict_stu)
                                    print('{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}'.format(
                                        '姓名', '学号', '年龄', '英语成绩', '数学成绩', '总分'))
                                    print('{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}'.format(
                                        dict_stu['姓名'],    dict_stu['学号'], dict_stu['年龄'], dict_stu['英语成绩'], dict_stu['数学成绩'], int(dict_stu['英语成绩'])+int(dict_stu['数学成绩'])))
                                    break
                            else:
                                print('没有找到！')
                    elif a == 2:
                        b = input('请输入学生姓名：')
                        with open('student.txt', 'r', encoding='utf-8') as stu_txt:
                            for i in stu_txt:
                                dict_stu = eval(i)
                                if b == dict_stu['姓名']:
                                    stu_listf.append(dict_stu)
                                    print('{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}'.format(
                                        '姓名', '学号', '年龄', '英语成绩', '数学成绩', '总分'))
                                    print('{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}'.format(
                                        dict_stu['姓名'],    dict_stu['学号'], dict_stu['年龄'], dict_stu['英语成绩'], dict_stu['数学成绩'], int(dict_stu['英语成绩'])+int(dict_stu['数学成绩'])))
                                    break
                            else:
                                print('没有找到！')
            
                    elif a == 3:
                        b = int(input('请输入学生年龄：'))
                        with open('student.txt', 'r', encoding='utf-8') as stu_txt:
                            for i in stu_txt:
                                dict_stu = eval(i)
                                if b == dict_stu['年龄']:
                                    stu_listf.append(dict_stu)
                                    print('{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}'.format(
                                        '姓名', '学号', '年龄', '英语成绩', '数学成绩', '总分'))
                                    print('{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}'.format(
                                        dict_stu['姓名'],    dict_stu['学号'], dict_stu['年龄'], dict_stu['英语成绩'], dict_stu['数学成绩'], int(dict_stu['英语成绩'])+int(dict_stu['数学成绩'])))
                                    break
                            else:
                                print('没有找到！')
            
                    elif a == 4:
                        try:
                            b = int(input('请输入学生英语成绩：'))
                            with open('student.txt', 'r', encoding='utf-8') as stu_txt:
                                for i in stu_txt:
                                    dict_stu = eval(i)
                                    if b == dict_stu['英语成绩']:
                                        stu_listf.append(dict_stu)
                                        print('{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}'.format(
                                        '姓名', '学号', '年龄', '英语成绩', '数学成绩', '总分'))
                                        print('{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}'.format(
                                        dict_stu['姓名'],    dict_stu['学号'], dict_stu['年龄'], dict_stu['英语成绩'], dict_stu['数学成绩'], int(dict_stu['英语成绩'])+int(dict_stu['数学成绩'])))
                                    break
                                else:
                                    print('没有找到！')
                        except:
                            print('输入错误！')
                    elif a == 5:
                        try:
                            b = int(input('请输入学生数学成绩：'))
                            with open('student.txt', 'r', encoding='utf-8') as stu_txt:
                                for i in stu_txt:
                                    dict_stu = eval(i)
                                    if b == dict_stu['数学成绩']:
                                        stu_listf.append(dict_stu)
                                        print('{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}'.format(
                                        '姓名', '学号', '年龄', '英语成绩', '数学成绩', '总分'))
                                        print('{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}'.format(
                                        dict_stu['姓名'],    dict_stu['学号'], dict_stu['年龄'], dict_stu['英语成绩'], dict_stu['数学成绩'], int(dict_stu['英语成绩'])+int(dict_stu['数学成绩'])))
                                    break
                                else:
                                    print('没有找到！')
                        except:
                            print('输入错误！')
                    else:
                        print('输入错误！')
                except :      
                   print('请输入数字！')
                answer=input('是否继续查询？（y/n）')
                if answer=='n':
                 return stu_listf
                else:
                      continue
       else:
           print('还没有学生信息！')
def show_student():
    import os
    if os.path.exists('student.txt'):
       
       stu_lists=[]
       try:
           stu_txt=open('student.txt','r',encoding='utf-8')
       except:
           stu_txt=open('student.txt','r',encoding='utf-8')
       for i in stu_txt:
           stu_lists.append(eval(i))
       stu_txt.close()
       # print (stu_lists[0]['姓名'])如果要显示最大或最小值，可以先排序再显示第一个索引
       print('{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}'.format( '姓名', '学号', '年龄', '英语成绩', '数学成绩', '总分'))
       for i in stu_lists:
           print('{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}'.format(i['姓名'], i['学号'], i['年龄'], i['英语成绩'], i['数学成绩'], int(i['英语成绩'])+int(i['数学成绩'])))
    else:
           print('没有学生信息！')
def count_student():
    import os
    if os.path.exists('student.txt'):
       
       stu_listc=[]
       try:
           stu_txt=open('student.txt','r',encoding='utf-8')
       except:
           stu_txt=open('student.txt','r',encoding='utf-8')
       for i in stu_txt:
           stu_listc.append(eval(i))
       stu_txt.close()
       print('学生总人数：%s'%len(stu_listc))
    else:
              print('没有学生信息！')
def delete_student():
      import os
      if os.path.exists('student.txt'):
     
         stu_listd=[]
         try:
             stu_txt=open('student.txt','r',encoding='utf-8')
         except:
             stu_txt=open('student.txt','r',encoding='utf-8')
         for i in stu_txt:
             stu_listd.append(eval(i))
         stu_txt.close()
         while True:
                    name=input('请输入删除学生姓名：')
                    for i in stu_listd:
                        if i['姓名']==name:
                            stu_listd.remove(i)
                            with open('student.txt','w',encoding='utf-8') as file1:
                                for i in stu_listd:
                                    file1.write(str(i)+'\n')
                            print('删除成功')
                            break
                    else:
                        print('没有找到该学生')
                    a=input('是否继续删除？（y/n）')#删除多个学生
                    if a!='y':
                        break
      else:
           print('没有找到！')
def modify_student():
    import os
    if os.path.exists('student.txt'):
       stu_listm=[]
       try:
           stu_txt=open('student.txt','r',encoding='utf-8')
       except:
           stu_txt=open('student.txt','r',encoding='utf-8') 
       for i in stu_txt:
           stu_listm.append(eval(i))
       stu_txt.close()
       while True:
           name=input('请输入修改学生姓名：')
           for i in stu_listm:
               if i['姓名']==name: 
                   print('姓名\t学号\t年龄\t英语成绩\t数学成绩')
                   print('{:<4}\t{:<4}\t{:<4}\t{:<4}\t{:<4}'.format(i['姓名'],i['学号'],i['年龄'],i['英语成绩'],i['数学成绩']))
                   while True:
                       try:
                           num=int(input('请输入要修改的学生信息：1.学号 2.年龄 3.英语成绩 4.数学成绩'))
                           if num==1:
                               i['学号']=input('请输入学号：')
                           elif num==2:
                               i['年龄']=int(input('请输入年龄：'))
                           elif num==3:
                               i['英语成绩']=int(input('请输入英语成绩：'))
                           elif num==4:
                               i['数学成绩']=int(input('请输入数学成绩：'))
                           else:
                               print('输入错误！')
                               continue
                       except:
                           print('输入错误！')
                       answer=input('是否继续修改%s？（y/n）'%i['姓名'])
                       if answer=='n':
                            break
                   with open('student.txt','w',encoding='utf-8') as file1:
                            for i in stu_listm:
                                file1.write(str(i)+'\n')
                            print('修改成功')
                            break
           else:
                print('没有找到该学生')
           a=input('是否继续修改其他学生？（y/n）')
           if a!='y':
                    break
    else:
            print('没有学生信息！')
def update_student():
 import os
 if os.path.exists('student.txt'):

    stu_listu=[]
    try:
        stu_txt=open('student.txt','r',encoding='utf-8')
    except:
        stu_txt=open('student.txt','w',encoding='utf-8')
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
    file3=open('student.txt','w',encoding='utf-8')
    for i in stu_listu:
        file3.write(str(i)+'\n')
    file3.close()
    print('修改成功')
def sort_student():
    import os
    if os.path.exists('student.txt'):
   
       stu_lists=[]
       try:
           stu_txt=open('student.txt','r',encoding='utf-8')
       except:
           stu_txt=open('student.txt','w',encoding='utf-8')
       for i in stu_txt:
           stu_lists.append(eval(i))#将文件中的字符串转换成字典
       stu_txt.close()
       try:
           num1=int(input('请输入排序方式：1.按学号排序；2.按年龄排序；3.按英语成绩排序；4.按数学成绩排序；5.按总成绩排序'))
       except:
           print('输入错误，请重新输入')
       if num1==1:
              a1=input('请输入排序方式：1.升序；2.降序')
              if a1=='1':
                 stu_lists.sort(key=lambda x:x['学号'])
              elif a1=='2':
                 stu_lists.sort(key=lambda x:x['学号'],reverse=True)
              else:
                    print('输入错误，请重新输入')
       elif num1==2:
                a2=input('请输入排序方式：1.升序；2.降序')
                if a2=='1':
                     stu_lists.sort(key=lambda x:x['年龄'])
                elif a2=='2':
                    stu_lists.sort(key=lambda x:x['年龄'],reverse=True)
                else:
                    print('输入错误，请重新输入')
       elif num1==3:
                a3=input('请输入排序方式：1.升序；2.降序')
                if a3=='1':
                     stu_lists.sort(key=lambda x:x['英语成绩'],)
                elif a3=='2':
                    stu_lists.sort(key=lambda x:x['英语成绩'],reverse=True)
                else:
                    print('输入错误，请重新输入')
       elif num1==4:
                a4=input('请输入排序方式：1.升序；2.降序')
                if a4=='1':
                     stu_lists.sort(key=lambda x:x['数学成绩'])
                elif a4=='2':
                    stu_lists.sort(key=lambda x:x['数学成绩'],reverse=True)
                else:
                    print('输入错误，请重新输入')
       elif num1==5:
                a5=input('请输入排序方式：1.升序；2.降序')
                if a5=='1':
                     stu_lists.sort(key=lambda x:x['英语成绩']+x['数学成绩'])
                elif a5=='2':
                    stu_lists.sort(key=lambda x:x['英语成绩']+x['数学成绩'],reverse=True)
                else:
                    print('输入错误，请重新输入')
       else:
           print('输入错误，请重新输入，返主菜单层')
           return
       file4=open('student.txt','w',encoding='utf-8')
       for i in stu_lists:
           file4.write(str(i)+'\n')
       file4.close()
       print('排序成功,请在显示学生信息查看')  

    else:
           print('没有学生信息！')
def save(lis):
        try:
           stu_txt=open('student.txt','a',encoding='utf-8')#追加
        except:
           stu_txt=open('student.txt','w',encoding='utf-8')#注意windows下的路径用的/，而不是\  如果是w模式，则会清空原来的内容  如果是a模式，则会追加    如果是r模式，则不能追加  如果是w+模式，则会清空原来的内容  如果是a+模式，则会追加 带+与不带+的区别是：带+的是在原来的内容上追加，不带+的是在原来的内容上添加，添加与追加的区别是：添加是在原来的内容上添加，追加是在原来的内容上追加   
        for i in lis:
               stu_txt.write(str(i)+'\n')#+'\n'什么意思？  字典转字符串 
        stu_txt.close()
        




main()        



         
