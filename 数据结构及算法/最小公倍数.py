# 最大公约数 * 最小公倍数 = a * b 

def func(a, b):
    if b == 0:
        return a
    else:
        return(func(b, a%b))

a, b = list(map(int, input().split()))
result = a*b
# // 向下取整(不保留小数)， (除以/保留小数)

print(result//func(a, b))