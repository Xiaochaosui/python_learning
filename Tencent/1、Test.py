# 求一个数的开根号
# 10e-5
# x2 = (x1+a/x1)2
# x*y = a
def sqr(s):
    #res = x**0.5
    #x1= 0.0
    #x1 = x//2
    es = 10e-5
    x = s/2
    y = s / x
    if x>=0:
        while x-y>es or y-x>es:
            y = s / x
            x = (x+y)/2
        res = x
        return res
    else:
        print("请输入正数")

if __name__ == '__main__':
    a = float(input())
    print(sqr(a))
