class Book:
    def __int__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.check_out = False # Initially, the book is not checked out

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return True
        else:
            return False # Book is already checked out

    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            return True
        else:
            return False # Book is not checked out
    
class Member:
    def __int__(self, name, member_id):
            self.name = name
            self.member_id = member_id
            self.checked_out_books = []
    def checked_out_book(self, book):
        if book.check_out():
            self.checked_out_books.append(book)
            return True
        else:
            return False # Book is already checked out
    
    def return_book(self, book):
        if book in self.checked_out_books:
            book.check_in()
            self.checked_out_books.remove(book)
            return True
        else:
            return False # The number didn't check out this book

class Library:
    def __int__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def list_available_books(self):
        return[book for book in self.books if book.checked_out]

    def list_checked_out_books(self):
        return [book for book in self.books if book.checked_out]
        



