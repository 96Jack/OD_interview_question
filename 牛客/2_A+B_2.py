n = int(input())

n_list = []
for i in range(n):
    a = list(map(int,input().split(" ")))
    n_list.append(a)

for a, b in n_list:
    print(a+b)
    