import sys

for strings in sys.stdin:
    print(type(strings))
    a = strings.strip()
    b = strings.split(",")
    c = strings.strip('\n').split(",")
    print("-"*10)
    print(a)
    print(b)
    print(c)
    # string = sorted(a)
    # print(",".join(string))