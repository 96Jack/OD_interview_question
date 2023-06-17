def bubble(arry):
    n = len(arry)
    for i in range(n):               # 从头开始的次数
        flag = True
        for j in range(0, n-i-1):    # 从头部开始相邻的两个数据依次两两比较
            if arry[j] > arry[j+1]:
                arry[j], arry[j+1] = arry[j+1], arry[j]
                flag = False         # 无两两换位时，比较结束，避免重复
        if flag:
            break
    return arry

a = [3, 5, 8, 2, 1, 9, 4]
print(bubble(a)) 