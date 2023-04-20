def bubble(arry):
    n = len(arry)
    k = n
    for i in range(n):
        flag = True
        # for j in range(1, n-i):
        for j in range(1, k):    # 只遍历最后交换的位置
            if arry[j-1] > arry[j]:
                arry[j-1], arry[j] = arry[j], arry[j-1]
                k = j            # 记录最后交换的位置
                flag = False
        if flag:
            break
    return arry

a = [3, 5, 8, 2, 1, 9, 4]
print(bubble(a))