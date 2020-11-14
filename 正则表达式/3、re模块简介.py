import re

# pip 下载三方的 包管理工具

# re.match() 函数
r'''
原型：match(pattern,string,flag=0)
参数：
pattern:匹配的正则表达式，
string:要匹配的字符串，
flags:标志位，用于控制正则表达式的匹配方式，值如下:
re.I: 忽略大小写(常用)
re.L：做本地化识别（一般用不上）
re.M：多行匹配，影响^和$(常用)
re.S：是.匹配包括换行符在内的所有字符(常用)
re.U：根据Unicode字符集解析字符，影响\w,\W,\b,\B
re.X：使我们以更灵活的格式理解正则表达式
参数：
功能：尝试从字符串的起始位置匹配一个模式，如果不是起始位置，匹配成功的话，也会返回None
'''
print(re.match("www","www.baidu.com").span())
print(re.match("www","ww.baidu.com"))
print(re.match("www",".baidu.wwwcom"))
print(re.match("www","wwW.baidu.com",flags=re.I))

# 扫描整个字符串，返回从起始位置成功的匹配

print("*******")
'''
re.search()
原型：search(pattern,string,flags=)
功能：扫描整个字符串，并返回第一个匹配成功的匹配
参数：
pattern:匹配的正则表达式，
string:要匹配的字符串，
flags:标志位，用于控制正则表达式的匹配方式，值如下:
'''
print("-----")
print(re.search("xcs"," is a Xcs good\n man xcs",flags=re.M))

'''
re.findall()
原型：findall(pattern,string,flags=)
功能：扫描整个字符串，并返回结果列表
参数：
pattern:匹配的正则表达式，
string:要匹配的字符串，
flags:标志位，用于控制正则表达式的匹配方式，值如下:
'''
print("@@@@")
print(re.findall("xcs"," is a Xcs good man xcS",flags=re.I))
