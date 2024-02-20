from book import *
from Node import * 
class ViewBooks:
    def f1(self):
        print("Bid | Title | Author | Status")
        print("-----------------------------")
        current = self.head
        while current:
            print(f'{current.bid} | {current.title} | {current.author} | {current.status}')
            current = current.next
