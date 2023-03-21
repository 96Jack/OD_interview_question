# [1,1,0,1,2,1,0]
# left = [2,1]
# right = [1,0]

n = [int(x) for x in input().split()]
print(n)

def get_friend(n):
    result_lst = []
    re = 0
    for i in n:
        if i==0:
            result_lst.append(re)
            re = 0
        elif i==1:
            re += 1
        else:
            re = 0
    return result_lst


left = n
right = n[::-1]
print(right)

left_re = get_friend(left)
right_re = get_friend(right)[::-1]

print(left_re, right_re,len(left_re))

print(max([left_re[i]+right_re[i] for i in range(len(left_re))]))