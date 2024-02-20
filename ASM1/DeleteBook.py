from book import *
from Node import * 
class DeleteBook:
    def deletebook(self, key):
        current = self.head
        while current:
            current = current.next
            if current.bid == key:
                current = None