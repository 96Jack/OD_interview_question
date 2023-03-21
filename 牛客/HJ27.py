s = input()
a = ''
for i in s:
    if i.isalpha():
        a += i

b = sorted(a,key=str.upper) # 或者 d = sorted(a,key=str.lower) 字母排序，若相同的字母保留原来的排序

# len(b) < len(s)
index = 0
c = ''
for i in range(len(s)):
    if s[i].isalpha():
        # len(b) < len(s),用index记录排好序的b中字符对应的顺序
        c += b[index]
        index += 1
    else:
        c += s[i]
print(c)
    