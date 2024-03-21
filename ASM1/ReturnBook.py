from book import *
from borrowerBooks import*
from linkedList import *
from database import*
from Viewbook import*

def deletedbBorrowed(bidDelete, borrowerDelete):
    if not dbBorrowed.isEmpty():
        if dbBorrowed.head.data.bid == bidDelete and dbBorrowed.head.data.borrower == borrowerDelete:
            dbBorrowed.head = dbBorrowed.head.next
            return
        else:
            currentNode = dbBorrowed.head
            while currentNode.next:
                if currentNode.next.data.bid == bidDelete and currentNode.next.data.borrower == borrowerDelete:
                    currentNode.next = currentNode.next.next
                    return
                currentNode = currentNode.next

    print("Can't delete in database Borrowed")

def returnBook():
    viewBook()
    bidReturn = input("Enter book id: ")
    returner = input("Enter name of returner: ")

    currentNode = dbBorrowed.head
    while currentNode:
        if currentNode.data.bid == bidReturn and currentNode.data.borrower == returner:
            currentNode1 = library.head
            while currentNode1:
                if currentNode1.data.bid == bidReturn:
                    currentNode1.data.status = "0"
                    print("Successfully")
                    deletedbBorrowed(bidReturn, returner)
                    return
                currentNode1 = currentNode1.next

        currentNode = currentNode.next
    print("Can't find data borrow")
