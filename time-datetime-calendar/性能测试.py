
import time
sum = 0
for i in range(10000000):
    sum += i
print(sum)
print(time.perf_counter())