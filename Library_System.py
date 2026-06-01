""" Task: Library Management System
Build a small Library Management System using multiple classes and inheritance.

Requirements

Create a base class:

class Person:
    id
    name
    email
Create two child classes using inheritance:

class Member(Person)
class Librarian(Person)
Member class
Extra attributes:

borrowed_books
Methods:

borrow_book(book)
return_book(book)
show_borrowed_books()
Librarian class
Methods:

add_book(library, book)
remove_book(library, book_id)
Book class
Attributes:

book_id
title
author
is_available
Methods:

mark_borrowed()
mark_returned()
to_dict()
Library class
Store books using a dictionary:

{
    book_id: Book(...)
}
Methods:

add_book(book)
remove_book(book_id)
find_book(book_id)
show_available_books()
show_all_books()
Expected Flow
library = Library()

librarian = Librarian(1, "Sara", "sara@gmail.com")
member = Member(2, "Ali", "ali@gmail.com")

book1 = Book(101, "Python Basics", "Mark Lutz")
book2 = Book(102, "Clean Code", "Robert Martin")

librarian.add_book(library, book1)
librarian.add_book(library, book2)

member.borrow_book(book1)
member.show_borrowed_books()

member.return_book(book1)
Rules
The same book cannot be borrowed twice.

A member cannot return a book they did not borrow.

A librarian should not remove a book that does not exist.
 """
class Person:
    def __init__(self,id,name,email):
        self.id=id
        self.name=name
        self.email=email
class Book:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.is_available=True
    def mark_borrowed(self):
         print("Your Book has been marked!")
    def mark_returned(self):
        print("Your Book has been returned!")

class Member(Person):
    def __init__(self,id,name,email):
         super().__init__(id,name,email)
         self.borrowed_books=[]

    def borrow_book(self,book):
        if book in self.borrowed_books:
            print("You have already borrowed this book!")
            return
        if not book .is_available:
            print("Sorry, this book is currently unavailable!")
            return
        book.mark_borrowed()
        book.is_available=False
        self.borrowed_books.append(book)
    def return_book(self,book):
            if book not in self.borrowed_books:
                print("You cannot return a book you did not borrow!")
                return
            book.mark_returned()
            book.is_available=True
            self.borrowed_books.remove(book)
    def show_borrowed_books(self):
                if not self.borrowed_books:
                    print("You have not borrowed any books.")
                    return
                print("Borrowed Books:")
                for book in self.borrowed_books:
                    print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")

        
class Librarian(Person):
    def __init__(self, id, name, email):
        super().__init__(id, name, email)
    def add_book(self, library, book):
        library.add_book(book)

        

    def remove_book(self, library, book_id):
        library.remove_book(book_id)
       





class Library:
    def __init__(self):
        self.book={
            101:{'book_id':12,'book_name':'Harry Potter'},
            102:{'book_id':13,'book_name':'Feminism'},
        }

    def add_book(self,book):
      self.book[book.book_id]={}
      self.book[book.book_id]['book_id'] = book.book_id
      self.book[book.book_id]['book_name'] = book.title
      self.book[book.book_id]['author'] = book.author
      self.book[book.book_id]['is_available'] = book.is_available
    
    def find_book(self,book_id):
       if book_id in self.book:
           return self.book[book_id]
       else:
           print("Book not found!")
           return None
    def remove_book(self,book_id):
       pass

           
       pass
    def show_available_books(self):
        pass

           
    def show_all_books(self):
        for book_id in self.book:
            print(f"Book ID:{book_id},Book Name:{self.book[book_id]['book_name']}")

        pass


library = Library()

librarian = Librarian(1, "Sara", "sara@gmail.com")
member = Member(2, "Ali", "ali@gmail.com")

book1 = Book(101, "Python Basics", "Mark Lutz")
book2 = Book(102, "Clean Code", "Robert Martin")

librarian.add_book(library, book1)
librarian.add_book(library, book2)

member.borrow_book(book1)
member.show_borrowed_books()

member.return_book(book1)