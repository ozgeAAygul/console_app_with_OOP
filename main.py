from book import Book
from library import Library
from user import User
from utils import save_books, load_books

if __name__ == "__main__": # bu dosya başka dosyanın içine import edilince direkt çalıştırılmasın diye. ancak direkt çalıştırmada çalışır

  lib = Library()
  load_books(lib)
  '''
  program başlar başlamaz kitapları aldık sisteme obje olarak ekledik
  '''
  
  name = input("Enter your user name: ")
  user = User(name)
  # Eğer kitapların kaydında hangi kullanıcının ödünç aldığı bilgisi varsa,
  # giriş yapan kullanıcı ile eşleştir ve kullanıcının "borrowed_books" listesini doldur.
  for book in lib.books:
    borrowed_name = getattr(book, "borrowed_by_name", None)
    if borrowed_name == user.name:
      book.borrowed_by = user
      book.available = False
      user.borrowed_books.append(book)
    # temizle geçici alanı
    if hasattr(book, "borrowed_by_name"):
      delattr(book, "borrowed_by_name")

  while True:

    print("\nMenü\n1- Kitap ekle\n2- Kitap sil\n3- Kitap ara\n4- Listele\n5- Kitap ödünç al\n6- Kitap iade et\n7- Aldığım kitapları listele\n8- Çık\n")
    choice = input("Which operation number do you want to perform? ")
    if choice == "1":
      book_title = input("Write the book title: ")
      book_author = input("Write the book author: ")
      try:
        book_year = int(input("Write the book year: "))
      except ValueError:
        print("Invalid input!")  
        continue
      new_book = Book(book_title, book_author, book_year)
      lib.add_book(new_book)

    elif choice == "2":
      remove_book_title = input("Enter the title of the book you want to delete: ")
      lib.remove_book(remove_book_title) 

    elif choice == "3":
      search_book_title = input("Enter the title of the book you wish to search for: ")
      lib.search_book(search_book_title)

    elif choice == "4":
      lib.list_books()

    elif choice == "5":
      book_for_borrowing = input("Enter the title of the book you want: ")
      user.borrow_book(lib, book_for_borrowing)

    elif choice == "6":
      book_title = input("Enter the title of the book you wish to return: ")
      user.return_book(lib, book_title)

    elif choice == "7":
      for book in user.borrowed_books:
        print("-", book)  

    elif choice == "8":
      save_books(lib) #çıkmadan eklenenleri kaydet
      print("Good bye:)")
      break

    else:  
      print("Invalid input!")  
