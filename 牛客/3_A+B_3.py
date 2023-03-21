import sys

for line in sys.stdin:
    a = line.split()
    a.pop(0)
    print(sum([int(x) for x in a]))
