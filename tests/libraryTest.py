import unittest
from unittest.mock import Mock
from src.libraryRepository import LibraryRepository
from src.library import Library


class LibraryTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_repository = Mock(spec=LibraryRepository)
        self.library = Library(self.mock_repository)

    def test_borrow_book(self):
        self.mock_repository.remove_book.return_value = True
        result = self.library.borrow_book("Pan Michał")
        self.assertTrue(result)
        self.mock_repository.remove_book.assert_called_once_with("Pan Michał")

    def test_return_book(self):
        self.library.return_book("Pan Michał", "Tadeusz", 1834)
        self.mock_repository.add_book.assert_called_once_with("Pan Michał", "Tadeusz", 1834)

    def test_list_books(self):
        self.mock_repository.get_all_books.return_value = [{"title": "Pan Michał", "author": "Tadeusz", "year": 1834}]
        books = self.library.list_books()
        self.assertEqual(books, [{"title": "Pan Michał", "author": "Tadeusz", "year": 1834}])
        self.mock_repository.get_all_books.assert_called_once()


if __name__ == '__main__':
    unittest.main()
