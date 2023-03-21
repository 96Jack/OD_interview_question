# coding:utf-8
#JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。 
import math
 
def cal(k, fields):
    days = 0
    for i in range(len(fields)):
        # 对fields中的每个元素 除以 中间值k并向上取整
        days += math.ceil(fields[i] / float(k))
    return days

#处理输入
params = [int(x) for x in input().split(" ")]
m = params[0]
n = params[1]
fields = [int(x) for x in input().split(" ")]

# 最少天数小于果林大小可直接返回-1
if (n<len(fields)):
    print(-1)
elif(n==len(fields)):
    print(max(fields))
else:
    # 排序找到最小值
    fields = sorted(fields)
    left = 0
    # right为最大值
    right = fields[len(fields) - 1]

    result = -1
    while (left +1 < right):
        #取中间位置的值作为效能k，
        k = int(math.ceil(float(left + right) / 2))
        print(k)
        res = cal(k, fields)
    # 二分法：若天数多则说明中值小，需要更大的效能，取右边大区间
        if (res - n > 0):
            left = k
        else:
            # 若天数少则反之。
            result = k
            right = k
    print(result)
 