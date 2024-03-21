from book import *
from linkedList import *
from database import*
def addBook():
    title = input("Enter title of book: ")
    author = input("Enter author of book: ")
    status = input("Enter status of book: ")
    bookAdd = book(title, author, status)

    if library.isEmpty():
        library.head = node(bookAdd)
    else:
        currentNode = library.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = node(bookAdd)  
