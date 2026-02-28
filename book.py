class Book:
  def __init__(self, title, author, year):
    self.title = title
    self.author = author
    self.year = year
    self.available = True #kitap kütüphanedeyken true'dur
    self.borrowed_by = None 
  def __str__(self):
    status = "available" if self.available else f"Borrewed by {self.borrowed_by.name}"
    return f"{self.title} - {self.author} ({self.year}) [{status}]"
  def __repr__(self):
    return f"Book('{self.title}', '{self.author}', {self.year})" # bu geliştiriciler için 
  
