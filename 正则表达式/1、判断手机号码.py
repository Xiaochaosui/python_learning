'''
给你一串字符串，判断是否是手机号码


'''
import re
def checkPhone(str):

    if len(str) != 11:
        return False
    elif str[0] != '1':
        return False
    for i in range(3,11):
        if str[i] > '9' or str[i] <'0':
            return False
    return True

def checkPhone2(str):
    #17382865078
    #93910385@qq.com
    pat1 = r"^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$"# 判断邮箱
    pat2 = r"^\w*\@\w*\.com$" # 判断邮箱
    res = re.match(pat1,str)
    print(res)

checkPhone2("93910385@qq.com")
print(checkPhone("17382865078"))
print(checkPhone("173828650781"))
