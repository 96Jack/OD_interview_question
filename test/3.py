s = input()

def func(s):
    if len(s) <= 1:
        return [s]
    l = []
    for i in range(len(s)):
        for j in func(s[0:i] + s[i+1:]):
            l.append(s[i] + j)
    return l

print(func(s))