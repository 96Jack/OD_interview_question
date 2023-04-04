logs = [int(x) for x in input().split()]

max_num = logs[0]
# ex: [3 7 40]
# 公式： 在 3， 3+7-3*1，3+7+40-3*2-7*1 中取最大值  
for i in range(len(logs)):
    # 取每次往前加一个元素的分割列表
    log_list = logs[0:i+1]
    num_list = [i for i in range(len(log_list))][::-1]
    dis = [log_list[i]*num_list[i] for i in range(len(log_list)-1)]
    max_num = max(max_num, sum(log_list)-sum(dis))
    if sum(log_list) <= 100:
        max_num = max(max_num, sum(log_list)-sum(dis))
    else:
        max_num = max(max_num, 100 - sum(dis))
        break

print(max_num)