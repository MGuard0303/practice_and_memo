"""docstrings

"""


import time


# 尚未实现对空输入的处理
# 尚未实现对秒级别倒数的处理
hrs, mins = input("Please input countdown time in 'hh:mm': ").split(sep=":")

hrs = float(hrs)
mins = float(mins)

# 需要支持mins大于60以及hrs是浮点数的情况
if mins >= 60:
    print("minute should be less than 60.")

if hrs < 1:
    mins += hrs*60

if mins > 60:
    hrs, mins = divmod(mins, 60)    # divmod(a, b)返回(a // b, a % b)



SLEEP_TIME = 1
countdown_time = hrs*60 + mins*1


while countdown_time > 0:
    print("{:02.0f}".format(hrs) + " : " + "{:02.0f}".format(mins), end="\r")
    time.sleep(SLEEP_TIME)
    hrs = hrs - SLEEP_TIME/60
    mins = mins - SLEEP_TIME/1
    
    if mins < 0:
        mins = 59
        hrs -= 1
    if hrs < 0:
        hrs = 0
    # 需要KeyboardInterrupt处理


# 需要完成时邮件提醒
print("TIME UP")

