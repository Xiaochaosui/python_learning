import calendar




# 返回某年某月的日历
print(calendar.month(2012,5))
# 返回某年的日历
# print(calendar.calendar(2012))

# 判断闰年返回True
# print(calendar.isleap(2012))

# 返回某个月的weekday的第一天和所有天数
# print(calendar.monthrange(2012,5))
# 返回某个月以每一周为元素的列表
print(calendar.monthcalendar(2012,5))
