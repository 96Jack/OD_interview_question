class Node():
    def __init__(self, data):
        self.data = data 
        self.next = None

class Link_node():
    def __init__(self):
        self.head = None 

    def print_l(self):
        ptr = self.head 
        while ptr:
            print(ptr.data)
            ptr = ptr.next
    def beging(self, newdata):
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node

    def ending(self, newdata):
        newnode = Node(newdata)
        # 若是一个空链表，那么尾部插入的数据就是第一个数据head
        if self.head == None:
            self.head = newnode
            return 
        last_node = self.head
        # 尾部的数据指针指向null
        while last_node.next:
            last_node = last_node.next
        last_node.next = newnode

    def between(self, pre_node,newdata):
        """
        给定插入位置的前一个节点
        既可以从头插入元素，又可以从尾部插入元素
        """
        if pre_node == None:
            print("请输入插入节点的前一个节点")
            return 
        newnode = Node(newdata)
        # 先将新节点的下一个节点和前一个节点的下一个节点链接
        # 【】 -> []
        # 【】 -> []
        newnode.next = pre_node.next
        pre_node.next = newnode   
    
    def remove(self,rm_data):
        curr_node = self.head
        if curr_node:
            # 若头部数据和待删除的数据相等
            if curr_node.data == rm_data:
                self.head = curr_node.next
                return 
        while curr_node:
            if curr_node.data == rm_data:
                break
            # 当前节点往后移动一位， 直到找到待删除的数据为止
            pre_node = curr_node
            curr_node = curr_node.next
        if curr_node == None :
            return 
        pre_node.next = curr_node.next
    
        
        


        
link = Link_node()
n1 = Node(15)
n2 = Node(25)
n3 = Node(35)
n1.next = n2
n2.next = n3
link.head = n1

link.print_l()
# print("*"*20,"从头插入元素","*"*20)
# link.beging(45)
# link.print_l()
# print("*"*20,"从尾插入元素","*"*20)
# link.ending(0)
# link.print_l()
print("*"*20,"从中间插入元素","*"*20)
link.between(n1,20)
link.print_l()
print("*"*20,"从中间删除元素","*"*20)
link.remove(20)
link.print_l()
