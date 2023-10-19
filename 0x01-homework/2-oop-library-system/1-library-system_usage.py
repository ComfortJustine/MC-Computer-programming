class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

    def checked_out(self):
        if not self.checked_out:
            self.checked_out = True

            print(f"The book '{self.title}' by '{self.author}' has been checked out.")
        else:
            print(f"The book '{self.title}' is already checked out.")

    def check_in(self):
        if self.checked_out:
            self.checked_out = False

            print(f"The book '{self.title}' by '{self.title}' has been checked in.")
        else:
            print(f"The book '{self.title}' is already checked in.")

class Member:
    def __init__(self, name):
        self.name = name
        self.books_books_checked_out = []

    def checked_out_book(self, book):
        if book.checked_out:
            print(f"The book '{book.title}' is already checked out.")
        else:
            book.checked_out
            self.books_books_checked_out.append(book) 
    
    def check_in_book(self, book):
        if book in self.books_books_checked_out:
            book.check_in()
            self.books_books_checked_out.remove(book)
        else:
            print(f"The book '{book.title}' is not checked out by this member.")

# Create book instances
book1 = Book("Harry Potter and the Sorcerers's Stone", "J.K.Rowling")
book2 = Book("To kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

# Create member instance
member1 = Member("John Doe")

# Demonstrate checking out and checking in books
member1.checked_out_book(book1)
member1.check_out_book(book2)
member1.check_out_book(book3)

member1.check_in_book(book2)
member1.check_in_book(book3)
member1.check_in_book(book1)
        

