import json
from book import Book

def save_books(library, filename="books.json"):
  data = []

  for book in library.books:
    data.append({
      "title": book.title,
      "author": book.author,
      "year": book.year,
      "available": book.available,
      "borrowed_by": book.borrowed_by.name if book.borrowed_by else None
    })

  with open(filename, "w") as f:
    json.dump(data, f, indent=4) #bu koddaki formatı jsona çevirir öyle yazar bide indent=4 4 girdilik bi boşluk oluşturur daha estetik olur

def load_books(library, users_dict= None, filename="books.json"):
  try:
    with open(filename, "r") as f:
      data = json.load(f) #dosyadakileri python formatına çavirecek

    for item in data:
      book = Book(item["title"], item["author"], item["year"])
      # Güvenli şekilde eksik alanları destekle
      book.available = item.get("available", True)
      borrowed_by_name = item.get("borrowed_by")
      # her durumda kaydedilmiş isim bilgisini sakla; kullanıcı dict verilirse nesneye bağla
      book.borrowed_by_name = borrowed_by_name
      if borrowed_by_name and users_dict:
        book.borrowed_by = users_dict.get(borrowed_by_name)
        if book.borrowed_by:
          book.borrowed_by.borrowed_books.append(book)
      library.add_book(book)
  except FileNotFoundError:
    pass #eğer dosya bulunamazsa sessizce devam et
