class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

n1 = Node(5)
n2 = Node(15)
n3 = Node(25)
n1.next = n2
n2.next = n3
# 将尾节点的指针指向头部
n3.next = n1
n = 0
curr = n1
while n< 6:
    print(curr.data)
    curr = curr.next
    n += 1

