s = input()
strList = s.split(" ")
strRes = []
res = -1
flag = 0
for str in strList:
    strRes.append(str)
    strRes.append(strList.count(str))
for i in range(len(strRes)):
    if strRes[i] == 1:
        flag = 1
        t = strList.index(strRes[i - 1])
        print("%d %s" % (t + 1, strRes[i - 1]))
        break
if flag == 0:
    print(res)

