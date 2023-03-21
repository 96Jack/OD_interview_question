n = int(input())

kv_dict = {}
for i in range(n):
    k,v = list(map(int, input().split()))
    kv_dict[k] = kv_dict.get(k,0) + v

for k in sorted(kv_dict.keys()):
    print(k,kv_dict[k])

