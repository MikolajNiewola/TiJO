from src.libraryRepository import LibraryRepository


class LibraryRepository2(LibraryRepository):
    def __init__(self):
        self.books = []

    def add_book(self, title: str, author: str, year: int):
        self.books.append({"title": title, "author": author, "year": year})
        return

    def remove_book(self, title: str):
        if title in self.books:
            self.books.remove(title)
            return True
        return False

    def get_all_books(self):
        return self.books
