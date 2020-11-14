'''# 实现列中列
list1 = [1,2,3]
list2 = [4,5,6]
list3 = []
list3.append(list1)
list3.append(list2)
#[[1,2,3],[4,5,6]]
print(list3)
t = list3[1]
print(t[1])
print(list3[1][1])
# 取888
list4 = [[1,2,3,[30,59,[888,26]]]]
print(list4[0][3][2][0])'''


a = [1,2,3,4,5,6,7,8]
odd_num = [i for i in a if i%2 != 0]
nums = [i if i%2!=0 else i*i for i in a]
print(odd_num)
print(nums)

