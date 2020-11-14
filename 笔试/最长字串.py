
def findLong(str):
    t = str[0]
    dic = {}
    for i in range(len(str)):
        for x in str[i:]:
            if t.find(x) != -1:
                if t.find('a') != -1:
                    dic[t] = len(t)
                else:
                    dic[t] = 0
                break
            else:
                t = t + x
    print(dic)
    print("无重复子串带‘a’:",list(dic.keys())[list(dic.values()).index(max(dic.values()))],"长度:",max(dic.values()))








if __name__ == '__main__':
    str = input("请输入字符串:\n")
    findLong(str)