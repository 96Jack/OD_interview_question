class Node():
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class Linked_node():
    def __init__(self) -> None:
        self.head = None
    
    def print_link(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def ending(self, newdata):
        """
        在链表的尾部添加新的节点
        """
        new_node = Node(newdata)
        if self.head == None:
            self.head = new_node
            return
        last_ptr = self.head
        while last_ptr.next:
            last_ptr = last_ptr.next
        last_ptr.next = new_node

link = Linked_node()
link.head = Node(5)
n2 = Node(15)
n3 = Node(25)
link.head.next = n2
n2.next = n3
link.print_link()
print("*"*20,"insert new number from end","*"*20)
link.ending(100)
link.print_link()



        