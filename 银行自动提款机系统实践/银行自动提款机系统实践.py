import  time
import pickle
import os
'''
人
类名：Person
属性：姓名 身份证号  电话号 卡
行为：

卡
类名：Card
属性：卡号  密码 余额
行为：

银行
类名：Bank
属性： 提款机
行为：

提款机
类名：ATM
属性：用户字典
行为：开户  查询  取款 存储 转账 改密 锁定  解锁  补卡  销户  退出

管理员
类名：Admin
属性:
行为: 管理员验证   管理员界面   系统功能界面
'''
from admin import Admin
from atm import ATM
def main():
    # 管理员对象
    admin = Admin()
    # 管理员开机
    admin.printAdminView()
    if admin.adminOption():
        print("登录失败！请稍后再试……")
        return -1
    # 创建提款机对象
    atm = ATM()
    fileDir = os.path.join(os.getcwd(), "data")
    if os.path.exists(fileDir):
        filePath = os.path.join(fileDir, "data.txt")
        with open(filePath, "rb") as f:
            atm.allUsers = pickle.load(f)




    while True:
        # 存储所有用户的信息
        admin.printSysFunctionView()
        # 等待用户操作
        option = input("请输入您的操作：")
        if option == "1":
            #开户
            atm.creatUser()
        elif option == "2":
            atm.searchUserInfo()
        elif option == "3":

            print("取款")
        elif option == "4":

            print("存款")
        elif option == "5":

            print("转账")
        elif option == "6":

            print("改密")
        elif option == "7":

            atm.lockUser()
        elif option == "8":

            atm.unlockUser()
        elif option == "9":

            print("补卡")
        elif option == "0":

            print("销户")
        elif option == "t":
            if not admin.adminOption(): #841968
                # 将当前系统中的用户保存到文件中
                fileDir = os.path.join(os.getcwd(), "data")
                if not os.path.exists(fileDir):
                    os.mkdir("data")
                file = os.path.join(fileDir, "data.txt")
                allUsersDict = atm.allUsers
                f = open(file, "wb")
                pickle.dump(allUsersDict, f)
                f.close()
                print("退出成功！")
                return -1
        time.sleep(2)




if __name__ == '__main__':
    main()
