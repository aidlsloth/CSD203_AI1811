class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return "<Node Data: %s>" % self.data

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, data):
        new_node = Node(data)
        current = self.head 
        new_node.next_node = self.head

        if self.head is not None:
            while(current.next_node != self.head):
                current = current.next_node
            current.next_node = new_node
        
        else:
            new_node.next_node = new_node
            self.head = new_node

    def addToTail(self, data):
        new_node = Node(data)
        current = self.head
        new_node.next_node = self.head

        if self.head is not None:
            while current.next_node != self.head:
                current = current.next_node
            current.next_node = new_node
        
        else:
            new_node.next_node = new_node
            self.head = new_node

    '''def addAfter(self, data, key):
        new_node = Node(data)
        current = self.head 
        if self.head is not None:
            while current.next_node != self.head:
                if current.data == key:
                    current.next_node = new_node
                    new_node = current.next_node.next_node
                current = current.next_node
        else:
            new_node.next_node = new_node
            self.head = new_node'''
    
    def traverse(self):
        nodes = []
        current = self.head
        if self.head is not None:
            while True:
                nodes.append("[%s]" % current.data)
                current = current.next_node
                if (current == self.head):
                    return ' - '.join(nodes)
                
    def deleteFromHead(self):
        current = self.head
        temp = self.head.next_node

        while current.next_node != self.head:
            current = current.next_node

        deleted = current.next_node
        current.next_node = temp
        self.head = current.next_node

        return deleted
    
    def deleteFromTail(self):
        current = self.head
        
        while current.next_node.next_node != self.head:
            current = current.next_node
        deleted = current.next_node
        current.next_node = self.head

        return deleted

    def deleteAfter(self, key):
        current = self.head
        while current.next_node != self.head:
            if current.data == key:
                deleted = current.next_node
                current.next_node = current.next_node.next_node
            current = current.next_node
        
        return deleted
    
    def Del(self, key):
        current = self.head 
        previous = None
        found = False
        while current.next_node != self.head:
            if current.data == key and current is self.head:
                found = True
                self.head= current.next_node

            elif current.data == key:
                found = True
                prev.next_node = current.next_node

            else:
                prev = current
                current = current.next_node

    def search(self, key):
        current = self.head
        count = 0

        while current.next_node != self.head:
            if current.data == key: 
                return count
            count += 1
            current = current.next_node
        return None
    
    def count(self):
        current = self.head
        count = 0 

        while current.next_node != self.head:
            count += 1
            current = current.next_node

        return count
    
    def DelIn(self, index):
        if self.head is None:
            return
        current = self.head
        count = 0
        
        while current.next_node != self.head:
            previous = current
            current = current.next_node
            count += 1
        
        if count < index:
            print("Index out of range.")
        elif count == 0:
            self.head = self.head.next_node
        else:
            previous.next_node = current.next_node

    def DelAll(self, key):
        current = self.head
        previous = None

        while current.next_node != self.head:
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
        while current.next_node != self.head:
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
        while current.next_node != self.head:
            if current.data > Max:
                Max = current.data
        return Max
    
    def Min(self):
        Min = self.Max()
        current = self.head
        while current.next_node != self.head:
            if current.data < Min:
                Min = current.data
        return Min
    
    def Sum(self):
        current = self.head
        total = 0
        while current.next_node != self.head:
            total += current.data
        return total
    
    def avg(self):
        total_value = self.Sum
        total_node = self.count
        return total_value/total_node
    
    def sorted(self):
        current = self.head
        while current.next_node != self.head:
            if current.data < current.next_node.data:
                current = current.next_node
            else:
                return False
        return True   



l = CircularLinkedList()
l.addToHead(1)
l.addToHead(2)
l.addToHead(3)
l.addToTail(4)
#l.addAfter(5, 3)
print(l.traverse())
print(l.deleteFromTail())
print(l.traverse())
            
    
