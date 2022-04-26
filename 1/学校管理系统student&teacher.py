#欢迎使用Python脚本编辑器！我的一小步，人类一大步！
#@File    :   学校管理系统student&teacher.py
#@Time    :   2022/04/26 11:28:57
#@Author  :   flow-laic 
def main():
    while True:
        print("\t\t\t欢迎使用学校管理系统！")
        print("\t\t\t1.进入学生管理系统")
        print("\t\t\t2.进入教师管理系统")
        print("\t\t\t3.退出系统")
        
        try:
            choice = int(input("请输入您的选择："))
            if choice == 1:
                import 学生信息录入系统student
                main()
            elif choice == 2:
                import 教师信息录入系统teacher
                main()
            elif choice == 3:
                print("欢迎下次使用！")
                break
            else:
                print("输入错误！")
        except ValueError:
            print("输入错误！")
            
         
main()      
         
         
         
         
         
         
         
         
         
         
         