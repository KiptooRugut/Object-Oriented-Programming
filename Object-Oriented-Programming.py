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

class PrintedBook(Book):
    def __init__(self, title, author, pages, genre, cover_type, weight):
        # Call the parent constructor to initialize common attributes
        super().__init__(title, author, pages, genre)
        # Initialize additional attributes unique to PrintedBook
        self.cover_type = cover_type  # e.g., Hardcover or Paperback
        self.weight = weight  # in grams
        
    def book_info(self):
        # Override to include cover type and weight
        base_info = super().book_info()
        return f"{base_info} It is a {self.cover_type} edition weighing {self.weight} grams."