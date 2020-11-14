'''
字符串是以单引号或双引号括起来的任意文本
'abc'
"def"
'''

# 创建string-》字符串

str1 = "xcs is a good man"

str2 = "xcs"
str3  = "is"
str4 = "a good man"

# 字符串不变
'''# 字符串连接 (逗号和加号的区别)
print(str2,str3,str4)
print(str2+str3+str4)'''

#输出重复字符串
str5 = "xcs "
'''print(str5*10)'''

# 访问字符串中的某个字符 通过索引下标查找字符，从0开始
# 字符串名[下标]
str6 = "xcs is a good man!"
'''print(str6[17])
print(str6[5])'''

# 截取一部分字符串 切片
#字符串名[下标1:下标2]
'''print(str6[7:13])
print(str6[7:])
print(str6[:7])'''


# 从头截取到给定下标之前
# print("str10=",str10)
#str11 = str9[:4]
#print("str11=",str11)

# 从给定下标截取到结尾
#str12 = str9[4:]
#print("str12=",str12)


# 判断成员是否在序列中  查询
str13= "xiao is a good man"
'''print("@@@@@")
print("good" in str13)
print("god" in str13)
print("@@@@@")'''
# 格式化输出
#print("xiao is a good man")
n = 10
#print("num =",num)
f = 3.1415926 # 精确到小数点后多少位，会四舍五入
# 占位符 %d %f %s
str7 = "xcs is a good man!"
'''print("n= %d,f= %f ,str = %s" % (n,f,str7))'''


'''# 换行
print(
"good",
"nice",
"xiao",
"sadasd"
)
print("asdas")'''



# 转义字符 \ 或者 r"str"
# \t Tab(4个space)

'''str8 = "xcs is a good man!"
print("*****************")
print(str8+"\t"+"aaaa")
print(str8+"\\t"+"aaaa")
print(str8+"\t\t\t\t"+"aaaa")
print(str8+r"\t\t\t\t"+"aaaa")
print("*****************")
'''

# 方法
# eval(str)
# string 串 绳
# 功能 ：将字符串str 当成有效的表达式来求值并返回计算结果
'''num = 123
str9 = "123"
str10 = str(num)
num1 = eval(str9)

# int float str bool  Type()获取数据类型
print(num1)
print(type(num1))'''

# len(str) 返回字符串的长度（字符个数） 循环条件

# str.lower() 转换字符串中的大写字母为小写字母
'''str14 = "XIao"
print("lower()")
print(str14.lower())
print(str14)
# str.upper() 转换字符串中的小写字母为大写字母
print("upper()")
print(str14.upper())'''






# swapcase() 小写字母变大写 大写字母变小写
str15 = "Xiao GOd"
#print(str15.swapcase())

# str.capitalize() 首字母大写，其他小写 标准格式
'''print("capitalize()")'''
# print("str15".capitalize())

# str.title() 每个单词的首字母大写， 标题的标准格式
# print("title()")
# print("xiao is a good man".title())
# startswith 是否以某个字符串开头，是返回True，否则返回False
#str.startswith(str1)
# print("xiao is a good man".startswith("good"))


# str.center(width[,fillchar]) char character 居中字符串
print("center()")
print("center()".center(11,"*"))
print("hello world".center(40,"*"))
print("hello world".center(40))

#str.ljust(width[,fillchar])  左对齐  l  left
print("ljust()")
print("hello world".ljust(11,"*"))
print("hello world".ljust(40,"*"))
print("hello world".ljust(40))
# str.rjust(width[,fillchar])  右对齐   r  right
print("rjust()")
print("hello world".rjust(11,"*"))
print("hello world".rjust(40,"*"))
print("hello world".rjust(40))

# str.zfill(width) 返回一个长为width的字符串，源字符串右对齐，前面补0
#print(str1.zfill(40))

# str.count(str1,[start],[end]) 返回str指定范围的str1的个数
str17 = "xiao is is a gentleman"
# print(str17.count("is",5,10))



str17 = "xiao is is a gentleman"
print("good" in str17)
# str.find(str1[,start][,end])
# 从左向右检测str中 指定范围 中 str1第一次出现的开始下标 没有则返回-1
# str.rfind(str1[,start][,end]) 从右向左
print("&&&&&&&")
print(str17.find("is"))
print(str17.find("good"))
print(str17.find("is",6,len(str17)))
print("&&&&&&&")
# str.rfind(str1[,start][,end]) 从右向左的 检测str中 指定范围 中 str1第一次出现的开始下标 没有则返回-1
# print(str17.rfind("is"))
# str.index(str1) 与find()一样 如果str1不存在就会报错
str18 = "xiaochaosui is is a man"
# print(str18.index("iss"))
# print(str18.index("iaaa"))
# str.index(str1) 与rfind()一样 如果str1不存在就会报错


# str.lstrip() 截掉字符串左侧指定的字符，默认为空格
#print("lstrip")
str19 = "*******xiao is a man***"
print(str19.lstrip("*"))

# str.rstrip() 截掉字符串右侧指定的字符，默认为空格
print("rstrip")
print(str19.rstrip("*"))

# str.strip() 截掉字符串左右侧指定的字符，默认为空格
print("strip")
print(str19.strip("*"))

# join
# str.split(str1="",num) 以str1为分隔符截取字符串，指定num，则仅截取num个字符串
print("####")
str20 = "xcs is a*a****good man"
print(str20.split("*",2))

str21 = "xcs is a good man"
q = 0
list1 = str21.split(" ")
for s in list1:
    if len(s) > 0:
        q += 1
print(q)
print(len('a'))

# splitlines([keepends])  按照('\r','\r\n','\n')分割，返回
# keepends == True 会保
str22 = "xcs is a good00 man!" \
        "xcs is a nice man!" \
        " "


print(str22.splitlines())

# str.join(seq) 以指定的字符串分隔符str,将seq中的所有元素
#               组合成字符串
list2 = ['xcs','is','a','good','man']
str23 = "*".join(list2)
print(str23)

# max() min() 按照Ascall码来对比大小的
str24 = "xcs is a good man"
#print(max(str24))
#print(min(str24))

# str.replace(oldstr,newstr,num)
# 用newstr替换oldstr，默认是全部替换，指定num，那么替换前num个
str25 = "xcs is a good man"
str26 = str25.replace("good","nice",1)
'''print("***")
print(str25)
print(str26)
'''
# 创建一个字符串映射表
#print("********")
#                     被转换字符串  目标字符串
str27 = str.maketrans("xcs","pan")
# 只能一一对应 x--p c--a s--n
str28 = "xcs is a good man"
print(str27)
str29 = str28.translate(str27)
print(str29)

# str.startswith(str,start=0,end=len(str))
# 在给定的范围内判断是否以给定的字符串开头的，如果没有指定范围默认整个字符串
str30 = "xcs is a good man"
#print(str30.startswith("xcs"))
# str.endtswith(str,start=0,end=len(str))
# 在给定的范围内判断是否以给定的字符串结尾的，如果没有指定范围默认整个字符串
# str.endswith(str1,num1,num2)  num1与num2是截取的字符串的start和end位置，不写的话默认是全部字符串str
str31 = "xcs is a nice man"
'''print("endswith()")
print(str31.endswith("man"))
print(str31.endswith("man",4,10))'''


# 编码
# encode(encoding="utf-8",errors="strict")
str32 = "xcs is a good man鹅"
# ignore 忽略错误
data32 = str32.encode("utf-8","ignore")
#print(str32.encode())
#print(type(data32))
# 解码 pay attention:要与编码时的格式一致
str33 =data32.decode("utf-8","ignore")
#print(str33)




# str.isupper()
# 如果字符串中至少有一个英文字符且所有英文字符都为大写英文字母返回True

'''print("ABC".isupper())
print("AAC22".isupper())
print("ABC**".isupper())'''

# str.islower() s
# 如果字符串中至少有一个英文字符且所有英文字符都为小写英文字母返回True
# 用于数据整理
'''print("abc".islower())
print("Abc".islower())
print("abc**".islower())
'''
# str.istitle()
# 如果字符串是标题化的返回True
'''print("xcs is a good man".title())
print("xcs is a good man".istitle())
print("xcs is a good man".title().istitle())
'''
# str.isalpha()
# 如果字符串中至少有一个字符且所有字符都为字母返回True
'''str34 = "xcs is a good man"
str35 = "xcssdadasdas"
print("isalpha:")
print(str34.isalpha())
print(str35.isalpha())'''




# str.isalnum()
# 如果字符串中至少有一个字符且所有字符都为字母或数字返回True
str35 = "1a*23"
'''print("isalnum()")
print(str35.isalnum())
print("15ad665".isalnum())
print("15665".isalnum())'''

str  = "     "
'''print("isspace()")
print("45  asd".isspace())
print(str.isspace())
print("\t".isspace())
print(r"\t".isspace())'''
# str.isdigit()
# 如果字符串中只包含数字字符返回True
'''print("isdigit:")
print("123".isdigit())
print("123A".isdigit())
print("123c".isdigit())
print("".isdigit())'''
# str.isnumeric() 同上
print("123".isnumeric())
print("123a".isnumeric())
print("123***".isnumeric())




# str.isdecimal() 字符串只包含十进制字符返回True
'''print("123".isdecimal())
print("123a".isdecimal())
print("123*".isdecimal())
'''
# str.isspace() 字符串中只包含空格 返回True
'''print(" ".isspace())
print("asdsad asd".isspace())
print("\t".isspace())
print("\n".isspace())
print("\r".isspace())
'''



str = "Continuous rain down the ancient city people's road has my good mood, today is like a written game waiting to be pasted with a new stamp, I would rather my heart is not calm, forgotten only the good past, like the tumultuous mind of the stars shining in the dream, let me be happy, let me be happy, do not let the question stay in the heart, let me be happy, let me be happy, do not let the question stay In the heart of continuous rain under the ancient city people's road, I have a good mood today, like a well written letter waiting to be pasted with a new stamp. I'd rather that there is no peace in my heart, only the beautiful past is left behind, like the tumultuous noise in my mind, stars shining in the dream, let me be happy, let me be happy, don't let questions stay in my heart, let me be happy, let me be happy, don't let doubt Ask to stay in my heart goodbye Jack goodbye my Kerouac goodbye Jack goodbye my Kerouac goodbye Jack goodbye my Kerouac goodbye Jack goodbye my Kerouac goodbye Jack goodbye my Kerouac let me have a little joy let me be happy don't let the question stay in the heart let me be happy let me have a little joy don't let the question stay in the heart goodbye Jack goodbye my Kerouac goodbye Jack, goodbye to my Kerouac"


'''n=0
for i in range(len(str)):
    if str[i:i+7]=="goodbye":
        print(str[i:i+7])
        n +=1
print(n)
list1 = []
list1 = list(str)
for i in range(len(list1)):
    if list1[i]==",":
        list1[i]=" "
print(list1)
print("".join(list1))

for i in range(len(str)):
    if str[i]==",":
         s1 =str[:i]
         s2=str[i+1:]
         str = s1+" "+s2
print("***")
print(str)'''