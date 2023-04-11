class Node():
    def __init__(self, data=None) -> None:
        self.data = data 
        self.next = None 

class Linked_node():
    def __init__(self) -> None:
        self.head = None

    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def between(self, pre_node, newdata):
        if pre_node == None:
            print("缺少插入节点前一个节点")
            return
        new_node = Node(newdata)
        new_node.next = pre_node.next
        pre_node.next  = new_node

link = Linked_node()
link.head = Node(5)
n2 = Node(15)
n3 = Node(25)
link.head.next = n2
n2.next = n3
link.print_list()
print("*"*20,"insert data in  middle ", "*"*20)
link.between(n2, 100)
link.print_list()