from book import *
from linkedList import*
from database import*
def viewBook():
    print("Bid".ljust(7, " ") +"| "+"Title".ljust(15, " ") +"| "+ "Author".ljust(30, " ") + "| " + "status")
    print("-"*60)

    currentNode = library.head
    while currentNode != None:
        print(currentNode.data.bid.ljust(7, " ") +"| "+currentNode.data.title.ljust(15, " ") +"| "+ currentNode.data.author.ljust(30, " ") + "| " + currentNode.data.status)
        currentNode = currentNode.next