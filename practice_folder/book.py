class Book:
    total_books = 0

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        Book.total_books += 1

    @classmethod
    def display_total_books(cls):
        return Book.total_books
    


book1 = Book('Animal Farm', 'George Orwell', 50)
book2 = Book('Romeo and Juliet', 'William Shakespeare', 150)


print(Book.display_total_books())