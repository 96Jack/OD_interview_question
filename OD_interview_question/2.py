# coding:utf-8
#JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。 
import functools
 
 
#处理输入
s = input().split()
 
#第一步，单词内部调整
new_list = ["".join(sorted(s[i])) for i in range(len(s))]
print(new_list)

#自定义排序函数

def comp(x, y):
    if new_list.count(x) > new_list.count(y):
        return -1
    elif new_list.count(x) == new_list.count(y):
        if len(x) > len(y):
            return 1
        elif len(x) == len(y):
            if x[0] > y[0]:
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1    

re = sorted(new_list, key=functools.cmp_to_key(comp))
print(" ".join(re))
