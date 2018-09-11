"""
import calendar

cal = calendar.calendar(2018)
print(cal)

# isleap:判断某一年是否为闰年
a = calendar.isleap(2000)
print(a)

b = calendar.leapdays(1998, 2018)
print(b)

c = calendar.month(2018, 8)
print(c)

d = calendar.monthrange(2018, 8)
print(d)# 周一到周六（0-5）


"""

"""
import time

# Time模块
print(time.timezone)# 获取时间戳
print(time.altzone)# 获取时间戳
print(time.daylight)# 判断是否为夏季
print(time.time())
print(time.localtime())# 当前时间
print(time.localtime().tm_hour)# 当前时间
print(time.asctime())# 当前时间
print(time.ctime())# 当前时间

ft = time.strftime('%Y年%m月%d日 %H:%M', time.localtime())
print(ft)
"""
import datetime
# datetime.date:一个理想的日期，提供year,month,day
# print(datetime.date(2018,3,25))

from datetime import datetime

dt = datetime(208, 3, 25)
print(dt.day)
print(dt.now())
print(dt.today())
