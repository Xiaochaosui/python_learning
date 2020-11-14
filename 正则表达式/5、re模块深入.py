import re

# 字符串切割
str1 = "xcs is a good     man"
#print(str1.split(" "))
#print(re.split(r" +",str1))

# re.finditer()函数
'''
原型：finditer(pattern,string,flag=0)
参数：
pattern:匹配的正则表达式，
string:要匹配的字符串，
flags:标志位，用于控制正则表达式的匹配方式，值如下:
功能:与findall类似，扫描整个字符串,返回的是一个迭代器
'''
str2 = "xcs is a good man! xcs is a nice man! xcs is a gentle man!"
d = re.finditer(r"(xcs)",str2)
while True:
    try:
        l = next(d)
        print(l)
    except StopIteration as e:
        break


# 字符串的替换与修改
'''
sub(pattern, repl, string, count=0, flags=0)
subn(pattern, repl, string, count=0, flags=0)
pattern:正则表达式(规则)
repl:指定的用来替换的字符串
string：目标字符串
count：最多替换次数
flags：同re简介
功能：在目标字符串中以正则表达式的规则匹配字符串，再把他们替换成指定的字符串。可以指定替换的次数，如果不指定，替换所有的匹配字符串
区别：前者返回结果字符串，后者返回一个tuple，第一个元素是结果字符串，第二个元素是表示被替换的次数
'''
print("字符串的替换与修改\n")
str3 = "xcs is a good good good man!"
print(re.sub(r"(good)","nice",str3))
print(re.subn(r"(good)","nice",str3,count = 2))
print(type(re.sub(r"(good)","nice",str3))) #str
print(type(re.subn(r"(good)","nice",str3))) # tuple

# 分组
'''
re.group()
概念：除了简单的判断是否匹配之外，正则表达式还有提取子串的功能，用()表示分组

'''
str2 = r"0739-8881510"

m = re.match(r"(?P<first>\d{4})-(\d{7})",str2)
print(m)
# 查看匹配的各组的情况,用序号获取对应组的信息
print(m.group())
print(m.group(1))
print(m.group("first"))
print(m.group(2))
print(m.groups())

# 编译
'''
编译:当我们使用正则表达式时，re模块会干两件事
1、编译正则表达式，如果正则表达式不合法，会报错
2、用编译后的正则表达式去匹配对象

'''
# 编译成正则对象
pat = r"^1([3578]\d|(47))\d{8}$"
re_telephone = re.compile(pat)
print(re_telephone.match("17382865078"))
