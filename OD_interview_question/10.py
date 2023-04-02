# 暴力枚举
# 待用尺举法解

s = input()
mother_str = "WASD"
if len(s) == 4:
    count = 4
    son_strs = mother_str
    for i in range(len(son_strs)):
        if s[i] == son_strs[i]:
            count -= 1
    print(count)
else:
    result = []
    for i in range(len(s)-4):
        count = 4
        son_strs =  s[i+1:5+i] 
        for j in range(len(son_strs)):
            if son_strs[j] == mother_str[j]:
                count -= 1
        result.append(count)
    print(min(result))