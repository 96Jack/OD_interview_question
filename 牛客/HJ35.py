# 蛇形矩阵

n = int(input())

for i in range(1, n+1):
    for j in range(i, n+1): 
        print((j**2+j)//2 - i+1, end=" ")
    print()