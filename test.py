'''n = int(input())
i = 2
while n != 1:
    if n % i ==0:
        print(i)
        n //=i
    else:
        i += 1'''

'''t = ord("9")+1
s=chr(t)
print(t)
print(s)'''

'''for i in range(1,5,2):
    print(i)'''

str ="asdd"
#print(list(set(list(str))))




# 求最大值，排序，和最大值个数
'''g=input().split(" ")
grade=[]
for i in range(len(g)):
    grade.append(int(g[i]))
sum=0
max=-1
for v in grade:
    sum += v
    if max<=v:
        max=v
avg=float(sum/len(grade))
c=0
for v in grade:
    if max==v:
        c +=1
grade.sort()
for v in grade[:-1]:
    print(v,end=' ')
print(grade[-1],end='')
print(",max:%d,count:%d,avg：%.2f\n"%(max,c,avg))'''


def solveProblem():
    a = {'a':5,'b':4,'c':3,'d':2,'e':1,'f':6}
    sorted(a.items(), key=lambda kv: (kv[1], kv[0]))  # a按战力升序排序
    lis = [[] for i in range(len(a))]  # 标记数组
    if len(a) % 2 == 0:  # 如果是偶数，不存在轮空
        for i in range(5):
            alreadychose = []
            for j in range(len(a)):
                alreadychose.append(0)  # 一开始都没被选中过
            for j in range(len(a)):
                if alreadychose[j] == 0:
                    k = j + 1
                    while k < len(a):
                        if lis[j][k] == 0 and j < len(lis) and k<len(lis[j]):  # reachable
                            lis[j][k] = 1
                            alreadychose[j] = 1
                        k = k + 1
                    print(a[j], a[k])
            print('\n')
    else:  # 如果是奇数
        for i in range(5):
            if a[0].force - a[1].force < a[len(a)-2].force - a[len(a) - 1].force:  # 最大的一个轮空
                for i in range(5):
                    alreadychose = []
                    for j in range(len(a)):
                        alreadychose.append(0)  # 一开始都没被选中过
                    for j in range(len(a)):
                        if alreadychose[j] == 0:
                            k = j + 1
                            while k < len(a):
                                if lis[j][k] == 0:  # reachable
                                    lis[j][k] = 1
                                    alreadychose[j] = 1
                                k = k + 1
                            print(a[j], a[k])
                    print('\n')


solveProblem()