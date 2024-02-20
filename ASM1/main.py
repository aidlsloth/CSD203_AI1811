from mylist import *
from book import * 
from AddBook import *
from DeleteBook import *
from ReturnBook import *
from ViewBooks import *
from BorrowedBook import * 

print("1. Add Book")
print("2. Delete Book")
print("3. Borrow Book")
print("4. Return Book")
print("5. View Book")
choice = int(input("Selection 1 -> 5"))
print("OUTPUT")

if choice == 1:
    newbook = input("Book's info")
    AddBook(newbook)

elif choice == 2:
    DeleteBook()

elif choice == 3:
    BorrowedBook.Borrow()

elif choice == 4:
    ReturnBook()

elif choice == 5:
    ViewBooks()
