import functools

# 输入数据
task_num = int(input())
ranges = []

while(task_num>0):
    input_str = input()
    input_list = [int(x) for x in input_str.split(" ")]
    ranges.append(input_list)
    task_num -= 1

print(ranges)

# 区间排序
def comp1(x,y):
    return x[0]-y[0]

ranges = sorted(ranges,key=functools.cmp_to_key(comp1))
print(ranges)

# 点排序
def comp(x,y):
    return x-y

points = set()
for single_range in ranges:
    points.add(single_range[0])
    points.add(single_range[1])
points = sorted(points,key=functools.cmp_to_key(comp))

print(points)

# 在区间内的时间点，result=该区间核 + 交集区间核 ，否则跳过该区间
result = 0
ignore = set()
for point in points:
    curr_num = 0
    for i in range(len(ranges)):
        if (i in ignore):
            continue
        start = ranges[i][0]
        end = ranges[i][1]
        count = ranges[i][2]
        # 取左闭右开区间
        if (point < start):
            break
        elif(point < end):
            curr_num += count
        else:
            ignore.add(i)
    result = max(result,curr_num)

print(result)
        