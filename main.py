from book import Book
from library import Library

if __name__ == "__main__": # bu dosya başka dosyanın içine import edilince direkt çalıştırılmasın diye. ancak direkt çalıştırmada çalışır
  book1 = Book("Ezilenler", "Dostoyevski", 1861)
  book2 = Book("Baba'ya Mektup", "Kafka", 1919)

  lib = Library()

  lib.add_book(book1)
  lib.add_book(book2)

  lib.list_books()  
