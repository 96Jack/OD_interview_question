class LinkNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
l1 = None 
for i in [4, 3, 1]:
    l1 = LinkNode(i, l1)
l2 = None 
for i in [4, 2, 1]:
    l2 = LinkNode(i, l2)

