def str_sort(s=''):
    if len(s)<=1:
        return [s]
    str_list = []
    for i in range(len(s)):
        for j in str_sort(s[0:i] + s[i+1:]):
            str_list.append(s[i]+j)
    return str_list
print(str_sort('abc'))
