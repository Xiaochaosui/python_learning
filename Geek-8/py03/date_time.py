import time

# time.time()表示从1970.1.1至今相隔时间 单位s
print("时间戳:",time.time())
# time.localtime() 获取本地时间  local 当地的 adj
# 返回时一个元组 tuple
# tuple = (1,2,3)
# list = [1,2,3] 列表
print("本地时间1:",time.localtime() )
# time.asctime()
print("本地时间2:",time.asctime() )

'''3、格式化字符串
百度：时间字符串格式 python

%b	月份的英文单词的缩写：如一月， 则返回 Jan
%B	月份的引文单词的缩写：如一月， 则返回 January
%c	返回datetime的字符串表示，如03/08/15 23:01:26
%d	返回的是当前时间是当前月的第几天
%f	微秒的表示： 范围: [0,999999]
%H	以24小时制表示当前小时
%I	以12小时制表示当前小时
%j	返回 当天是当年的第几天 范围[001,366]
%m	返回月份 范围[0,13]
%M	返回分钟数 范围 [0,61]
%P	返回是上午还是下午–AM or PM
%a	星期的英文单词的缩写：如星期一， 则返回 Mon 
%A	星期的英文单词的全拼：如星期一，返回 Monday
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
'''
# 年 月 日 周几  时：分：秒
t = time.localtime()
print(t[0],"年",t[1],t[2],t[6]+1,t[3],t[4],t[5])
print("现在是%d年%d月%d日 周%d %d时%d分%d秒"%(t[0],t[1],t[2],t[6]+1,t[3],t[4],t[5]))
# time.strftime() 输出时间格式化
print(time.strftime("%Y/%m/%d %H:%M:%S"))
print(time.strftime("%Y/%m/%d %a %H:%M:%S"))
print(time.strftime("%Y/%m/%d %A %X"))

# calendar

import calendar
print("2020年7月的日历")
print(calendar.month(2020,7))
# 年/月/日/星期几/时/分/秒
print(time.strftime("%Y/%m/%d/%A/%H/%M/%S"))