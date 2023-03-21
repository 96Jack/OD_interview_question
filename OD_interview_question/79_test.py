# 处理输入

taskNum = int(input())
relationsNum = int(input())
relation_ids = []

for i in range(taskNum):
    relation_ids.append([int(x) for x in input().split(" ")])
print(relation_ids)

# 入度： 每个任务的前置依赖任务个数
upstream = [0 for i in range(taskNum)]
# 出度： 每个任务的下游任务
downstream = [[] for j in range(taskNum)]

# 初始化任务入度，出度
for task_1, task_2 in relation_ids:
    upstream[task_2] += 1
    downstream[task_1].append(task_2)
print(upstream)
print(downstream)

# 列表保存当前入度为0 的任务id
queue = []
result = 1
for i in range(taskNum):
    # 将所有入度为0 的任务入队，默认耗时为1
    if (upstream[i] == 0):
        queue.append([i, result])
print(queue)


while(len(queue)>0):
    task ,time  = queue.pop(0)
    for downstream_task in downstream[task]:
        upstream[downstream_task] -= 1
        if(upstream[downstream_task] == 0):
            result = time + 1
            queue.append([downstream_task, result])

print(result)


