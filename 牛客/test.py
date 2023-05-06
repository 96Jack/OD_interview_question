class Node():
    def __init__(self, data=None, next=None):
        self.data = data 
        self.next = next

class LinkNode():
    def __init__(self):
        self.head = Node()
        self.length = 0

    def insert(self, val1, val2):
        cur = self.head
        new_node = Node(val2)
        while cur:
            if cur.data == val1:
                new_node.next = cur.next
                cur.next = new_node
                break
            else:
                cur = cur.next

    def remove(self, rm_data):
        cur = self.head
        if cur:
            if cur.data == rm_data:
                self.head = cur.next
                return
        while cur:
            if cur.data == rm_data:
                break  
            pre_node = cur
            curr = curr.next
        if curr == None:
            return 
        pre_node.next = curr.next

    def print_l(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next

nums = [int(x) for x in input().split(" ")]
lenght ,head = nums[0],nums[1]
del_num = nums[-1]
l = nums[2:-1]
i, j, pairs = 0, 1, []
while i < len(l):
    pairs.append((l[i], l[j]))
    i += 2
    j += 2
l = LinkNode()
#pairs = [(1,2),(3,2),(5,1),(4,5),(7,2)]
l.head.data = head
# print(pairs)
for p in pairs:
    l.insert(p[1],p[0])
# l.print_l()
l.remove(del_num)
# print()
l.print_l()


