def fib(n):
    if n==1 or n==2:
        return 1
    elif n==0 :
        return 0
    else:
        return fib(n-1)+fib(n-2)

if __name__ == '__main__':
    n = int(input("输入n:"))
    for i in range(1,n):
        print(fib(i),end=" ")

