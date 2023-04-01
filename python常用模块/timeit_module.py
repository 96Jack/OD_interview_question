from timeit import timeit, repeat

def func():
    s = 0
    for i in range(100):
        s += i

# timeit参数：  待测函数，需要传入参数， number:测试次数，  
t = timeit('func()', 'from __main__ import func', number=100)
print(f"t: {t}")

# repeqt: 重复测试5次，每次执行100遍, 返回每次执行的时间列表
t1 = repeat('func()', 'from __main__ import func', number=100, repeat=5)

print(f"t1: {t1}")
