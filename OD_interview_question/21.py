from functools import reduce

# 若拓展模块不能用，自定义乘积函数
# def product(l):
#     result = l[0]
#     for i in range(1,len(l)):
#         result = result * l[i]
#     return result

n = [int(x) for x in input().split()]
l = []
for i in range(len(n)):
    if i == 0:
        a = 1
    else:
        a = reduce(lambda x, y:x*y, n[0:i])
        # a = product(n[0:i])
    if i == len(n) -1:
        b = 1
    else:
        b = reduce(lambda x, y:x*y, n[i+1::])
        # b = product(n[i+1::])
    # print(a, b)
    if a == b:
        l.append(i)

if len(l) >=1:
    print(l[0])
else:
    print(-1)


