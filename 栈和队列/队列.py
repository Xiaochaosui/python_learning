import  collections

# 创建一个队列
queue = collections.deque()
print(queue)

# 进队
queue.append("A")
queue.append("B")
queue.append("C")
print(queue)

# 出队
res = queue.popleft()
print(res)
print(queue)


