import sys 
b = sys.stdin
print(f"b:{b}")
for line in sys.stdin:
    a = line.split()
    print(f"a:{a}")
    print(int(a[0])+int(a[1]))