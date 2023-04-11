#在数组：1,2,3,4,7,9,10中查找元素2， 返回元素的下标

a = [1,2,3,4,7,9,10]
# target 在左闭右闭区间
class Solution():
    def search(self, nums, target) -> int:
        left , right = 0, len(nums)-1       # 定义target在左闭右闭的区间里，[left, right]

        while left <= right :
            middle = left + (right - left ) // 2
            if nums[middle] > target:        # target在左区间，所以[left, middle - 1]
                right = middle -1
            elif nums[middle] < target:
                left = middle +1                 # target在右区间，所以[middle + 1, right]
            else:
                return middle                   # 数组中找到目标值，直接返回下标
        return -1               # 数组中找到目标值，直接返回下标
    
find_index = Solution()
re = find_index.search(a, 9)
print(re)