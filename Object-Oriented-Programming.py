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

    def carry(self):
        # New method specific to printed books
        return f"You carry the {self.cover_type} book titled '{self.title}'. It's {self.weight} grams."
    
# Example usage
if __name__ == "__main__":
    my_book = Book("1994", "Mike Kiptoo", 327, "After Series")
    print(my_book)
    print(my_book.read())
    print(my_book.book_info())

    print()  # blank line

    my_printed_book = PrintedBook("Blackswan Theory", "Blackbriar Mik", 287, "Fiction", "Hardcover", 500)
    print(my_printed_book)
    print(my_printed_book.read())  # inherited method
    print(my_printed_book.book_info())  # overridden method
    print(my_printed_book.carry())  # subclass-specific method



# Activity 2: Polymorphism Challenge
# Defines different Vehicle classes each implementing move() differently to demonstrate polymorphism

class Vehicle:
    def move(self):
        # Abstract method: should be overridden in subclasses
        raise NotImplementedError("Subclasses must implement the move method.")
    
class Car(Vehicle):
    def move(self):
        # Car moves by driving
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        # Plane moves by flying
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        # Boat moves by sailing
        return "Sailing ⛴️"

class Bicycle(Vehicle):
    def move(self):
        # Bicycle moves by pedaling
        return "Pedaling 🚲"
    
# Example usage
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat(), Bicycle()]

    for vehicle in vehicles:
        # Call move() polymorphically
        print(vehicle.move())