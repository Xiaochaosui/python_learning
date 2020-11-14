import itertools

'''
排列
组合
'''

# 排列
myList = list(itertools.permutations([1,2,3,4],3))
print(myList)
print(len(myList))
#print(type(myList[1]))

# 组合
myList1 = list(itertools.combinations([1,2,3,4],3))
print(myList1)
print(len(myList1))
#print(type(myList1[1]))

# 排列组合
myList2 = list(itertools.product([1,2,3,4],repeat=4))
print(myList2)
print(len(myList2))
