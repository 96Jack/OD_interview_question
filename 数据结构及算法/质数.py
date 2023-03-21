# 质数=素数，指的是大于1的自然数中，除了1和本身外没有其他因数
# 解法： 对1到本身这个区间的所有数取余，若只有两个数（1和本身）可以整除，则这个数为质数


# 求n以内的所有质数
# num = []  # 定义一个空列表用来接收找到的符合条件的数字

# n = int(input())
# for i in range(2, n+1):
#     mark = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             mark += 1
#     if mark == 2:
#         num.append(i)
# print(num)

# 判断一个数是不是质数， 除了1和自身不能被其他数整除
n = int(input())
mark = True
for i in range(2, n):
    if n % i == 0:
        mark = False
print(mark)