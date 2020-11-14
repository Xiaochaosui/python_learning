
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#a=_odd_iter()
#print(next(a))
#print(next(a))

def _not_divisible(n):
    return lambda x: x % n > 0
a =_not_divisible(3)
#print(list(filter(a,[1,2,3,4])))
#print(3%2)
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        print("**",n)
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列


if __name__ == '__main__':
    for n in primes():
        if n < 20:
            print(n)
        else:
            break


