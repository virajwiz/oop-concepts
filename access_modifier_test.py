from access_modifier import Book, Library, Member

book1 = Book(1, "Abc", "J.D. Salinger", "Fiction")
book2 = Book(2, "Xyz", "Harper Lee", "Classic")

library = Library()
library.add_book(book1)
library.add_book(book2)

member = Member(1, "Viraj")

library.display_books()
member.borrow_book(book1)
member.return_book(book1)
member.borrow_book(book2)


library.display_books()