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
        if book.available:
          book.available = False #artık kütüpte değil
          book.borrowed_by = self # bu kullanıcı aldı
          self.borrowed_books.append(book)
          print(f"{self.name} borrowed '{book.title}'")
          return
    print(f"'{title}' is not available in library")

  def return_book(self, library: Library, title: str):
    for book in self.borrowed_books:
      if book.title.lower() == title.lower():
        book.available = True
        book.borrowed_by = None
        self.borrowed_books.remove(book)
        print(f"{self.name} returned '{book.title}'")
        return
    print(f"{self.name} does not have '{title}'")