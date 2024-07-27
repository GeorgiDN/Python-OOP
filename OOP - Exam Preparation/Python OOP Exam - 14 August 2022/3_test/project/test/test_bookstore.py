from unittest import TestCase, main

from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self):
        self.bookstore = Bookstore(10)

    def test_init(self):
        self.assertIsInstance(self.bookstore, Bookstore)
        self.assertEqual(self.bookstore.books_limit, 10)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})
        self.assertEqual(self.bookstore._Bookstore__total_sold_books, 0)

    def test_books_limit_with_negative_value_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -1
        message = f"Books limit of -1 is not valid"
        self.assertEqual(message, str(ve.exception))

    def test_books_limit_with_zero_value_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
        message = f"Books limit of 0 is not valid"
        self.assertEqual(message, str(ve.exception))

    def test_proper_boo_limit(self):
        self.bookstore.books_limit = 10
        self.assertEqual(self.bookstore.books_limit, 10)

    def test_len_method_with_not_added_books(self):
        result = self.bookstore.__len__()
        self.assertEqual(result, 0)

    def test_receive_book_with_not_books_added(self):
        result = self.bookstore.receive_book("book1", 2)
        message = "2 copies of book1 are available in the bookstore."
        self.assertEqual(result, message)
        self.assertEqual(
            self.bookstore.availability_in_store_by_book_titles, {"book1": 2})

    def test_receive_book_with_add_more_books(self):
        self.bookstore.receive_book("book1", 2)
        self.bookstore.receive_book("book2", 3)
        result = self.bookstore.receive_book("book1", 2)
        message = "4 copies of book1 are available in the bookstore."
        self.assertEqual(result, message)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles,
                         {"book1": 4, "book2": 3})

    def test_receive_book_with_count_over_limit(self):
        self.bookstore.receive_book("book1", 2)
        self.bookstore.receive_book("book2", 3)
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("book1", 6)
        message = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(message, str(ex.exception))
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles,
                         {"book1": 2, "book2": 3})

    def test_receive_book_with_count_over_limit_not_added_books(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("book1", 11)
        message = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(message, str(ex.exception))
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})

    def test_len_method_with_added_books(self):
        self.bookstore.receive_book("book1", 2)
        self.bookstore.receive_book("book2", 3)
        result = self.bookstore.__len__()
        self.assertEqual(result, 5)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles,
                         {"book1": 2, "book2": 3})

    def test_sell_book_with_not_added_books(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("book1", 2)
        message = "Book book1 doesn't exist!"
        self.assertEqual(message, str(ex.exception))

    def test_sell_book_with_required_copies_more_than_in_stock(self):
        self.bookstore.receive_book("book1", 2)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("book1", 10)
        message = "book1 has not enough copies to sell. Left: 2"
        self.assertEqual(message, str(ex.exception))

    def test_sell_book_with_required_copies_more_than_in_stock_with_added_more_books(self):
        self.bookstore.receive_book("book1", 5)
        self.bookstore.receive_book("book1", 2)
        self.bookstore.receive_book("book2", 2)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("book1", 10)
        message = "book1 has not enough copies to sell. Left: 7"
        self.assertEqual(message, str(ex.exception))

    def test_sell_book_with_one_books_added(self):
        self.bookstore.receive_book("book1", 5)
        result = self.bookstore.sell_book("book1", 5)
        message = "Sold 5 copies of book1"
        self.assertEqual(result, message)
        self.assertEqual(
            self.bookstore.availability_in_store_by_book_titles, {"book1": 0})
        self.assertEqual(self.bookstore._Bookstore__total_sold_books, 5)

    def test_sell_book_with_more_books_added(self):
        self.bookstore.receive_book("book1", 5)
        self.bookstore.receive_book("book2", 3)
        result = self.bookstore.sell_book("book1", 2)
        message = "Sold 2 copies of book1"
        self.assertEqual(result, message)
        self.assertEqual(
            self.bookstore.availability_in_store_by_book_titles, {"book1": 3, "book2": 3})
        self.assertEqual(self.bookstore._Bookstore__total_sold_books, 2)

    def test_str_method(self):
        self.bookstore.receive_book("book1", 4)
        self.bookstore.receive_book("book2", 4)
        self.bookstore.sell_book("book1", 2)
        self.bookstore.sell_book("book2", 2)
        action = self.bookstore.__str__()

        result = "Total sold books: 4\n"
        result += "Current availability: 4\n"
        result += " - book1: 2 copies\n"
        result += " - book2: 2 copies"

        self.assertEqual(action, result)


if __name__ == '__main__':
    main()
