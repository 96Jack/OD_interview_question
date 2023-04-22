class List_node():
    def __init__(self, data=None, next=None):
        self.data = data 
        self.next = next
# 创建链表
l1 = None
l2 = None 
for i in [4,2,1]:
    l1 = List_node(i,l1)
for i in [4, 3, 1]:
    l2 = List_node(i, l2)
datas1 = []
datas2 = []
while l1:
    datas1.append(l1.data)
    datas2.append(l2.data)
    l1 = l1.next
    l2 = l2.next
print(datas1, datas2)