import math 

m, n = list(map(int, input().split(' ')))
fields = list(map(int, input().split(' ')))

 
def cal(k,fields):
    days = 0
    for i in range(len(fields)):
        # 对fields中的每个元素除中间值并向上取整
        days += math.ceil(fields[i] / float(k))
        print(f"days{days} += math.ceil({fields[i]} / {float(k)})")
    return days 

if (m > n):
    print(-1)
elif(m==n):
    print(max(fields))
else:
    # 排序找到最小值
    fields = sorted(fields)
    left = 0
    
    # right为最大值
    right = fields[len(fields)-1]

    result = -1
    while (left +1 < right):
        # 取中间的值作为效能k
        k = int(math.ceil(float(left + right) / 2))
        print(f"k:{k}")
        days = cal(k, fields)

        print(f"days:{days}")
        # 二分：若天数多则说明中值小，需要更大的效能，取右边大区间
        if (days - n > 0):
            left = k
            print(f"left:{left}")
        else:
            # 天数少则反之
            result = k
            right = k
            print(f"right:{right}")
    print(f"result:{result}")
