l = []
while True:
    n = int(input())
    if n != 0:
        l.append(n)
    else:
        break
print(l)

def func(a,b):
    sum = a + b 
    c, d = sum//3, sum%3
    if c+d == 2 or c+d == 3:
        return sum + 1
    elif c+d > 3:
        return func(b, c)
    else:
        return 0
for i in l:
    a, b = i//3, i%3
    print(func(a, b))


