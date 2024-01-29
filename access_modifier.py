class Book:
    def __init__(self, book_id, title, author, genre):
        self.__book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self._is_borrowed = False

    def get_book_id(self):
        return self.__book_id

    def borrow_book(self):
        if not self._is_borrowed:
            self._is_borrowed = True
            print(f"{self.title} by {self.author} has been borrowed.")
        else:
            print("Sorry, the boook is not available.")

    def return_book(self):
        if self._is_borrowed:
            self._is_borrowed = False
            print(f"{self.title} has been returned.")
        else:
            print("This book was not borrowed.")

class Library:
    def __init__(self):
        self.__books = []
        
    def add_book(self, book):
        self.__books.append(book)

    def display_books(self):
        print("Library Catalog: ")
        for book in self.__books:
            print(f"{book.title} by {book.author}.")

class Member:
    def __init__(self, member_id, name):
        self.__member_id = member_id
        self. name = name

    def borrow_book(self, book):
        if not book._is_borrowed:
            book.borrow_book()
            print(f"{self.name} has borrowed {book.title}.")
        else:
            print("Sorry, the book is not available.")

    def return_book(self, book):
        book.return_book()
        print(f"{self.name} has returned the {book.title}")

