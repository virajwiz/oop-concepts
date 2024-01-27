# book class
# attributes:title, author, ISBN, availability
# library class
# 

class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__availability = True

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    @property
    def is_available(self):
        return self.__availability

    def borrow_book(self):
        if self.__availability == False:
            print(f"{self.title} is not available for borrowing.")
        else:
            print(f"{self.title} is borrowed.")
            self.__availability = False

    def return_book(self):
        if self.__availability == False:
            print(f"{self.title} is returned.")
            self.__availability = True
        else:
            print(f"{self.title} is already available.")


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def display_books(self):
        print("Books in library: ")
        for book in self.__books:
            print(f"-  {book.title} by {book.author}.")
            
