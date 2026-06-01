""" Question: Merge Dictionaries
Given:

sales_jan = {"Laptop": 5, "Mouse": 10}
sales_feb = {"Laptop": 3, "Keyboard": 7}
Merge both dictionaries.

If a product exists in both dictionaries, add the quantities.

Expected:

{
    "Laptop": 8,
    "Mouse": 10,
    "Keyboard": 7
}
Question: Nested Dictionary Search
Given:

employees = {
    101: {"name": "Ali", "salary": 50000},
    102: {"name": "Ammara", "salary": 70000},
    103: {"name": "Ahmed", "salary": 60000}
}
Write a function:

find_employee(employee_id)
that returns employee details if found, otherwise returns "Employee not found".

Validation Function
Write a function:

is_valid_email(email)
Requirements:

Contains "@" Contains "." Returns True/False

Question: Student Class
Create a class:

Student
Attributes:

name
roll_no
marks
Methods:

display_info()
is_passed()
Passing marks = 40.

Task: Library Management System
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

Only available books should appear in show_available_books(). """
""" Given:

sales_jan = {"Laptop": 5, "Mouse": 10}
sales_feb = {"Laptop": 3, "Keyboard": 7}
Merge both dictionaries.

If a product exists in both dictionaries, add the quantities.

Expected:

{
    "Laptop": 8,
    "Mouse": 10,
    "Keyboard": 7
} """
merged={}
sales_jan = {"Laptop": 5, "Mouse": 10}
sales_feb = {"Laptop": 3, "Keyboard": 7}
for key in sales_jan:
     merged[key]=sales_jan[key]
for key in sales_feb:
     if key in merged:
          merged[key]=merged[key]+sales_feb[key]
     else:
          merged[key]=sales_feb[key]
print(merged)
""" Question: Nested Dictionary Search
Given:

employees = {
    101: {"name": "Ali", "salary": 50000},
    102: {"name": "Ammara", "salary": 70000},
    103: {"name": "Ahmed", "salary": 60000}
}
Write a function:

find_employee(employee_id)
that returns employee details if found, otherwise returns "Employee not found".

Validation Function
Write a function:

is_valid_email(email)
Requirements:

Contains "@" Contains "." Returns True/False """

employees = {
    101: {"name": "Ali", "salary": 50000},
    102: {"name": "Ammara", "salary": 70000},
    103: {"name": "Ahmed", "salary": 60000}
}
def find_employee(employee_id):
    if employees[employee_id] in employees:
        print(employees[employee_id])
    else:
        print("Employees Not Found")
def  is_validate_email(email):
    if '@' in email  and '.' in email:
        return True
    else:
       return False
""" Question: Student Class
Create a class:

Student
Attributes:

name
roll_no
marks
Methods:


display_info()
is_passed()
Passing marks = 40. """
class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def is_passed(self):
        if self.marks>=40:
            print("You are passed!")
        else:
            print("You will not passed")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

s1=Student('laiba',12,90)
s1.display_info()
s1.is_passed()
