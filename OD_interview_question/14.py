m = int(input())
jimu_d = {}
index = 0
while index< m:
    n = int(input())
    if n in jimu_d:
        jimu_d[n].add(index)
    else:
        jimu_d[n] = {index}
    index += 1 

result = -1
for v in jimu_d.values():
    if len(v) > 1:
        max_dis = max(v)-min(v)
        # 找出所有重复元素的最大间距
        result = max(result, max_dis)

# 当所有索引集合不满足长度大于1时，即不重复数字
print(result)