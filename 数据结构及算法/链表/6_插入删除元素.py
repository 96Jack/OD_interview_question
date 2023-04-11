class Node():
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None 

class Linked_list():
    def __init__(self) -> None:
        self.head = None 

    def print_list(self):
        ptr = self.head 
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def beging(self, data):
        newdata = Node(data)
        # 从新建数的节点处建立链接关系
        newdata.next = self.head 
        self.head = newdata

    def ending(self, data):
        newdata = Node(data)
        ptr = self.head
        # 若链表中没有元素
        if ptr == None:
            self.head = newdata
            return 
        # 链表中至少一个元素
        while ptr.next:
            ptr = ptr.next
        ptr.next = newdata

    def between(self, prenode , newdata):
        if prenode == None:
            print("缺少插入节点的前节点")
            return
        currdata = Node(newdata)
        currdata.next = prenode.next
        prenode.next = currdata

    def remove(self, rm_data):
        ptr = self.head
        # 头节点是要删除的数据
        if ptr == rm_data:
            self.head = ptr.next
            return 
        while ptr:
            if ptr.data == rm_data:
                break
            prev = ptr
            ptr = ptr.next
        if ptr == None:
            return 
        # 后面的节点往前挪一位
        prev.next = ptr.next
            

link = Linked_list()
n1 = Node(1)
n2  = Node(2)
n3 = Node(3)
n4 = Node(4)
link.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
link.print_list()
link.beging(5)
print("*"*40)
link.print_list()
link.ending(6)
print("*"*40)
link.print_list()
link.between(n3,200)
print("*"*40)
link.print_list()
