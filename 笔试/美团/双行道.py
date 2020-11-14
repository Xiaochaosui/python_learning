def r(List,a):
    List

n=int(input())
List1=input().split(" ")
List2=input().split(" ")
L=[]
i=0
j=0
stack=[]
L.append(List1)
L.append(List2)
stack.append(L[i][j])
if List1[0]=='.':
    while L[1][n-1] !='o':
        if i==0:
            if L[i][j+1]=='X' and L[i+1][j+1]=="X":
                continue
            elif L[i][j+1]=='.' and L[i+1][j+1]=="X":
                stack.append(L[i][j+1])





else:
    print(-1)

