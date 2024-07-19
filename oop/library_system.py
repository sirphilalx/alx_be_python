class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"
class EBook(Book):
    def __init__(self, title: str, author: str, filesize: int):
        super().__init__(title, author)
        self.filesize = filesize

    def __str__(self):
        return f"Ebook: {self.title} by {self.author}, File Size: {self.filesize}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library():
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise ValueError("Only instances of Book, EBook, or PrintBook can be added")

    def list_books(self):
        for book in self.books:
            print(book)
