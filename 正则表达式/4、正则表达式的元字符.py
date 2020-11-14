import re

print("******匹配单个字符与数字*****")
r'''
.: 匹配除换行符意外的任意字符
[0123456789]：[]字符集合，表示匹配方括号中所有所包含的任意[一个]字符
[xcs]  匹配'x','c','s'中任意一个字符
[a-z]  匹配任意一个小写字母
[A-Z]  匹配任意一个大写字母
[0-9]  匹配任意一个数字，类似[0123456789]
[0-9A-Za-z]  匹配任意一个数字，字母
[0-9A-Za-z_]  匹配任意一个数字，字母和下划线
[^xcs]  匹配除了'x','c','s'中任意一个字符
^ 称为脱字符，表示不匹配集合中的字符
[^0-9]  匹配任意一个非数字
[\d]    匹配数字，效果同[0-9]
[\D]    效果同[^0-9]
[\w]    效果同[0-9A-Za-z_] 
[\W]    效果同[^\w]
[\s]    匹配任意的空白符[空格，换行\r，回车\n，换页，制表],效果同[ \f,\n,\r,\t]
\S   效果同[^ \f,\n,\r,\t]
'''

#print(re.search("[xcs]","xcs is 6a good man"))
#print(re.findall("\w","xcs is 6a good man"))


print("******锚字符(边界字符)*****")
r'''
^  行首匹配，和在[]里的^不是一个意思
$  行尾匹配
\A 匹配字符串开始,它和^的区别是，'\A'只匹配整个字符出的开头，即使在re.M模式下也不会匹配它行的行首
\Z 匹配字符串结束,它和$的区别是，'\Z'只匹配整个字符出的结束，即使在re.M模式下也不会匹配它行的行尾
\b 匹配一个单词的边界，也就是单词和空格间的位置
\B 匹配非单词边界


'''
#print(re.search("man$","xcs is a good man"))


#print(re.findall('\Axcs',"xcs is a goo man\nxcs is a nice man",flags=re.M))
#print(re.findall('^xcs',"xcs is a goo man\nxcs is a nice man",flags=re.M))

print(re.search(r"er\b","nerve"))
print(re.search(r"er\B","never"))

print("***匹配多个字符***")
r'''
说明：下方的x,y,z,均为假设的普通字符，n,m非负整数，不是正则表达式的元字符
(xyz) 匹配小括号内的xyz(作为一整体去匹配)
x? 匹配0 个或者1个x
x*  匹配0个或者任意多个x   （.*）表示0个或任意多个字符(换行符除外)
x+ 匹配至少一个x
x{n} 匹配确定的n个x(n是一个非负整数)
x{n,} 匹配至少n个x(n是一个非负整数)
x{n,m} 匹配至少n个x，至多m个x n<=m
x|y   匹配x或者y
'''

print(re.findall(r"(xcs)","xcsasd is a good man,xcs is a nice man"))
print(re.findall(r"o?","oiopoo"))# 非贪婪匹配 (尽可能少的匹配)
print(re.findall(r"o*","ghjoo")) # 贪婪匹配 (尽可能多的匹配)
print(re.findall(r".*","ghjoo"))
print(re.findall(r"a+","fssaaaadgdfga"))# 贪婪匹配

print(re.findall(r"a{3}","aabaaaabaaa"))
print(re.findall(r"a{3,}","aabaaaabaaa"))# 贪婪匹配
print(re.findall(r"a{3,5}","aabaaaaabaaaa"))

print(re.findall(r"((p|P)y)","Pydfgdfpy"))


# 需求：提取xcs……man
str = "xcs is a good man! xcs is a nice man! xcs is a gentle man!"
print(re.findall(r"xcs.*?man",str))



print("-----特殊-----")
'''
*?  +?  x?  最小匹配，通常都是尽可能多的匹配，可以使用这种解决贪婪匹配
(?:x) 类似(xyz)，但不表示一个组


'''
s = r"/* part1 */ /* part2 */"
print(re.findall(r"//*.*?/*/",s))