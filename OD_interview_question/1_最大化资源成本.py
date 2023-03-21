# coding:utf-8
#JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。

import functools

def comp(a, b):
    return a - b


def comp1(x, y):
    return x[0] - y[0]

result_machine = 0

#处理输入
task_num = input()

i = int(task_num)
ranges = []
while(i>0):
    input_list = [int(x) for x in input().split(" ")]
    # input_list = list(map(int,input().split(" ")))
    ranges.append(input_list)
    i=i-1
#区间排序
ranges = sorted(ranges, key=functools.cmp_to_key(comp1)) # 按照所有区间的开始值排序
print("ranges:",ranges)
points = set()
for single_range in ranges:
    points.add(single_range[0])
    points.add(single_range[1])

# print("-"*20,points)
#点排序
points = sorted(points, key=functools.cmp_to_key(comp))
# print("points",points)

# 判断排序好的所有时间点，是否在排好序的区间内（左闭右开），若在则将该时间点所需的服务器数量 + 该区间的服务器数量
result =0
ignore = set()
# print("ignore",ignore)
for point in points:
    current_sum = 0
    # i 为range的索引，当point的值比区间结束值大时，则不在该区间内，记录该区间的索引，
    # 后面比当前大的point跳过记录的区间（后面的point肯定也不在当前区间，且比当前区间大）
    for i in range(len(ranges)):
        # print('i:',i)
        # print("ignore:",ignore)
        if (i in ignore):
            continue
        start = ranges[i][0]
        end = ranges[i][1]
        count = ranges[i][2]
        # print("point:",point)
        # print("start:",start)
        # print("end:",end)
        if (point < start):
            break
        elif (point < end):
            current_sum += count
            # print("current_sum:",current_sum)
        else:
            ignore.add(i)
    result = max(result, current_sum)
print(result)
# points [0, 1, 2, 3, 5, 6]
# 3
# 0 5 1
# 3 6 2
# 1 2 1