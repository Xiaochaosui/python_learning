import sys
def show():
    print("=" * 20+"欢迎使用穗少ATM自助存款系统"+"="*20)
    print("\t"*5+"1.登陆系统")
    print("\t"*5+"2.注册账户")
    print("\t"*5+"3.退出系统")
    print("=" * 20+"欢迎使用穗少ATM自助存款系统"+"="*20)
def login(np):
    name = input("请输入用户名:")
    if name not in np.keys():
        print("您输入的用户名不存在")
    else:
        pd = input("请输入密码:")
        if pd ==np[name]:
            print("登陆成功!")
def register(np):
    name = input("请输入用户名:")
    if name in np.keys():
        print("您输入的用户名已存在")
    else:
        pd1 = input("请输入6位数的数字密码:")
        if pd1.isdigit() and len(pd1) == 6:
            pd2 = input("请再次输入6位数的数字密码:")
            if pd1==pd2:
                np[name] = pd1
                print("注册成功！")
            else:
                print("两次密码输入不一致!")

def search(np):
    for items in np.items():
         print("用户名:"+items[0]+" 密码:"+items[1])

def tuichu():
    print("欢迎再次使用本ATM！(●'◡'●)")
    sys.exit()

def panduan(str,np):
    if str == '1':
        login(np)  # 登陆系统
    elif str == '2':
        register(np)  # 注册账户
    elif str == '3':
        tuichu()  # 退出系统
    elif str == '4':
        search(np)  # 退出系统
    else:
        print("您的操作有误")
if __name__ == '__main__':
    np = {}
    while 1:
        show()
        str = input("请输入操作:")
        panduan(str,np)