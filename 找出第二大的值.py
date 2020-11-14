listnum = []

num = 0
while num < 5:
    val = int(input())
    listnum.append(val)
    num += 1
print(listnum)

listnum.sort()
count = listnum.count(listnum[len(listnum)-1])
c = 0
while c < count:
    listnum.pop()
    c += 1
print(listnum[len(listnum)-1])