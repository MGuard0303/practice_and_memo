"""docstrings
该文件提供了一个 Hour : Minute 级别的倒计时工具。作为输入的 Hour 和 Minute 可以是浮点数，Minute 也不需要限制在60之内。

e.g. Hour:Minute -> 3:05; Hour:Minute -> 3.4:45.1; Hour:Minute -> 47.24:168.4

# ==========
Future Plan
添加通过邮件通知的功能
# ==========
"""



import time




# 尚未实现对秒级别倒数的处理
ori_hour, ori_min = input("Please input countdown time in 'Hour:Minute': ").split(sep=":")

ori_hour = float(ori_hour)
ori_min = float(ori_min)


# 处理小时输入为浮点数的情况
hour_x, hour_y = divmod(ori_hour, 1)
if hour_y != 0:
    hour_y = hour_y * 60

ori_min = ori_min + hour_y


# 处理分钟输入大于60的情况
min_x, min_y = divmod(ori_min, 60)
if min_x >= 0:
    hour_x = hour_x + min_x

hours = int(hour_x)
minutes = int(min_y)

# 为了记录设定的时间
hours_copy = hours
minutes_copy = minutes



SLEEP_TIME = 60  # sleep for 1 min (60s)
countdown_time = hours*3600 + minutes*60   # countdown_time unit is sec


start = time.time()
while countdown_time > 0:
    try:
        print("{:02d} : {:02d}".format(hours, minutes), end="\r")
        time.sleep(SLEEP_TIME)
    
        minutes = int(minutes - SLEEP_TIME/60)   
        countdown_time -= SLEEP_TIME
    
        if minutes < 0:
            minutes = 59
            hours -= 1

    except KeyboardInterrupt as e:
        end = time.time()   # time()返回值单位为秒
        duration = (end - start) / 60  # 将duration转换到min
        duration_h, duration_m = divmod(duration, 60) 

        print("Timer has been stopped by user.")
        print("Duration: {:02d} : {:02d}".format(int(duration_h), int(duration_m)))
        exit()
    

end = time.time()
duration = (end - start) / 60  # 将 duration 转换到 min
duration_h, duration_m = divmod(duration, 60) 

print("TIME'S UP")
print("The setting time is {:02d} : {:02d}".format(hours_copy, minutes_copy))
print("The runing time is {:02d} : {:02d}".format(int(duration_h), int(duration_m)))



# 需要完成时邮件提醒
