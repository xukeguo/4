#欢迎使用Python脚本编辑器！我的一小步，人类一大步！
#@File    :   学校管理系统student&teacher.py
#@Time    :   2022/04/26 11:28:57
#@Author  :   flow-laic 
def main():
    while True:
        print("\t\t\t欢迎使用学校管理系统！")
        print("\t\t\t1.进入学生管理系统")
        print("\t\t\t2.进入教师管理系统")
        print("\t\t\t3.修改密码")
        print("\t\t\t4.退出系统")
        
        try:
            choice = int(input("请输入您的选择："))
            if choice == 1:
                import 学生信息录入系统student
                main()
            elif choice == 2:
                import 教师信息录入系统teacher
                main()
            elif choice == 3:
                student_change_password()
            elif choice == 4:
                print("欢迎下次使用！")
                break
            else:
                print("输入错误！")
        except ValueError:
            print("输入错误！")

def  student_change_password():
    while True:
        new = input('请输入新密码：')
        if new == '':
            print('密码不能为空，请重新输入')
            break
        if new=='123456':
            print('密码不能为123456，请重新输入')
            break
        if new.isalnum()==False:
            print('密码必须为数字或字母，请重新输入')
            break
        if len(new)<6:
            print('密码长度不能小于6位，请重新输入')
            break
        if len(new)>12:
            print('密码长度不能大于12位，请重新输入')
            break
        if new.isdigit()==True:
            print('密码不能为纯数字，请重新输入')
            break
        if new.isalpha()==True:
            print('密码不能为纯字母，请重新输入')
            break
       # if new.islower()==True:
        #    print('密码不能为纯小写字母，请重新输入')
         #   break
        if new.isupper()==True:
            print('密码不能为纯大写字母，请重新输入')
            break
        if new.count('a')>=2:
            print('密码不能为a或aa，请重新输入')
            break
        else:
            new2 = input('请再次输入新密码：')
            if new2 == '':
                print('密码不能为空，请重新输入')
                break
            if new2 == new:
               with open('student_info.txt', 'w') as f:
                  f.write(str(new))
                  print('密码修改成功！')
                  break
            
         
def student_in():
    with open('student_info.txt', 'a') as f:
     with open('student_info.txt', 'r') as f1:
        a = f1.readlines()
        if len(a) == 0:
            a1=0
            while a1 <6:
              a1+=1
              print("\t\t\t欢迎使用学校管理系统！")
              print("\t\t\t首次使用请输入初始密码！咨询徐校长！")
              password = 123456#有初始密码
              try:
                  b1 = int(input('请输入密码：'))
                  if b1==password:
                      f.write(str(password))
                      print('登录成功！')
                      main()
                      return None
                  else:
                      print('密码错误！')
                      continue
              except ValueError:
                    print('密码错误！')
                    continue
            print('欢迎下次光临！')
        else:
          print('\t\t\t欢迎使用学校管理系统！')
          print("\t\t\t请输入初始登录！")
          flags1 = 0
          while   flags1<3:
                   flags1 += 1
                   try:
                       with open('student_info.txt', 'r') as f:
                           password = f.read()
                       password1 = input('请输入密码：')
                       if password1 == '':
                           print('密码不能为空，请重新输入')
                           #break
                       #if password == '123456':
                          # print('密码不能为123456，请重新输入')
                          # break
                       if password1.isalnum() == False:
                           print('密码必须为数字或字母，请重新输入')
                           #break
                       if len(password1) < 6:
                           print('密码长度不能小于6位，请重新输入')
                           #break
                       if len(password1) > 12:
                           print('密码长度不能大于12位，请重新输入')
                           #break
                       #if password.isdigit() == True:
                           #print('密码不能为纯数字，请重新输入')
                           #break
                       if password1.isalpha() == True:
                           print('密码不能为纯字母，请重新输入')
                           #break
                       #if password.islower() == True:
                         #  print('密码不能为纯小写字母，请重新输入')
                         #  break
                       if password1.isupper() == True:
                           print('密码不能为纯大写字母，请重新输入')
                           #break
                       if password1.count('a') >= 2:
                           print('密码不能为a或aa，请重新输入')
                           #break
                       else:
                           if password1 == password:
                               print('登录成功！')
                               main()
                               return None
                           else:
                               print('密码错误，请重新输入')
                              # break
                   except:
                       print('密码错误，请重新输入')
                      # break

        
student_in()








         
         
         
         
         
         
         
         
         
         
         