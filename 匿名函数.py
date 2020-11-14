'''
概念： 不使用def这样的语句定义函数，使用lambda来创建匿名函数


特点：
1、lambda只是一个表达式，函数体比def简单
2、lambda的主体是一个表达式，而不是代码块，仅仅只能在lambada表达式中封装简单的逻辑
3、lambda函数有自己的命名空间，且不能访问自由参数列表之外的或全局命名空间的参数
4、虽然lambda是一个表达式且看起来只能写一行，与C和C++内联函数不同

格式： lambda 参数1，参数2，……，参数n：expression

'''

sum = lambda num1,num2:num1 + num2
print(sum(1,2))