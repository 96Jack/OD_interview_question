logs = [int(x) for x in input().split()]

max_num = logs[0]
for i in range(len(logs)):
    log_list = logs[0:i+1]
    print(log_list)
    num_list = [i for i in range(len(log_list))][::-1]
    print(num_list)
    dis = [log_list[i]*num_list[i] for i in range(len(log_list)-1)]
    print(dis)
    if sum(log_list) <= 100:
        max_num = max(max_num, sum(log_list)-sum(dis))
    else:
        max_num = max(max_num, 100 - sum(dis))
        break

print(max_num)