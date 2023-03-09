# coding:utf-8
#JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。 
#处理输入

nums = [int(x) for x in input().split(" ")]
m = int(input())
#排序找到最小值
nums = sorted(nums)
min_num = nums[0]
        
def dfs(nums, index, num_sum, count):
        print(f"nums:{nums}, index:{index}, num_sum:{num_sum}, count:{count}")
        if (num_sum > m):
            return count
        #满足边界条件+1
        print(f"num_sum:{num_sum} m-min_num:{m-min_num}")
        if (num_sum <= m and m - min_num < num_sum):
            return count + 1
    
        for i in range(index, len(nums)):
            print(f"nums, i, num_sum + nums[i], count : {nums, i, num_sum + nums[i], count}")
            count = dfs(nums, i, num_sum + nums[i], count)
    
        return count
 
print(dfs(nums, 0, 0, 0))
 
 
 
 
 