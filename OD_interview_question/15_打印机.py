printers = [[] for _ in range(5)]
fid = 0
N = int(input())
orders = []
for i in range(N):
    orders.append(input().split(" "))
 
 
import heapq
for i, order in enumerate(orders):
    opt = order[0]
    if opt == 'IN':
        _, p, rank = order
        fid += 1
        heapq.heappush(printers[int(p)-1], (-int(rank), fid))
    elif opt == 'OUT':
        p = int(order[1])
        if printers[p-1]:
            _, id = heapq.heappop(printers[p-1])
            print(id)
        else:
            print("NULL")