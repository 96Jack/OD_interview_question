# 辗转相除法，欧几里得算法
# 第一次的除数作为下一次运算的被除数，取被除数的余作为下一次运算的除数，

def fn(a, b):
    if b == 0:
        return a
    else:
        return(fn(b, a%b))

# 默认以空格分割
a, b = list(map(int, input().split()))
print(fn(a,b))
