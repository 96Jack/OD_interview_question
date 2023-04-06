
num = int(input())



connect = []
for i in range(num):
    lst = input().split()
    input_temp = tuple(lst)
    connect.append(input_temp)
 
# 去重
connect = list(set(connect))
 
source = []
target = []
 
for item in connect:
    source.append(item[0])
    target.append(item[1])
 
source.sort()
target.sort()
 
print(source == target)