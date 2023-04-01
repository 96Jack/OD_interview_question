n = int(input())
m = input().split()
x = input().split()

we , l = [], {0}

for i in range(n):
    we.extend([int(m[i])]*int(x[i]))

for i in we:
    # 取并集， 新的重量无非是前面有的重量加上一个新的重量组成的
    # 1 + 0          =>  {0, 1}          : 1和0可以构成的重量
    # 1 + {0, 1}     =>  {0, 1, 2}       ：1和{0， 1}可以构成的重量
    # 2 + {0, 1, 2}  =>  {0, 1, 2, 3, 4} ：2和{0， 1， 2}可以构成的重量
    l = l.union({i+j for j in l})
print(len(l))
