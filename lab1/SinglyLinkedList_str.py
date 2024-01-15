class Node:
    def __init__ (self, data):
        self.data = data 
        self.next_node = None

    def __repr__(self):
        return "<Node data: %s>" % self.data

class SinglyLinkedList:
    def __init__ (self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def count(self):
        current = self.head
        count = 0 

        while current:
            count += 1
            current = current.next_node

        return count
    
    def addToHead(self, data):
        newnode = Node(data)
        newnode.next_node = self.head
        self.head = newnode

    def addToTail(self, data):
        newnode = Node(data)
        if self.is_empty():
            self.head = newnode
        else:
            current = self.head 
            while current.next_node is not None:
                current = current.next_node
            current.next_node = newnode

    def traverse(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next_node

        return nodes
    
    def deleteFromHead(self):
        if self.head is None:
            raise ValueError
        current = self.head
        self.head = self.head.next_node
        return current
        
    def deleteFromTail(self):
        if self.head is None:
            return None
        if self.head.next_node is None:
            self.head = None
            return None
        current = self.head 
        while current.next_node.next_node:
            current = current.next_node
        deleted = current.next_node
        current.next_node = None

        return deleted

    def deleteAfter(self, key):
        current = self.head
        latter = None
        while current and current.next_node is not None:
            if current.data == key:
                if current.next_node.next_node is None:
                    latter = current.next_node
                    current.next_node = None
                else:
                    latter = current.next_node
                    current.next_node = current.next_node.next_node
            current = current.next_node
        return latter
            
    def Del(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node

            elif current.data == key:
                found = True
                previous.next_node = current.next_node

            else:
                previous = current
                current = current.next_node

        return current
    
    def search(self, target):
        current = self.head
        count = 0
        while current:
            if current.data == target:
                return count
            count += 1
            current = current.next_node
        if current is None:
            raise IndexError
        
    def display(self):
        current = self.head

        while current:
            print(current.data, end = ' -> ')
            current = current.next_node






