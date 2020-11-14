str = "Buddy, you're a boy make a big noisePlaying in the streets gonna be a big man somedayYou got mud on your faceYou big disgraceKicking your can all over the placeSingingWe will, we will rock youWe will, we will rock youBuddy you're a young man, hard manShouting in the street gonna take on the world somedayYou got blood on your faceYou big disgraceWaving your banner all over the placeWe will, we will rock youSinging it nowWe will, we will rock youPleading with your eyes gonna make you some peace some dayYou got mud on your facebig disgraceSomebody better put you back into your placeWe will, we will rock youSing itWe will, we will rock youEverybodyWe will, we will rock youWe will, we will rock youAlright"
# 1、will 出现的次数
'''count = 0
print(str.count("will"))'''

# 2、数单词
'''q=0
list1 = str.split(" ")
for s in  list1:
    if len(s)>0:
        q +=1
print(q)'''
# 3、回文串:12321  一块五花肉花五块一
# 4、将所有的 “we” 换成 “我们”
# str.replace(oldstr,newstr,num)
# 用newstr替换oldstr，默认是全部替换，指定num，那么替换前num个
'''str1 = str.replace("we","我们") # 不会影响 原字符串本身的
print(str1)'''
# 文字加密方式

# 输入：O S, GOMR YPFSU/
# 输出:I AM FINE TODAY.
str2 = r"qwertyuiop[]\asdfghjkl;'zxcvbnm,./"
str3 = r"QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./"
s1 = input("输入:")
list1 = []
for s in s1:
    if s in str2:
        c = str2.find(s)-1
        a = str2[c]
        list1.append(str2[c])
        '''list1.append(str2[str2.find(s) - 1])'''
    elif s in str3:
        c = str3.find(s) - 1
        a = str3[c]
        list1.append(str3[c])
        '''list1.append(str3[str3.find(s) - 1])'''
    if s==" ":
        list1.append(s)
print("".join(list1))










