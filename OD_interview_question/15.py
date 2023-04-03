n = int(input())

in_printer = {"1":{}, "2":{}, "3":{}, "4":{}, "5":{}}
out_printer = []
for file in range(1, n+1):
    all_data = input().split()
    if all_data[0] == "IN":
        printer , priority = all_data[1], int(all_data[2])
        in_printer[printer].update({file:priority})
    else:
        out_printer.append(all_data[1])

# print(in_printer)
# 构造数据：{'1': {1: 1, 2: 2, 3: 3}, '2': {4: 1}, '3': {}, '4': {}, '5': {}}
#           '打印机': {文件: 优先级，}
# 字典的键的顺序不变，对键对应的嵌套字典排序
in_printer = {k:sorted(v.items(), key=lambda x: x[1]) for k,v in in_printer.items() if v != {}}

for out in out_printer:
    files = in_printer.get(out)
    count = len(files)
    if  count != 0:
        print(in_printer[out][count-1][0])
        in_printer[out].pop(count-1)
    else:
        print("NULL")



