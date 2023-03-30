# 最长回文子串

#  answer-1 
# s = input()
# l = []
# n = len(s)

# for i in range(0, n-1):
#     for j in range(1, n):
#         if s[i] == s[j] and s[i+1:j] == s[j-1:i:-1]:
#             l.append(s[i:j+1])
            
# print(l)


# answer-2
# ABA型： 从当前字符向两边扩散，比较左右字符是否相等，找出当前字符中心的最长字串。
# ABBA型： 从当前和相邻下一个字符扩散，比较左右字符是否相等。



s = input()
out = 0


for i in range(0, len(s)):  # 双指针
    # 奇数回文子串
    k = i - 1
    j = i + 1
    len_ABA = 1
    while k >= 0 and j < len(s):
        if s[k] == s[j]:
            print(s[k:j+1])
            k -= 1
            j += 1
            len_ABA += 2
        else:
            break

    # 偶数回文子串 
    k = i
    j = i + 1
    len_ABBA = 0
    while k >= 0 and j < len(s):
        if s[k] == s[j]:
            print(s[k:j+1])
            k -= 1
            j += 1
            len_ABBA += 2
        else:
            break
      
    now_len = max(len_ABA, len_ABBA)
    if out <now_len:
        out = now_len
print(out)
