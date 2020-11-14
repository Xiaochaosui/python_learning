'''
递归调用：一个函数,调用自身，称为递归调用
递归函数：一个会调用自身函数称为递归函数

凡是循环能干的，递归都能干

方式：
1、写出临界条件
2、找这一次和上一次的关系
3、假设当前函数已经能用，调用自身计算上一次的结果没在求出本次的结果


'''
def sum(n):
    sum = 0
    for x in range(1,n+1):
        sum +=x
    return sum
print(sum(5))

def sum1(n):
    if n == 1:
        return 1
    else:
        return sum1(n-1)+n
print(sum1(5))