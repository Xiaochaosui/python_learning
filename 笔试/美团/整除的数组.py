import random
import itertools
I=input().split(" ")
n=int(I[0])
k=int(I[1])
L = int(I[2])
R = int(I[3])
List = []
count = 0

if n>=1 and n <=1e5 and k>=1 and k<=10 and L>=1 and L<=R and R <=1e9:
    LList = list(itertools.product(range(L,R+1),repeat=n))
    for List in LList:
        if sum(List) % k == 0:
            count += 1


res = count%(1e9+7)
print("%d"%res)
