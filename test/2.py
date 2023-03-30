out = 0
s = input()

for i in range(0, len(s)):
    # 奇
    k = i-1
    j = i+1
    len_ji=1
    while k >=0 and j < len(s): 
        if s[k] == s[j]:
            k -= 1
            j += 1
            len_s += 2
        else:
            break
    
    # 偶
    k = i
    j = i+1
    len_ou = 0
    while k >=0 and j < len(s):
        if s[k] == s[j]:
            k -=1 
            j += 1
            len_ou += 2
        else:
            break
    len_s = max(len_ji, len_ou)   
    if out < len_s:
        out = len_s

print(out) 
    
