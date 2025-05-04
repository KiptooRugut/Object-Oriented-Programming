# Assignment 1: Design Your Own Class
# This example presents a Book class with attributes and methods,

class Book:
    def __init__(self, title, author, pages, genre):
        # Initialize attributes for the Book
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre