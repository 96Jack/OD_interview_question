# [1,1,0,1,2,1,0]
# left = [2,1]
# right = [1,0]

nums = [int(x) for x in input().split()]



print(nums)
def func(nums):
    left = 0
    result_l = []
    for i in range(len(nums)):
        if nums[i] == 1:
            left += 1
        elif nums[i] == 0:
            result_l.append(left)
            left = 0
        else:
            left = 0
            continue
    return result_l

# left
a = func(nums)
# right
b = func(nums[::-1])
b = b[::-1]
print(a, b)
# 先遍历出0左边友好的座位， 再遍历出0右边友好的座位，最后将左右友好度相加即为0空位的友好度，最后求最大值
print(max([a[i]+b[i] for i in range(len(a))]))


