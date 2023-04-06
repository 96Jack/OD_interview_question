m = int(input())
l = []
for i in range(m):
    a, b = [int(x) for x in input().split()]
    l.append([a, a+b])

new_l = sorted(l, key=lambda x: x[1])
print(new_l)

last_end_time = 0
count = 0
for start , end in new_l:
    if count == 0 and start >= last_end_time:
        count += 1
        last_end_time = end
    elif start >= last_end_time + 15:
        count += 1
        last_end_time = end
print(count)