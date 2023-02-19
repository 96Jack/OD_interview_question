import functools

# 输入
input_num = int(input())

ranges = []
while(input_num > 0):
    # input_str = input()
    # input_list = [int(x) for x in input_str.split(" ")]
    input_list = list(map(int,input().split(" ")))
    ranges.append(input_list)
    input_num -= 1

print(ranges)

# 区间排序

def comp_1(x,y):
    return x[0]-y[0]

ranges = sorted(ranges, key=functools.cmp_to_key(comp_1))
print(ranges)

# 点排序
def comp(x,y):
    return x-y

points = set()
for point in ranges:
    points.add(point[0])
    points.add(point[1])

print(points)
points = sorted(points,key=functools.cmp_to_key(comp))
print(points)

# 取核

result = 0
ignore = set()

for point in points:
    curren_num = 0 
    for i in range(len(ranges)):
        if (i in ignore):
            continue
        start = ranges[i][0]
        end = ranges[i][1]
        count = ranges[i][2]

        if (point < start):
            break
        elif(point < end):
            curren_num += count
        else:
            ignore.add(i)

    result = max(result,curren_num)

print(result)