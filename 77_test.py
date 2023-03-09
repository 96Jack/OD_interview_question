# 处理输入
import math 

m, n = list(map(int, input().split(" ")))
fields = list(map(int, input().split(" ")))

def func(k, fields):
    days = 0
    for i in range(len(fields)):
        days += math.ceil(fields[i] / float(k))
        print(f"days{days} += math.ceil({fields[i]} / {float(k)})")
    return days

if (len(fields) > n ):
    print(-1)
elif(len(fields) == n):
    print(max(fields))
else:
    # 找到最小值
    fields = sorted(fields)
    left = 0
    # 右边最大值
    print(f"fields:{fields}")
    right = fields[-1]
    print(f"right:{right}")
    result = -1
    while (left+1 < right):
        # 取中间值k为效能
        k = int(math.ceil(float(left + right ) / 2))
        print(f"k:{k}")
        days = func(k, fields)
        print(f"days:{days}")
        if days -n > 0:
            left = k
            print(f"left:{left}")
        else:
            right = k
            result = k
            print(f"right:{right}")
            print(f'result:{result}')
    print(result)





