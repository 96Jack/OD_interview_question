m ,n  = [int(x) for x in input().split(" ")]
#构造边的数据结构
i = 0
bianyuan = []
while i< m:
    bianyuan.append([int(x) for x in input().split()])
    i += 1
print(bianyuan)

result = 0
# 1 << 4 相当与 二进制数 10000， 遍历这个数字就可以将所有染色情况全部表达出来，（1表示红色， 0表示黑色）
for i in range((2**m)):
    mark = True
    for j in range(n):
        color_1 = (i >> (m-bianyuan[j][0]) & 1)
        color_2 = (i >> (m-bianyuan[j][1]) & 1)
        if color_1 == 1 and color_2 == 1:
            mark = False
            break

    if mark:
        result += 1
print (result)