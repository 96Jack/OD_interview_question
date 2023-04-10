import datetime 
while True:
    try:
        year, month, day = [int(x) for x in input().split()]
        # 参数为整数类型
        date = datetime.date(year, month, day)
        print(date)
        # %j一年中的一天作为 以零填充的十进制数。
        # 001, 002, ...123
        which_day = date.strftime('%j').lstrip('0')
        print(f"{date} 是今年的第{which_day}天")
        # %W： 大写的W; 一年中的周数 （星期一为第一天 周）作为十进制数。 新年的所有日子 第一个星期一之前 被视为在 第 0 周。
        # 001, 002, ...42
        # %U:  一年中的周数 （星期日为第一天 周）作为零填充 十进制数。整天都在 第一个前的新年 星期天被认为是在 第 0 周。
        which_week = date.strftime('%W').lstrip('0')
        print(f"{date} 是今年的第{which_week}周")

        # 计算时间差
        current_time = datetime.datetime.now()
        # 可加减的时间差： 参数指定weeks=0, days=0, hours=0, minutes=0, secnonds=0  
        time_delta = datetime.timedelta(days=1)
        time_result = (current_time + time_delta).strftime("%Y-%m-%d %H-%M-%S")
        print("明天这个点的时间是：",time_result)
    except:
        break