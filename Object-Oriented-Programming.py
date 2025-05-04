# Assignment 1: Design Your Own Class
# This example presents a Book class with attributes and methods,

class Book:
    def __init__(self, title, author, pages, genre):
        # Initialize attributes for the Book
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
    
    def read(self):
        # Simulate reading the book
        return f"You are reading '{self.title}' by {self.author}."
    
    def book_info(self):
        # Return detailed information about the book
        return f"'{self.title}' is a {self.genre} book with {self.pages} pages."

    def __str__(self):
        # String representation of the Book object
        return f"Book: {self.title} by {self.author}"