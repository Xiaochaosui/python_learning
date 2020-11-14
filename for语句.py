'''
格式： for 变量名 in 集合:
         语句
'''

for i in [1,2,3]:
    print(i)


'''
range([start,]end[,step]) 列表生成器
start 默认为0 step默认为1
'''
for x in range(10):
      print(x)


for y in range(2,20,2):
      print(y)

print("*"*10)
for index,m in enumerate([1,2,5]):
    print(index,m)