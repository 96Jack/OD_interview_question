# coding:utf-8
import functools
 
def comp(a, b):
    if a[0] == b[0]:
        return b[1] - a[1]
    else:
        return b[0] - a[0]
 
 
#处理输入
logs = [int(x) for x in input().split(" ")]
#加分
plus_score = [0 for x in range(len(logs))]
plus_score[0] = logs[0]
 
# 减分
minus_score = [0 for x in range(len(logs))]
 
result = [0 for x in range(len(logs))]
result[0] = logs[0]
 
for i in range(1, len(logs)):
    plus_score[i] = min(100, plus_score[i - 1] + logs[i])
    minus_score[i] = minus_score[i - 1] + plus_score[i - 1]
    result[i] = plus_score[i] - minus_score[i]
 
    if (plus_score[i] >= 100):
        break
 
print(max(result))
 