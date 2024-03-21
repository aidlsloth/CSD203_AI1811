from AddBook import*
from book import *
from borrowerBooks import*
from database import *
from linkedList import *
from Viewbook import *
from DeleteBook import *
from BorrowedBook import*
from ReturnBook import *

run = True
while run:
    print("1. Add books to the database")
    print("2. Displays the list of books in the library")
    print("3. Delete a book from the library")
    print("4. Lend a book from library")
    print("5. Return a book to the library")
    print("6. Exit")
    print()
    choose = input("Enter a number from 1->6: ")

    if choose =="1":
        addBook()
    elif choose == "2":
        viewBook()
    elif choose == "3":
        deleteBook()
    elif choose == "4":
        borrowedBook()
    elif choose == "5":
        returnBook()
    elif choose == "6":
        run = False
    else:
        print("Wrong")
    print()
