#在数组：1,2,3,4,7,9,10中查找元素2， 返回元素的下标

a = [1,2,3,4,7,9,10]
# target 在左闭右开区间
# 
class Solution():
    def search(self, nums, target) -> int:
        left , right = 0, len(nums)

        while left < right :
            middle = left + (right - left)//2
            if nums[middle] > target:
                right = middle        # target 在左区间[left, middle)
            elif nums[middle] < target:
                left = middle + 1     # target 在右区间[middle+1, right)
            else:
                return middle         # 数组中找到目标值，直接返回下标
        return -1 # 未找到目标值
    

find_num_index = Solution()
re = find_num_index.search(a, 1)
print(re)