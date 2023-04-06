n = int(input())
shows = []
for i in range(n):
    t, l = map(int, input().split())
    shows.append((t, t + l))  # 将演出时间转换为起始和结束时间

print(shows)
shows.sort(key=lambda x: x[1])  # 按结束时间排序
print(shows)
# 4
# 0 45
# 45 20
# 90 60
# 65 10

last_end_time = 0  # 上一个观看的演出的结束时间
count = 0  # 观看的演出场数
# 下一次要比较的值用第三个变量来传递
for start, end in shows:
    if count == 0 and start >= last_end_time:
        count += 1
        last_end_time = end  # 第一次观看
    else:
        if start >= last_end_time + 15:  # 如果该场演出的开始时间大于等于上一个观看的演出结束时间加上15分钟
            count += 1
            last_end_time = end  # 更新上一个观看的演出的结束时间

print(count)

