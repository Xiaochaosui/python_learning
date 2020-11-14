fruits = ["苹果","桃子","梨","桃子","梨","橘子","梨"]
'''f1 = []
for s in fruits:
    if s == "梨":
        t = s.replace("梨","苹果")
        f1.append(t)
    else:
        f1.append(s)

print(f1)
'''
fruits = ["苹果","桃子","梨","桃子","梨","橘子","梨"]
str1 =" ".join(fruits)
print(str1.replace("梨","苹果").split(" "))
#
# 思路3
for i in range(len(fruits)):
    if fruits[i] == "梨":
        fruits[i] = "苹果" # 列表修改

print(fruits)