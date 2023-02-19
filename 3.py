import functools

input_str = input().split(" ")

# 单词间排序
new_str = []
for world in input_str:
    new_str.append("".join(sorted(world)))

print(new_str)

# 单词出现次数;字典排序
str_count = {}
for i in new_str:
    if i in str_count:    
        str_count[i] += 1
    else:
        str_count[i] = 1

# 排序函数
# 1.单词出现的次数，降序
# 2.次数相同，按单词长度升序
# 3.次数和单词数均相同，按字典升序 
def comp(a,b):
    if (a[1] > b[1]):
        return -1
    elif (a[1] == b[1]):
        if (len(a[0]) > len(b[0])):
            return 1
        elif (len(a[0]) == len(b[0])):
            if (a[0] > b[0]):
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return 1

list1 = sorted(str_count.items(),key=functools.cmp_to_key(comp))

print(list1)

res_str = ""
for item in list1:
    for i in range(item[1]):
        res_str += item[0] + " "

print(res_str)
