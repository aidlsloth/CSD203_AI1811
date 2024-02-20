from book import *
from Node import *

class ReturnBook:
    def return_book(self, key):
        current = self.head
        while current:
            if current.bid == key:
                if current.status == '1':
                    current.status = '0'
                    print(f'{current.title} is returned successfully')
                else:
                    print(f'{current.title} is already available')
            else:
                print(f'{current.title} is not found in the library')