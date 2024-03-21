class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head = None):
        self.head = head
    
    def isEmpty(self):
        return (self.head == None)
    
    def addToHead(self, node):
        if self.isEmpty:
            self.head = node
        else:
            node.next = self.head
            self.head = node
