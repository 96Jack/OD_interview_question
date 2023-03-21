import functools

n = int(input())
string = [x for x in input().split(" ")]

def func(a,b):
    return ord(a[0]) - ord(b[0])

string = sorted(string, key=functools.cmp_to_key(func))
for i in string:
    print(i, end=" ")
