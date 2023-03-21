import queue

ranges = [[0, 5, 3], [1, 2, 1], [3, 6, 3]]

pq = queue.PriorityQueue()
res = 0
temp_res = 0
for i in range(len(ranges)):
    while pq.qsize() > 0:
        print("pq.qsize:",pq.qsize())
        top = pq.queue[0]
        print("top:", top)

        if top[0] < ranges[i][0]:
            poll = pq.get() 
            temp_res -= poll[1]
            print("poll:",poll)
            print("temp_res:", temp_res)
        else:
            break

    print("*"*10,ranges[i][1], ranges[i][2])
    pq.put((ranges[i][1], ranges[i][2]))
    temp_res += ranges[i][2]
    print(r"temp_res:{temp_res}  res:{res}")

    if temp_res > res:
        res = temp_res
print(res)
