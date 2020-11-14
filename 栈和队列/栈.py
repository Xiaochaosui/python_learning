
# 模拟栈结构

stack = []  # 列表

# 压栈(向栈里存数据)
stack.append("A")
print(stack)
stack.append("B")
stack.append("C")
print(stack)

# 出栈(在栈里取数据)
res = stack.pop()
print(res)
print(stack)