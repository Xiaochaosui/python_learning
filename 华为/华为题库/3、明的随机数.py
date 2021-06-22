list1 = []
while 1:
    try:
        n = int(input())
        for i in range(n):
            a = int(input())
            list1.append(a)
    except Exception:
        break
set1 = set(list1)
list2 = list(set1)
list2.sort()
for x in list2:
    print(x)

