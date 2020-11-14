'''
UTC(世界协调时间)：格林尼治时间,世界标准时间，在中国说是UTC+8

DST（夏令时）：是一种节约能源而人为规定时间制度，在夏季调快一个小时


时间表现形式：
1、时间戳
以整型或浮点型表示时间的一个以秒为单位的时间间隔，这个时间间隔的基础值是从1970年1月1号0点开始算起
2、元组
一种python数据结构表示，这个元组有9个整型内容
year
month
day
hours
minutes
seconds
weekday
Julia day
flag(1 or -1 or 0)

3、格式化字符串
百度：时间字符串格式 python
%a	星期的英文单词的缩写：如星期一， 则返回 Mon
%A	星期的英文单词的全拼：如星期一，返回 Monday
%b	月份的英文单词的缩写：如一月， 则返回 Jan
%B	月份的引文单词的缩写：如一月， 则返回 January
%c	返回datetime的字符串表示，如03/08/15 23:01:26
%d	返回的是当前时间是当前月的第几天
%f	微秒的表示： 范围: [0,999999]
%H	以24小时制表示当前小时
%I	以12小时制表示当前小时
%j	返回 当天是当年的第几天 范围[001,366]
%m	返回月份 范围[0,12]
%M	返回分钟数 范围 [0,59]
%P	返回是上午还是下午–AM or PM
%S	返回秒数 范围 [0,61]。。。手册说明的
%U	返回当周是当年的第几周 以周日为第一天
%W	返回当周是当年的第几周 以周一为第一天
%w	当天在当周的天数，范围为[0, 6]，6表示星期天
%x	日期的字符串表示 ：03/08/15
%X	时间的字符串表示 ：23:22:08
%y	两个数字表示的年份 15
%Y	四个数字表示的年份 2015
%z	与utc时间的间隔 （如果是本地时间，返回空字符串）
%Z	时区名称（如果是本地时间，返回空字符串）

2020-02-12 14:49:30
'''
import time

# 返回当前时间的时间戳，浮点数形式，不需要参数，得到的是UTC时间
c = time.time()
# print(c)

# 将时间戳转为UTC时间元组
t = time.gmtime(c) # 得到的是UTC时间
# print(t)

# 将时间戳转为本地时间元组
b = time.localtime(c) # 得到的是北京时间
# print(b)

# 将元组转成时间戳
m =time.mktime(b)
# print(m)

# 将时间元组转成字符串
s = time.asctime(b)
# print(s)

# 将时间戳转为字符串  time.asctime(time.localtime(time.time()))
s1 = time.ctime(c)
# print(s1)

# 将时间元组转换成给定格式的字符串，参数2为时间元组，如果没有参数2，默认转的是当前时间
q = time.strftime("%Y-%m-%d %X",b) # 当前时间
# print(q)
# print(type(q))

# 将时间的字符串转成时间元组
w = time.strptime(q,"%Y-%m-%d %X")
#print(w)

# 延迟一个时间，参数为整型或者浮点型
# time.sleep(4)

# 返回当前程序的CPU执行时间
# Unix始终返回全部的运行时间
# Windows从第二次开始，都是以第一个调用此函数的开始时间戳作为基数
y1 = time.perf_counter() # 代替time.clock()这个加上睡眠时间 注意和time.process_time()区别，这个只有CPU处理时间
# print(y1)
# time.sleep(2)
y2 = time.perf_counter()
# print(y2)
