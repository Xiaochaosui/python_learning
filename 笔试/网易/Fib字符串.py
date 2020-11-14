import string
def fib(n,s1,s2):
    if n==1:
        return s1
    if n==2:
        return s2
    return fib(n-1,s1,s2)+fib(n-2,s1,s2)
def checkStr(str):
    strDict={}
    for i in string.ascii_lowercase:
        if(str.count(i)!=0):
            strDict[i]=str.count(i)
    for k,v in strDict.items():
        print("%s:%d"%(k,v))
if __name__ == '__main__':
    n=int(input())
    s=input()
    strList=s.split(" ")
    s1=strList[0]
    s2=strList[1]
    strFib=fib(n,s1,s2)
    checkStr(strFib)


