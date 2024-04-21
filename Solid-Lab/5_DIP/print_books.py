class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book):
        return book.content


class Printer:
    def get_book(self, book: Book, formatter:Formatter):
        formatted_book = formatter.format(book)
        return formatted_book


book = Book("Interesting book")
formatter = Formatter()
printer = Printer()

print(printer.get_book(book, formatter))



# Code for edit
#class Book:
#     def __init__(self, content: str):
#         self.content = content
#
#
# class Formatter:
#     def format(self, book: Book) -> str:
#         return book.content
#
#
# class Printer:
#     def get_book(self, book: Book):
#         formatter = Formatter()
#         formatted_book = formatter.format(book)
#         return formatted_book


# Condition
# We want to print books, but before printing the book,
# we should format it. To accomplish this, we have a class
# Printer that can print books and a class Formatter which is used by the Printer.
# Refactor the provided code that breaks the DIP because both the Printer and Formatter depend on concretions,
# not abstractions, by creating abstractions and injecting them wherever needed.

