import math

num , days = [int(x) for x in input().split()]
fields = [int(x) for x in input().split()]

if days < len(fields):
    print(-1)
elif days == len(fields):
    print(max(fields))
else:
    fields = sorted(fields)
    left, right = 0, fields[-1]
    result = -1
    while left  < right -1:
        middle = math.ceil((left + right)/2)
        day = [math.ceil(field/middle) for field in fields]
        print(day)
        result = sum(day)
        if result - days > 0:
            left = middle
        else:
            right = middle
            result = middle
    print(result)
