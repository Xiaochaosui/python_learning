
I=input().split(" ")
List=input().split(" ")
n=int(I[0])
x=int(I[1])
L=[]
def huo(x,y):
    return x|y
for a in List:
    L.append(int(a))
max1 = max(L.count(a) for a in L)
max2 =0
flag=0
i=0
while max2<=max1:
    for y in L:
        L[i]=huo(x, y)
        i +=1
        max2=max(L.count(a) for a in L)
        if max2 > max1:
            flag=1
        else:
            flag=0
    if flag==0:
        break


if flag==1:
    print(max2)
else:
    print(max1)



