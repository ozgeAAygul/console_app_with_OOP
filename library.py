class Library:
  def __init__(self):
    self.books = []

  def add_book(self, book):
    self.books.append(book)

  def list_books(self):
    if not self.books:
      print("Library is empty.")
      return
    
    for item in self.books:
      print(f"- {item}")

  def search_book(self, title):
    for book in self.books:
      if book.title.lower() == title.lower(): #burada book.title var ya bu Book clasında yazdığımız self.title a refer ediyor
        print(book)
        return
    print(f"- {title} is not in library!")   
  
  def remove_book(self, title):
    for book in self.books:
      if book.title.lower() == title.lower():
        self.books.remove(book)
        return
    print(f"- {title} is not in library!") 
