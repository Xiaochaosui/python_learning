# 暴力来匹配
def f(str):
    if str=='':
        return ""
    i=0
    while i<len(str):
        if str[i]=='a':
            if i==len(str)-1:
                str=str[:len(str)-1]
                break
            elif i==0:
                str=str[1:]
            else:
                str=str[:i]+str[i+1:]
        elif str[i]=='c' and i>0 and str[i-1]=='b':
            if i==1:
                str=str[2:]
                i=i-1
            elif i==len(str)-1:
                str=str[:i-1]
                break
            else:
                str=str[:i-1]+str[i+1:]
                i=i-1
        elif str[i] == 'f' and i >1 and str[i - 1] == 'e' and str[i - 2] == 'd':
            if i == 2:
                str = str[3:]
                i=i-2
            elif i == len(str) - 1:
                str = str[:i - 2]
                break
            else:
                str = str[:i - 2] + str[i + 1:]

                i = i - 2
        else:
            i += 1
    return str
def f3(s):
    s1 = 'a'
    s2 = 'bc'
    s3 = 'def'
    while True:
        if s.find(s1) != -1:
            s = s.replace(s1, '')
        elif s.find(s2) != -1:
            s = s.replace(s2, '')
        elif s.find(s3) != -1:
            s = s.replace(s3, '')
        else:
            break
    return s
# 栈
def f2(str):
    stack=[]
    for i in range(len(str)):
        t=str[i]
        if t=='a':
            continue
        if len(stack)==0:
            stack.append(t)
            continue
        if t=='c':
            peek= stack[len(stack)-1]
            if peek=='b':
                stack.pop()
            else:
                stack.append(t)
        elif t=='f':
            peek1=stack[len(stack)-1]
            peek2=stack[len(stack)-2]
            if peek1=='e' and peek2=='d':
                stack.pop()
                stack.pop()
            else:
                stack.append(t)
        else:
            stack.append(t)
    res = ''.join(stack)
    return res



if __name__ == '__main__':
    s = input()
    print(f(s))
    print(f2(s))
    print(f3(s))

