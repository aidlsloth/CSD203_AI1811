from book import *
from Node import *
class mylist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head == None
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
        print("")

    def clear(self):
        self.head = None
    