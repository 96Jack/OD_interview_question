# def sort_s(s):
#     s_list = []
#     if len(s) <= 1:
#         return([s])
#     for i in range(len(s)):
#         for j in sort_s(s[0:i] + s[i+1:]):
#             s_list.append(s[i]+j)
#     return s_list

# strings = [x for x in input().split()]
# s_arg = strings[-2]
# s_new = strings[1:-2]
# k = int(strings[-1]) - 1

# all_strs = sort_s(s_arg)
# s_list = [s for s in all_strs if s in s_new]

# print(set(s_list))
# if s_arg in s_list:
    
#     print(len(s_list)-1)
#     s_list.remove(s_arg)
#     print(s_list[k])
#     print(s_list)
# else:
#     print(len(s_list))
#     print(s_list[k])
#     print(s_list)
while True:
    try:
        st=input().split()
        n=int(st[0])
        s_for_sort=st[1:n+1]
        s=st[-2]
        k=int(st[-1])
        a=[]
        for i in s_for_sort:
            if len(i)==len(s) and i!=s and sorted(i)==sorted(s):
                a.append(i)
        print(len(a))
        if a and k<=len(a):
            print(sorted(a)[k-1])
    except:
        break