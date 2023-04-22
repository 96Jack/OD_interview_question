class Node():
    def __init__(self,data=None, next=None) -> None:
        self.data = data
        self.next = next

class Solution():
    def merge(self, list1, list2):
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        # 设置哨兵节点(preindex)和指针(prevalue)
        preindex = prevalue = Node(-1)
        """
        如果 list1 当前节点的值小于等于 list2 ，我们就把 list1 当前的节点接在 prevalue 节点的后面同时将 list1 指针往后移一位。否则，我们对 list2 做同样的操作。不管我们将哪一个元素接在了后面，我们都需要把 prevalue 向后移一位。在循环终止的时候， list1 和 list2 至多有一个是非空的。我们只需要简单地将非空链表接在合并链表的后面，并返回合并链表即可
        """
        while list1 and list2:
            if list1.data <= list2.data:
                prevalue.next = list1
                list1 = list1.next
            else:
                prevalue.next = list2
                list2 = list2.next
            prevalue = prevalue.next
        # 合并后，剩余部分，直接指完
        prevalue.next = list1 if list1  else list2
        return preindex.next
    
def create_link(l):
    list1 = None
    for i in l[::-1]:
        list1 = Node(i, list1)
    return list1

list1 = create_link([1, 2, 4])
list2 = create_link([1, 3, 4])

result = Solution()
merge_link = result.merge(list1, list2)
while merge_link:
    print(merge_link.data)
    merge_link = merge_link.next
