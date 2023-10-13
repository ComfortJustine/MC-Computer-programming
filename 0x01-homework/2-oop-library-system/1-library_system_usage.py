# class Book:
#     def __int__(self, title, author, isbn):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.check_out = False # Initially, the book is not checked out

#     def check_out(self):
#         if not self.checked_out:
#             self.checked_out = True
#             return True
#         else:
#             return False # Book is already checked out

#     def check_in(self):
#         if self.checked_out:
#             self.checked_out = False
#             return True
#         else:
#             return False # Book is not checked out
    
# class Member:
#     def __int__(self, name, member_id):
#             self.name = name
#             self.member_id = member_id
#             self.checked_out_books = []
#     def checked_out_book(self, book):
#         if book.check_out():
#             self.checked_out_books.append(book)
#             return True
#         else:
#             return False # Book is already checked out
    
#     def return_book(self, book):
#         if book in self.checked_out_books:
#             book.check_in()
#             self.checked_out_books.remove(book)
#             return True
#         else:
#             return False # The number didn't check out this book

# class Library:
#     def __int__(self):
#         self.books = []
#         self.members = []

#     def add_book(self, book):
#         self.books.append(book)

#     def add_member(self, member):
#         self.members.append(member)

#     def list_available_books(self):
#         return[book for book in self.books if book.checked_out]

#     def list_checked_out_books(self):
#         return [book for book in self.books if book.checked_out]

# # Example usage:

# # Create books
# book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
# book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")

# # Create members
# member1 = Member("Alice", 101)
# member2 = Member("Bob", 102)

# # Create a library
# library = Library()

# # add books to the library
# library.add_book(book1)
# library.add_book(book2)

# # Add members to the library
# library.add_member(member1)
# library.add_member(member2)

# # Member checks out a book
# member1.checked_out_book(book1)

# # List available and checked out books
# available_books = library.list_available_books()
# checked_out_books = library = library.list_checked_out_books()

# # Print the lists
# print("Available Books:")
# for book in available_books:
#     print(f"{book.title} by {book.author}")
# print("\nChecked out Books:")
# for book in checked_out_books:
#     print(f"{book.title} by {book.author}")

class Demo:
    def __init__(self, x, y) -> None:
        self.name = x
        self.age = y

x = Demo("Name", 30)