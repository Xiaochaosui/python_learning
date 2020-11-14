# input：asdasd456     1454adadasd说的
# 处理
# output: Yes           No
# break 终止循环  adas*/*

# 输入  isalnum()
while True:
    str = input("输入变量:")
    # 判断变量名字
    flag = 1
    s = str[0]
    if s !='_' and s.isalpha()==False: # 下划线_
        print("No*")
    else:
        for s1 in str[1:]:
            if (s1 !="_") and (s1.isalnum()==False) :
                print("No")
                break
            else:
                flag +=1
        if flag==len(str):
            print("Yes")






