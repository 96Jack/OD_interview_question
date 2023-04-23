# target = 7, nums = [2,3,1,2,4,3]

def func(n, l):
    if sum(l) < n:
        return 0
    if l[-1] >= n:
        return 1
    result = []
    for i in range(len(l)-1):
        sum_l = l[i]
        target = 0
        while sum_l < n:
            i+=1
            target += 1
            sum_l = sum_l+l[i]
        else:
            result.append(target+1)
    print(min(result))

if __name__ == "__main__":
    target = int(input())
    nums = [int(x) for x in input().split(",")]
    result = func(target, nums)
    print(result)
给定一个含有n个正整数的数组和一个正整数target。
找出该数组中满足其和≥target的长度最小的连续子数组[numsl, numsl+1, ..., numsr-1, numsr]，并返回其长度。如果不存在符合条件的子数组，返回0。

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

示例 2：
输入：target = 4, nums = [1,4,4]
输出：1

示例 3：
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
提示：
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105