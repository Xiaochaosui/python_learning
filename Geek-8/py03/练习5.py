# 通讯录
# Name   Tel
import sys
# function 功能



def show():
    print("="*6+"通讯录管理系统"+"="*6)
    print("1.增加姓名和手机号")
    print("2.删除姓名")
    print("3.修改手机")
    print("4.查询所有用户")
    print("5.根据姓名查找手机号")
    print("6.退出")
    print("="*19)
def add(Names,Tels):
    name = input("请输入名字:")
    tel = input("请输入手机号:")
    if len(list(tel)) ==11:
        Tels.append(tel)
        Names.append(name)
        print("添加成功")
    else:
        print("您的手机号输入错误，请输入正确的电话号码")

def delTel(Names, Tels):
    del_name = input("请输入删除人的名字:")
    if del_name in Names:
        for i in range(len(Names)):
            if del_name == Names[i] :
                del Names[i]
                del Tels[i]
                print("删除成功")
                break
    else:
        print("名字不存在")


def updateTel(Names, Tels):
    name = input("请输入要修改的名字:")
    if name in Names:
        for i in range(len(Names)):
            if name == Names[i]:
                tel = input("请输入"+name+"修改后的电话号码:")
                if len(list(tel)) == 11:
                    Tels[i] = tel
                    print("修改成功")
                    break
                else:
                    print("您的手机号输入错误，请输入正确的电话号码")
    else:
        print("名字不存在")
def searchTel(Names, Tels): # 查询所有用户
    for i in range(len(Names)):
        print("姓名:"+Names[i],"手机号:"+Tels[i])

def nameSearch(Names, Tels):
    name = input("请输入要修改的名字:")
    if name in Names:
        for i in range(len(Names)):
            if name == Names[i]:
                print("姓名:" + Names[i], "手机号:" + Tels[i])
    else:
        print("名字不存在,请先添加")

# sys  system 系统
def tuichu():
    sys.exit()
def store(Names,Tels):
    path = r"C:\Users\Administrator\Desktop\f"
    name = r"\n"
    tel =  r'\t'
    fileName = path + name + ".txt"
    fileTel = path + tel + ".txt"
    f1 = open(fileName, "w", encoding="utf-8")
    print(1)
    f2 = open(fileTel, "w", encoding="utf-8")
    for i in range(len(Names)):
        con1 = f1.write(Names[i] + "\n")
        con2 = f2.write(Tels[i] + "\n")
    f2.close()
    f1.close()

def panduan(str,Names,Tels):
    if str =='1':
        add(Names, Tels) #增加用户
    elif str == '2':
        delTel(Names,Tels) # 删除用户
    elif str =='3':
        updateTel(Names, Tels) # 修改用户手机号
    elif str =='4':
        searchTel(Names, Tels) # 查询所有用户
    elif str =='5':
        nameSearch(Names, Tels) # 按照姓名查找手机号
    elif str =='6':
        tuichu() # 退出
    else:
        print("您的操作有误")
    store(Names,Tels)
if __name__ == '__main__':# 两根下划线哈！！！
    Names = ['xcs','qwe','asd']
    Tels = ['17382865078','17282865078','17582865078']
    while 1:
        show()
        str = input("请输入操作:")
        panduan(str,Names,Tels)





