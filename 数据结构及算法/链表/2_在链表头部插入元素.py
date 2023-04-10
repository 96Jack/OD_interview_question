class Node():
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class Linked_list():
    def __init__(self):
        self.head = None

    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def begining(self, newdata):
        """
        在链表的头部添加新的节点
        """
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node



link = Linked_list()
link.head = Node(5)
n2 = Node(15)
n3 = Node(25)
link.head.next = n2
n2.next = n3
link.print_list()
# 在头部插入新元素
print("*"*20,"insert new number from head","*"*20)
link.begining(100)
link.print_list()

# 
