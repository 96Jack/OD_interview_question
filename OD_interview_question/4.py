# 输入

# m：限重
# n: 人数
input_1 = list(map(int,input().split(" ")))
m,n = input_1

# try except 复习 weight <= m；weights的数量控制；len(weights) =n
while 1:
    weights = [int(x) if int(x)<= m else -1 for x in input().split(" ")]

    try :
        if -1 not in weights:
            break
    except ValueError:
        raise("value error")

    print(weights)
# 先对体重内部排序
weights = sorted(weights,reverse=False)

# 左右指针向中间移动
left = 0
right = len(weights) -1

# 结果
min_bikes = 0

# 当前的重量
curr_weight= weights[left] + weights[right]

# 一辆车最多可载两人，人的重量< 车的载重

while (left < right):
    if (curr_weight > m):
        right -= 1
        min_bikes += 1
        curr_weight = weights[left] + weights[right]
    else:
        right -= 1
        left += 1
        min_bikes += 1
        curr_weight = weights[left] + weights[right]

if (left == right):
    min_bikes += 1
print(min_bikes)

