class Node:
    data = None
    next_node = None
    
    def __init__ (self, data):
        self.data = data

    def __repr__ (self):
        return "<Node data: %s>" % self.data

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def Count(self):
        current = self.head
        count = 0
        
        while current:
            count += 1
            current = current.next_node

        return count
    
    def addToHead(self, data):
         newNode = Node(data)
         newNode.next_node = self.head
         self.head = newNode

    def addToTail(self, data):
        newNode = Node(data)
        lastNode = self.head
        newNode.next_node = None

        if lastNode == None:
            return newNode
        
        while lastNode.next_node is not None:
            lastNode = lastNode.next_node

        lastNode.next_node = newNode
    
    def addAfter(self, data, index):
        new_node = Node(data)
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
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("Tail: %s" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return nodes

    def deleteFromHead(self):
        if self.head is None:
            return None
        current = self.head
        self.head = self.head.next_node
        return current
    
    def deleteFromTail(self):
        if self.head == None:
            return None
        if self.head.next_node == None:
            self.head = None
            return None
        current = self.head
        while (current.next_node.next_node):
            current = current.next_node
        deleted = current.next_node
        current.next_node = None
        return deleted
    
    def deleteAter(self, key):      
        current = self.head
        latter = None

        while current and current.next_node is not None:
            if current.data == key:
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
    
    def search(self, key):
        current = self.head 

        while current:
            if current.data == key:
                return current
            current = current.next_node
        if current is None:
            raise IndexError
        
    def DelIn(self, index):
        if self.head is None:
            return
        current = self.head
        count = 0
        
        while current.next_node and count < index:
            previous = current
            current = current.next_node
            count += 1
        
        if count < index:
            print("Index out of range.")
        elif count == 0:
            self.head = self.head.next_node
        else:
            previous.next_node = current.next_node

    #def sort(self):
            
    def Delete(self, key):
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
                

    def toArray(self):
        nodes = []
        current = self.head

        while current:
            nodes.append(current.data)

            current = current.next_node

        return nodes


    def addBefore(self, data, index):
        if index == 0:
            self.addToHead(data)
        
        if index > 0:
            new_node = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node 

            prev_node.next_node = new_node
            new_node.next_node = next_node
    
    def Max(self):
        Max = 0
        current = self.head
        while current:
            if current.data > Max:
                Max = current.data
            current = current.next_node
        return Max
    
    def Min(self):
        Min = self.Max()
        current = self.head
        while current:
            if current.data < Min:
                Min = current.data
            current = current.next_node
        return Min
    
    def Sum(self):
        Sum = 0
        current = self.head
        while current:
            Sum += current.data
            current = current.next_node
        
        return Sum
    
    def avg(self):
        value = self.Sum()
        nodes = self.Count()
        return (value/nodes)
    
    def sorted(self):
        current = self.head
        while current:
            if current.data < current.next_node.data:
                current = current.next_node
            else:
                return False
        return True
    
    def reverse(self):
        if self.head == None:
            return None
        current = self.head
        prev = None
        while current:
            next = current.next_node
            current.next_node = prev
            prev = current
            current = next
        self.head = prev


    def __repr__ (self):
        nodes = []
        current = self.head

        while current:

            if current is self.head:
                nodes.append(("[Head: %s]") % current.data)

            elif current.next_node == None:
                 nodes.append(("[Tail: %s]" % current.data))

            else:
                 nodes.append("[%s]" % current.data)

            current = current.next_node

        return '-> '.join(nodes)
    

l = SinglyLinkedList()
l.addToHead(1)
l.addToHead(12)
l.addToHead(25)
l.addToTail(16)
l.addBefore(9, 2)
l.addAfter(7, 2)
print(l)
print(l.reverse())
print(l)

