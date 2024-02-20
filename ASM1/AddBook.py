from book import *
from Node import *

class AddBook:

    def f1(self, bid, title, author, status):
        newbook = Book(bid, title, author, status)

        if not self.head:
            self.head = newbook

        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = newbook
