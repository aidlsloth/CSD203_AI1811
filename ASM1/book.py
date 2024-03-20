class Book:
    def __init__(self, bid =  None, title = None, author = None, status = None):
        self.bid = bid
        self.title = title
        self.author = author
        self.status = status

    def __repr__(self):
        return f'{self.bid} | {self.title} | {self.author} | {self.status}'

