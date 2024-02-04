from lib.library import Book, Library


def test_property():
    book1 = Book("C++", "Viraj", 123)
    book2 = Book("python", "anand", 2024)

    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.display_books()

    book1.borrow_book()
    print(f"{book1.title}: {book1.is_available}")
    book1.return_book()
    book1.borrow_book()
    book1.return_book()
    book1.return_book()
