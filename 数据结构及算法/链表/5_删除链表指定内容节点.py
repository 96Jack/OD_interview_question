class Node():
    def __init__(self, data=None) -> None:
        self.data = data 
        self.next = None 

class Linked_list():
    def __init__(self) -> None:
        self.head = None 

    def print_list(self):
        ptr = self.head
        while ptr :
            print(ptr.data)
            ptr = ptr.next

    def ending(self, newdata):
        new_node = Node(newdata)
        if self.head == None :
            self.head = new_node
            return 
        last_ptr = self.head
        while last_ptr.next:
            last_ptr = last_ptr.next
        last_ptr.next = new_node

    def rm_node(self,rmkey):
        ptr = self.head 
        # 删除第一个元素
        if ptr:
            if ptr.data == rmkey:
                self.head = ptr.next
                return 
        # 找到待删除的节点
        while ptr:
            if ptr.data == rmkey:
                break
            prev = ptr
            ptr = ptr.next
        if ptr == None:  # 到了末端
            return 
        prev.next = ptr.next

link = Linked_list()
link.ending(5)
link.ending(15)
link.ending(25)
link.print_list()
print("*"*30)
link.rm_node(15)
link.print_list()
