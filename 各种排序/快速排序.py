# 思路：取最左边的数作为基数，
# 1. 在每个子分区的两端取左右指针，
# 2. 先比较右边数值，再比较左边数值
# 3. 当右边的数值比基数小时，指针停留
# 4. 当左边的数值比基数大时，指针停留
# 5. 交换左右指针数值， 实现左小右大
# 6. 递归分组

l = [ 19, 2, 34, 23, 78, 9]
def Quicksort(lst):
    # 此函数完成分区操作
    def partition(arr, left, right):
        key = left
        while left < right :
            while left < right and arr[right] >= arr[key]:
                right -= 1
            while left < right and arr[left] <= arr[key]:
                left += 1
            arr[left], arr[right] = arr[right], arr[left]
        arr[left], arr[key] = arr[key], arr[left]
        return left

    def quicksort(arr, left, right):
        if left >=  right:
            return
        # 从基准分区开始
        mid = partition(arr, left, right)
        # 递归调用
        quicksort(arr, left, mid-1)
        quicksort(arr, mid+1, right)

    # 主函数
    n = len(l)
    if n <= 1:
        return lst
    quicksort(l, 0, n-1)
    return lst

print(Quicksort(l))
     

