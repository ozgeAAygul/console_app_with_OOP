from book import Book
from library import Library

class User:
  def __init__(self, name):
    self.name = name
    self.borrowed_books = []

  def borrow_book(self, library: Library, title: str): #title: str yazmamızın nedeni titleın typeını str istememiz
    # library içinden kitabı arıycaz
    for book in library.books:
      if book.title.lower() == title.lower():
        self.borrowed_books.append(book)
        library.books.remove(book) #bak burası önemli başka clasın içinde değişiklik yaptık
        print(f"{self.name} borrowed '{book.title}'")
        return
    print(f"'{title}' is not available in library")

  def return_book(self, library: Library, title: str):
    for book in self.borrowed_books:
      if book.title.lower() == title.lower():
        self.borrowed_books.remove(book)
        library.books.append(book)
        print(f"{self.name} returned '{book.title}'")
        return
    print(f"{self.name} does not have '{title}'")