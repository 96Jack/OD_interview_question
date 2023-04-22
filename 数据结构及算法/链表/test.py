class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None 

class Link_node():
    def __init__(self):
        self.head = None 

    def print_l(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def beging(self, newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode

    def ending(self, newdata):
        newnode = Node(newdata)
        curr_node = self.head
        if self.head == None:
            self.head = newnode
            return 
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = newnode

    def betwween(self, pre_node, newdata):
        # 需要指定插入位置的前一个节点
        if pre_node == None:
            print("请输入插入节点的前一个节点")
            return
        newnode = Node(newdata)
        newdata.next = pre_node.next
        pre_node.next = newnode
    
    def remove(self, rm_data):
        curr_node = self.head
        # 从头查找符待删除数据的值
        if curr_node.data == rm_data:
            self.head = curr_node.next
            return 
        while curr_node:
            if curr_node.data == rm_data:
                break
            pre = curr_node
            curr_node = curr_node.next
        if curr_node == None:
            return 
        pre.next = curr_node.next
        


n1 = Node(5)
n2 = Node(15)
n3 = Node(25)
n1.next = n2
n2.next = n3
link = Link_node()    
link.head = n1
link.print_l()
print("*"*20,"从中间删除元素","*"*20)
link.remove(25)
link.print_l()