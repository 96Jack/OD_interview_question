# coding:utf-8
#JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。 


#处理输入
taskNum = int(input())
relationsNum = int(input())
relation_ids = []
for i in range(relationsNum):
    relation_ids.append([int(x) for x in input().split(" ")])
 
 
# 每个任务的前置依赖任务个数，也就是拓扑排序中的入度
# 列表中添加taskNum个0
upstream = [0 for x in range(taskNum)]
# 每个任务的下游任务， 也就是拓扑排序中的出度
# taskNum个空列表
downstream = [[] for x in range(taskNum)]
# print(f"upstream:{upstream}")
# print(f"downstream:{downstream}")
print(f"relation_ids:{relation_ids}")

#初始化入度、出度
"""
demo:
元素0,1,2,3,4之间的拓扑图
对于 relation_ids:[[0, 4], [1, 2], [1, 3], [2, 3], [2, 4]]
各元素[0,1,2,3,4]对应
入度是: upstream:[0, 0, 1, 2, 2]
出度是: downstream:[[4], [2, 3], [3, 4], [], []]
"""
for relation_id in relation_ids:
    # print(f"relation_id[1]:{relation_id[1]}"
    upstream[relation_id[1]]+=1 
    # print(f"relation_id[0]:{relation_id[0]}, relation_id[1]:{relation_id[1]}")
    downstream[relation_id[0]].append(relation_id[1])
    # print(f"downstream:{downstream}")
    # print(f"upstream:{upstream}")

print(f"upstream:{upstream}")
print(f"downstream:{downstream}")



#队列中保存当前入度为0 的任务id
queue = []
result = 1

for i in range(taskNum):
    #将所有入度为零的任务入队, 默认耗时为1
    if (upstream[i] == 0):
        queue.append([i, result]) 
print(f"queue:{queue}")

while (len(queue)> 0):
    current_task = queue.pop(0)
    task = current_task[0]
    time = current_task[1]
    print(f"task:{task},time:{time}")
    print(f"downstream:{downstream[task]}")
    for downstream_task in downstream[task]:
        # 当前任务的入度减小到0时，放入queue中
        print(f"downstream_task:{downstream_task}")
        print(f"upstream[downstream_task]:{upstream[downstream_task]}")
        upstream[downstream_task] -= 1
        print(f"upstream[downstream_task]:{upstream[downstream_task]}")
        if (upstream[downstream_task] == 0):
            result = time + 1
            queue.append([downstream_task, result])
            print(f"queue:{queue}")
            
print(result)
