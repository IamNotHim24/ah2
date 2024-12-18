class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def display_book(self):
        for book in self.books:
            print(book.title,book.author)

b1 = Book('tempest','shakespeare')
b2 = Book('mrechant of venice','shakespeare')
li = Library()

li.add_book(b1)
li.add_book(b2)

li.display_book()