# coding:utf-8
#JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。 
import functools
import sys
from collections import Counter, defaultdict
import copy
from itertools import permutations
import re
import math
import sys
 
#处理输入
seats = [int(x) for x in input().split(" ")]
 
 
result=0
left=0
right=0
for i in range(len(seats)):
    if(seats[i]==1):
        left+=1
    elif(seats[i]==2):
        left=0
    elif(seats[i]==0):
        for j in range(i+1, len(seats)):
            if(seats[j]==1):
                right+=1
            elif(seats[j]==0 or seats[j]==2):
                break
            
        
        if(result<left+right):
            result=left+right
        
        right=0
        left=0
    
 
 
 
print(result)