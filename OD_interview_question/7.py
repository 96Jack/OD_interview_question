# coding:utf-8
#JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。 
import functools
import copy
 
 
#处理输入
left, right = [int(x) for x in input().split()]
 
count = 0
for i in range(left, right+1):
    bin_str = str(bin(i))
    if '101' not in bin_str:
        count += 1
print(count)
 