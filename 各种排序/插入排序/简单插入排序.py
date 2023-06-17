#思路：
# 1. 从第二张牌开始依次向后取牌
# 2. 取出的牌从当前位置向前依次比较，当取出的牌比前一张牌小时，继续往前移动比较
# 3. 直到当前的牌比前一张牌大时停止比较，并插入空位
# ex:      1 2 3 4       |32 8 7 9 10 21

l= [ 19, 2, 34, 23, 78, 9]

def Insertsort(lst):
    for i in range(1, len(lst)):
        j = i
        target = lst[i]                   # 从第二个数依次往后取所有的数
        # 使得前面比较过的数据都是有序数列
        while j>0 and target < lst[j-1]:  # 依次向前比较排序，目标值小的时候，前面排好序的数据依次向后挪一位，直到比较大时插入空位 
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = target                   # 直到比较大时插入空位 
    return lst


print(Insertsort(l))