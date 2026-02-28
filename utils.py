import json
from book import Book

def save_books(library, filename="books.json"):
  data = []

  for book in library.books:
    data.append({
      "title": book.title,
      "author": book.author,
      "year": book.year
    })

  with open(filename, "w") as f:
    json.dump(data, f, indent=4) #bu koddaki formatı jsona çevirir öyle yazar bide indent=4 4 girdilik bi boşluk oluşturur daha estetik olur

def load_books(library, filename="books.json"):
  try:
    with open(filename, "r") as f:
      data = json.load(f) #dosyadakileri python formatına çavirecek

    for item in data:
      book = Book(item["title"], item["author"], item["year"])
      library.add_book(book)
      '''
      Burada yapılan dosyadaki kitapları alıp kitap objesine çevirmek
      '''
  except FileNotFoundError:
    pass #eğer dosya bulunamazsa sessizce devam et
