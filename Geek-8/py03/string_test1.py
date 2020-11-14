# input:46655adad ada dasd655*$
# output:字母:11，数字:8，空格:2,其他:2

a=0 # 字母
b=0 # 数字
c=0 # 空格
d=0 # 其他
str = input("输入字符:")
for s in str:
    if s.isdigit():
        b +=1
    elif s.isalpha():
        a +=1
    elif s.isspace():
        c +=1
    else:
        d +=1
print("字母:%d，数字:%d，空格:%d,其他:%d"%(a,b,c,d))

