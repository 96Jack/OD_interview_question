m = int(input())
l1 = [int(x) for x in input().split()]
n = int(input())
l2 = [int(x) for x in input().split()]

print(l1)
print(l2)
# 构造数据： {重复数字：(在l1中出现的次数， 在l2中出现的次数)}
# 结果 = 各个重复数字在不同列表出现次数乘积的和
result_d = {num:(l1.count(num), l2.count(num)) for num in l2 if num in l1}
print(result_d)
mid = [v[0]*v[1] for v in result_d.values()]
result = sum(mid)
print(result)