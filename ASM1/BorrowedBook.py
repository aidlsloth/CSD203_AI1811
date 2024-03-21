from book import *
from borrowerBooks import*
from linkedList import *
from database import*
from Viewbook import*

def borrowedBook():
    viewBook()
    borrower = input("Enter the name of borrower: ")
    bidBorrow = input("Enter book id: ")

    currentNode = library.head
    while currentNode:
        if currentNode.data.bid == bidBorrow:
            runBorrow = True
            break
        currentNode = currentNode.next
    
    if runBorrow:
        if currentNode.data.status == "0":
            print("users can lend")
            dbBorrowed.addToHead(node(borrowerBooks(bidBorrow, borrower)))
            currentNode.data.status = "1"
        else:
            print("Book isn't available")
    else:
        print("Couldn't find book in library")