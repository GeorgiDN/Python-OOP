class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def show_current_page(self):
        return f"The book: {self.title} is opened on page {self.page}"

    def __repr__(self):
        return f"The book: {self.title} was written by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            return f"The book: {book.title} is added successfully!"
        return f"The book: {book.title} is already added!"

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return f"The book: {book.title} is removed successfully!"
        return f"The book: {book.title} is not in the collection, so you can't remove it!"

    def show_all_books(self):
        if self.books:
            if len(self.books) == 1:
                return f"There is only one book in the library: {', '.join([b.title for b in self.books])}."
            elif len(self.books) > 1:
                return f"The books in the library are: {', '.join([b.title for b in self.books])}."
        return "There is no books in the library!"

    def find_book(self, book):
        searched_book = next((b.title for b in self.books if b.title == book.title), None)
        if searched_book is not None:
            return f"The book {searched_book} is found!"
        return f"The book: {book.title} is not found!"

    # def find_book(self, book):
    #     try:
    #         searched_book = next(b for b in self.books if b == book.title)
    #         return f"The book {searched_book} is found!"
    #     except StopIteration:
    #         return f"The book: {book.title} is not found!"


book = Book("Boxing", "Mike Tyson")
book2 = Book("The Giant", "Ivanov")
book3 = Book("Fighter", "Mirchev")
print(book)
book.turn_page(10)
print(book.show_current_page())

library = Library()
print(library.add_book(book))
print(library.add_book(book2))
print(library.add_book(book2))
print(library.show_all_books())
print(library.find_book(book2))
print(library.find_book(book3))
print(library.remove_book(book2))
print(library.remove_book(book3))
print(library.show_all_books())
print(library.remove_book(book))
print(library.show_all_books())


#Refactor the provided code, so there is a separate class called Library, which contains books and has a method called
# find_book(title) that returns the book with the given title.
# Remove the unnecessary code from the Book class.


# Code for edit
# class Book:
#     def __init__(self, title, author, location):
#         self.title = title
#         self.author = author
#         self.location = location
#         self.page = 0
#
#     def turn_page(self, page):
#         self.page = page




