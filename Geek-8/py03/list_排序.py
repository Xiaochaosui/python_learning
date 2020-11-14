# list 排序
# 将列表元素倒序输出 reverse()没有返回值 直接改变list本身
list1 = [1,2,3,4,5]
print("反转前",list1)
list1.reverse()
print("反转后",list1)
# ctrl+c 复制
# ctrl+x 剪切
# ctrl+v 粘贴
# ctrl+z 撤销



list3 = [28,60,89,99,70,59]
list4 = []
list4.extend(list3)  # 复习前天的
list3.sort(reverse=True) #  等于后面两句 list2.sort()  list2.reverse()
print("排序后（大到小）",list3)
print(list4)
# sort() 将列表list排序 ，改变原来的list ，排序方式是从小到大排序
list2 = [28,60,89,99,70,59]
print("排序前",list2)
list2.sort()
print("排序后(小到大)",list2)
list2.reverse()
print("排序后（大到小）",list2)
# sorted() 不改变原来的list，与上面的sort()对比学习，有返回值，返回值是排序之后的列表,sorted()不止排序数字
list5 = [28,60,89,99,70,59]
temple = sorted(list5)
# 根据ASCll码排序   1个字符是由7位二进制数组成的
# 0000001  *
# 0000000  /
# 0000010 -
# 0000011 +
# 0000100 .
# 0000101 @
# 0000110 #
# 0000111 ￥
# 2^7种
#  可以排多少种字符
str1 = "xcs is123#%…… a good man123"
print(temple)
print("sorted排序后",sorted(list5))
print("sorted排序后原来的list5",list5)
print("排序非数字:",sorted(str1))

# 用切片来实现 reverse()  切片实现反转不改列表本身 reverse()改变list本身
# 切片格式:list[起始位置:末尾位置:间隔数量]
list6 = [1,2,3,4,5]
print(list6[::-1])
print(list6)