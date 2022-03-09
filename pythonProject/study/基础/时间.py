import datetime
import time
from calendar import calendar, isleap

print("时间戳",time.time())
print("",datetime.datetime.now().timestamp())
print("时间元祖",time.localtime())
print("格式化时间格式",time.strftime("%Y-%m-%d %H:%M:%S  星期%A"))
time.sleep(3)
print("",time.asctime())
print("",time.process_time())

print("下划线".center(20,"-"))

print(""+calendar(2022,1))
print("",isleap(2022))

print("",datetime.datetime.today())
print("",datetime.datetime.now())
