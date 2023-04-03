strs = input().split()

# 按照长度排序
strs = sorted(strs, key=lambda x: len(x))
set_slen = set(len(l) for l in strs)
# print(set_slen)
if len(set_slen) == 1 :
    print(strs[-1])
else:
    flag = False
    # 倒数着取，1. 满足最长 2. 满足等长取最大字典序
    for s in strs[::-1]:
        for i in range(1,len(s)):
            if s[0:i] in strs:
                # 有子串：3. 满足有子串
                flag = True 
                break
        if flag:
            break
        else:
            continue
    
    if flag:
        print(s)
    else:
        # 没有子串且长度不等： a, b, cd : 取最长的那个
        print(strs[-1])