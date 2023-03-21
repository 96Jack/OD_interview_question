import math
n = input()
f = n.split(".")[-1]
m = int("5".ljust(len(f), "0"))
print(int(f), m)

if int(f) >= m:
    print(math.ceil(float(n)))
else:
    print(int(float(n)))