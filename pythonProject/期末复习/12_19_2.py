import time

def demo(day1, day2):
    time_array1 = time.strptime(day1, "%Y-%m-%d")
    timestamp_day1 = int(time.mktime(time_array1))
    time_array2 = time.strptime(day2, "%Y-%m-%d")
    timestamp_day2 = int(time.mktime(time_array2))
    result = (timestamp_day2 - timestamp_day1) // 60 // 60 // 24  #得到时间秒数后转化为天数
    return result

day1=input(r"请以该种形式输入日期:2018-07-09   ----")

day2 =input("请以该种形式输入日期:2018-07-09   ----")

day_diff = abs(demo(day1, day2))
print("两个日期的间隔天数：{} ".format(day_diff))
