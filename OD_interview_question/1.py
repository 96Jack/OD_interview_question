import functools

# 输入
task_num = int(input())

ranges = []
while task_num > 0:
    range_list = list(map(int, input().split(" ")))
    ranges.append(range_list)
    task_num -= 1

# 区间排序

def comp(x, y):
    return x[0] - y[0]

ranges = sorted(ranges, key=functools.cmp_to_key(comp))

# 点排序
points = set()
for i in ranges:
    points.add(i[0])
    points.add(i[1])

points = sorted(points)

# 运算

result = 0
ignore = set()
for point in points:
    current_num = 0
    print("point:",point)
    for i in range(len(ranges)):
        if i in ignore:
            continue
        start = ranges[i][0]
        end = ranges[i][1]
        count = ranges[i][2]

        if point < start:
            break
        elif point < end:
            current_num += count
        else:
            ignore.add(i)
        
    result = max(result, current_num)

print(result)


        






