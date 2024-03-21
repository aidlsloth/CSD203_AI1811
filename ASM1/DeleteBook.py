from book import *
from linkedList import *
from database import*
from Viewbook import*
def deleteBook():
    viewBook()
    bidDelete = input("Enter bid need delete: ")
    currentNode = library.head

    if not library.isEmpty():
        if library.head.data.bid == bidDelete:
            library.head = library.head.next
            return
        else:
            while currentNode.next:
                if currentNode.next.data.bid == bidDelete:
                    currentNode.next = currentNode.next.next
                    return
                currentNode = currentNode.next

    print("Don't exist this bid")