"""docstrings
该文件提供了一个 Hour : Minute 级别的倒计时工具。作为输入的 Hour 和 Minute 可以是浮点数，Minute 也不需要限制在60之内。

e.g. Hour:Minute -> 3:05; Hour:Minute -> 3.4:45.1; Hour:Minute -> 47.24:168.4

该文件提供了一个可选的计时结束后的邮件提醒服务。
"""



import time
from email.message import EmailMessage
import smtplib




# 尚未实现对秒级别倒数的处理
ori_hour, ori_min = input("Please input countdown time in 'Hour:Minute': ").split(sep=":")

# 询问用户是否需要邮件服务
mail_notice = input("Do you wish to receive a mail notification when countdown complete? (y|n) ")

if mail_notice == "y":
    receiver = input("Please enter your email: ")

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
countdown_time = hours*3600 + minutes*60  # countdown_time unit is sec


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
        end = time.time()  # time()返回值单位为秒
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
print("The running time is {:02d} : {:02d}".format(int(duration_h), int(duration_m)))



# 邮件提醒服务
if mail_notice == "y":
    sender = "result.and.notification.center@gmail.com"
    pwd = "notification"
    
    # 构建邮件
    msg = EmailMessage()
    msg.set_content("TIME'S UP\nThe setting time is {:02d} : {:02d}\nThe running time is {:02d} : {:02d}".format(hours_copy, minutes_copy, int(duration_h), int(duration_m)))
    msg["Subject"] = "TIME'S UP"
    msg["From"] = sender
    msg["To"] = receiver


    
    try:
        # 建立SMTP连接
        smtpObj = smtplib.SMTP(host="smtp.gmail.com", port=587)
        # 不需要显式调用smtplib.ehlo()方法
        smtpObj.starttls()  # 加密连接
        smtpObj.login(sender, pwd)
        smtpObj.sendmail(sender, receiver, msg.as_string()) 
    finally:
        smtpObj.quit()
    
