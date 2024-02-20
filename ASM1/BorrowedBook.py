from book import *
from Node import *
from borrowed import * 

class BorrowedBook:
    def Borrow(self, key):
        current = self.head
        while current:
            if current.bid == key and current.status == '0':
                current.status = '1'