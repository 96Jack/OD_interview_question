def all_char(s):
    if len(s)<=1:
        return [s]
    c_list = []
    for i in range(len(s)):
        # 去除i字符，让i字符和剩余的字符组合
        for j in all_char(s[0:i] + s[i+1:]):
            c_list.append(s[i] + j )
    return c_list

s = all_char("abcdd")
print(list(set(s)))
