class book:
    bid = 0
    def __init__(self, title , author , status ):
        book.bid += 1
        self.bid = "B0"+str(book.bid)
        self.title = title
        self.author = author
        self.status = status
