colors = [int(x) for x in input().split()]
second = int(input())

# 按照second时间间隔取出车辆
if second != 0:
    l = []
    for i in range(len(colors)-second+1):
        bus_dict = {bus:colors[i:second+i].count(bus) for bus in colors[i:second+i] }
        result = max(bus_dict.values())
        l.append(result)
    print(max(l))
else:
    print(0)