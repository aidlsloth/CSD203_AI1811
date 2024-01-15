class Node:
    def __init__(self, data, prev_node = None, next_node = None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node
    def __repr__(self):
        return "<Node data %s>" % self.data

class DoublyLinkedList:
    def __init__(self):
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
        new_node = Node(data, prev_node = None, next_node = self.head)
        
        if not self.is_empty():
            self.head.prev_node = new_node

        self.head = new_node

    def addToTail(self, data):
        new_node = Node(data, prev_node = None, next_node = None)
        lastnode = self.head
        while lastnode.next_node is not None:
            lastnode = lastnode.next_node
        
        lastnode.next_node = new_node
        new_node.prev_node = lastnode

    def addAfter(self, data, index):
        new_node = Node(data, prev_node = None, next_node = None)
        position = index
        current = self.head
        if index == 0:
            self.head.next_node = new_node
            new_node.next_node = self.head.next_node.next_node

        if index > 0:
            while position != 0:
                current = current.next_node
                position -= 1
            new_node.next_node = current.next_node
            current.next_node = new_node

    def traverse(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next_node
        return nodes
    
    def deleteFromHead(self):
        if self.head is None:
            return None
        deleted = self.head
        self.head = self.head.next_node
        return deleted
    
    def deleteFromTail(self):
        if self.head == None:
            return None
        if self.head.next_node == None:
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
        deleted = None

        while current and current.next_node is not None:
            if current.data == key:
                deleted = current.next_node
                current.next_node = current.next_node.next_node
            
            current = current.next_node
        return deleted

    def Del(self, key):
        current = self.head
        found = False

        while current and not found:
            if current.data == key and current.data is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                current.prev_node.next_node = current.next_node
            else:
                current = current.next_node
        
        return current
    
    def search(self, key):
        current = self.head
        count = 0 
        while current:
            if current.data == key:
                return count
            current = current.next_node
            count += 1
        return None
    
    def DelIn(self, index):
        current = self.head
        count = 0 

        while current:
            if count == index:
                current.prev_node.next_node = current.next_node
                return count
            count += 1
            current = current.next_node
        return None
    
    def DelAll(self, key):
        current = self.head
        previous = None

        while current:
            if current.data == key and current is self.head:
                self.head = current.next_node
            elif current.data == key:
                previous.next_node = current.next_node
            previous = current
            current = current.next_node

        return current
    
    def toArray(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
        return nodes
    
    def addBefore(self, data, index):
        newnode = Node(data)
        position = index
        current = self.head

        if index == 0:
            self.head = newnode

        if index > 0:
            while position > 1:
                current = current.next_node
                position -= 1

            previous = current
            next = current.next_node

            previous.next_node = newnode
            newnode.next_node = next

    def Max(self):
        Max = 0 
        current = self.head
        while current:
            if current.data > Max:
                Max = current.data
        return Max
    
    def Min(self):
        Min = self.Max()
        current = self.head
        while current:
            if current.data < Min:
                Min = current.data
        return Min
    
    def Sum(self):
        current = self.head
        total = 0
        while current:
            total += current.data
        return total
    
    def avg(self):
        total_value = self.Sum
        total_node = self.count
        return total_value/total_node
    
    def sorted(self):
        current = self.head
        while current:
            if current.data < current.next_node.data:
                current = current.next_node
            else:
                return False
        return True
    
    def reverse(self):
        temp = None
        current = self.head

        while current:
            temp = current.prev_node
            current.prev_node = current.next_node
            current.next_node = temp
            current = current.prev_node

        if temp is not None:
            self.head = temp.prev_node
            

    def __repr__(self):
        nodes = []
        current = self.head
        while current:

            if current is self.head:
                nodes.append('[Head: %s]' % current.data)
            elif current.next_node is None:
                nodes.append('[Tail: %s]' % current.data)
            else:
                nodes.append('[%s]' % current.data)
            current = current.next_node

        return ' <=> '.join(nodes)
    
l = DoublyLinkedList()
l.addToHead(1)
l.addToHead(2)
l.addToHead(3)
l.addToHead(4)
l.addToHead(3)
l.addToTail(0)
print(l)
print(l.reverse())
print(l)

