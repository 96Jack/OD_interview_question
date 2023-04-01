# coding:utf-8 
#处理输入
m, n = [int(x) for x in input().split()]
weights = [int(x) for x in input().split()]
#对重量排序处理
weights = sorted(weights)
#第二步，左右指针向中间移动
re = 0
l = 0
r = len(weights) - 1
# 隐藏条件：
# 1. 人的重量一定小于等于车的重量
# 2. 一辆车最到坐两个人
# 正好全部配对
while l < r:
    if weights[l] == m:
        l += 1
        re += 1
        continue 
    elif weights[r] == m:
        r -= 1
        re += 1
        continue
    elif weights[l] + weights[r] <= m:
        l += 1
        r -= 1
        re += 1
        continue
# 除了多出的一个人，其他全部配对成功
if l == r:
    re += 1
print(re)

    
        