# 质因子： 质因子（或质因数）在数论里是指能整除给定正整数的质数（一个数的所有因子中是质数的就是质因子）
# 将一个正整数表示成质因数乘积的过程和得到的表示结果叫做质因数分解
# 360 = 2*2*2*3*3*5 = 2^3 X 3^2 X 5
# 短除法分解：processon


# 方法1：算法复杂度太高，运行太慢
# x = int(input())
# lst = []
# while x!=1:
#     for i in range(2, x+1):
#         if x%i == 0:
#             lst.append(i)
#             x = x//i
#             break
# print(*lst)


# 方法2：递归, range(2,int(a**0.5+2)) :为什么取这个范围
def prime(a):
    mark = 1
    for i in range(2,int(a**0.5+2)):
        if a%i == 0:
            # i是a的因子
            mark = 0
            print(i, end=" ")
            b = int(a/i)
            prime(b)
            break
    # 最后一个质数
    if mark == 1:
        print(a, end=' ')
prime(int(input()))