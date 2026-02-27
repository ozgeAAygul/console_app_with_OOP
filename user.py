from book import Book
from library import Library

class User:
  def __init__(self, name):
    self.name = name
    self.borrowed_books = []

  def borrow_book(self, library: Library, title: str): #title: str yazmamızın nedeni titleın typeını str istememiz
      # library içinden kitabı arıycaz
      for book in library.books:
         if book.title.lower() == title.lower()
         self.borrowed_books