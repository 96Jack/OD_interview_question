# 四种数列生成性能

from timeit import Timer
# 1.循环“+”号连接
def test1():
    l = []
    for i in range(1000):
        l += [i]

# 2.append添加元素
def test2():
    l = []
    for i in range(1000):
        l.append(i)

# 3. 列表推导式
def test3():
    l = [i for i in range(1000)]

# 4.range函数转换列表
def test4():
    l = list(range(1000))

t1 = Timer("test1()","from __main__ import test1") 
print(f"concat {t1.timeit(number=1000)} s")

t2 = Timer("test2()","from __main__ import test2") 
print(f"append {t2.timeit(number=1000)} s")

t3 = Timer("test3()","from __main__ import test3") 
print(f"list {t3.timeit(number=1000)} s")

t4 = Timer("test4()","from __main__ import test4") 
print(f"range {t4.timeit(number=1000)} s")