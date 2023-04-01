n = 9
 
def func(n):
    if n < 2:
        return n
    else:
        return func(n-2)+func(n-1)

print(func(n))