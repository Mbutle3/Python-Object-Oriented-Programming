# # Course: Python Object-Oriented Programming
# print("                             chapter 1: Object-Oriented Python")
#
#
# # TODO: create a basic class
# class Book:
#     # TODO: Properties defined at the class level are shared by all instances
#     BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
#
#     # TODO: create a class method
#     @classmethod
#     def get_book_types(cls):
#         return cls.BOOK_TYPES
#
#     # TODO: double-underscore properties are hidden from other classes
#     __booklist = None
#
#     # initialization function/instance method
#     def __init__(self, title, author, published_year, page_count, price,
#                  summary, book_type):  # self must be included by convention
#         self.title = title  # instance attribute
#         self.author = author  # instance attribute
#         self.published_year = published_year  # instance attribute
#         self.page_count = page_count  # instance attribute
#         self.price = price  # instance attribute
#         self.summary = summary  # instance attribute
#         self.__secret = "this is a secret attribute "  # secret attribute
#         # __ means that this attribute is hidden by interpreter
#
#         if book_type not in Book.BOOK_TYPES:
#             raise ValueError(f'{book_type} is not a valid book type')
#         else:
#             self.book_type = book_type
#
#     # TODO: create instance methods
#     def get_title(self):
#         return self.title
#
#     def get_author(self):
#         return self.author
#
#     def get_published_year(self):
#         return self.published_year
#
#     def get_page_count(self):
#         return self.page_count
#
#     def get_price(self):
#         if hasattr(self, "_discount"):
#             return self.price - (self.price * self._discount)
#         else:
#             return self.price
#
#     def get_summary(self):
#         return self.summary
#
#     def get_book_type(self):
#         return self.book_type
#
#     def set_discount(self, amount):
#         # noinspection PyAttributeOutsideInit
#         self._discount = amount  # _ means that an attribute is only intended to be used by the class
#
#     # TODO: create a static method
#     @staticmethod
#     def get_book_list():
#         if Book.__booklist is None:
#             Book.__booklist = []
#         return Book.__booklist
#
#
# # TODO: Create instance of book class (Book object)
#
# book_one = Book("The Pragmatic Programmer", "Andy Hunt", 1999, 320, 39.99, "Illustrates the best approaches and "
#                                                                            "\nmajor pitfalls of many different "
#                                                                            "aspects of software development.",
#                 "HARDCOVER")
#
# book_two = Book("The Obstacle Is The Way", "Ryan Holiday", 2014, 224, 14.99, "a modern take on the ancient "
#                                                                              "philosophy of Stoicism, \n"
#                                                                              "which helps you endure the "
#                                                                              "struggles of life with grace and "
#                                                                              "resilience ", "PAPERBACK")
# print()
# print("Book One")
# print(f'Title: {book_one.get_title()}\n'
#       f'Author: {book_one.get_author()}\n'
#       f'Book Type: {book_one.get_book_type()}\n'
#       f'Year Published: {book_one.get_published_year()}\n'
#       f'Number Of Pages: {book_one.get_page_count()}\n'
#       f'Cost: ${book_one.get_price()}\n'
#       f'Summary: {book_one.get_summary()}')
# print("\nBook Two")
# print(f'Title: {book_two.get_title()}\n'
#       f'Author: {book_two.get_author()}\n'
#       f'Book Type: {book_two.get_book_type()}\n'
#       f'Year Published: {book_two.get_published_year()}\n'
#       f'Number Of Pages: {book_two.get_page_count()}\n'
#       f'Cost: ${book_two.get_price()}\n'
#       f'Summary: {book_two.get_summary()}')
#
# print()
#
# print("Books Prices Before Discount:")
# print(f'Book One: {book_one.get_price()}')
# print(f'Book Two: {book_two.get_price()}')
#
# book_one.set_discount(0.25)
# book_two.set_discount(0.25)
#
# print("\nBooks Prices After Discount:")
# print(f'Book One: {book_one.get_price()}')
# print(f'Book Two: {book_two.get_price()}')
# # print(book_one.__secret) # generates an error
# # print(book_one._Book__secret) #prints out this is a secret attribute
# print("-----------------------------------------------------------------------")
#
#
# class Newspaper:
#     def __init__(self, name):
#         self.name = name
#
#
# newspaper_one = Newspaper("The Washington Post")
# newspaper_two = Newspaper("The New York Times")
#
# # TODO: use type() to inspect the object type
# print(type(book_one))
# print(type(newspaper_one))
# print()
# # TODO: compare two types together
#
# print(type(book_one) == type(book_two))
# print(type(book_one) == type(newspaper_one))
# print()
#
# # TODO: use isinstance to compare a specific instance to a knwon type
#
# print(isinstance(book_one, Book))
# print(isinstance(newspaper_one, Newspaper))
# print(isinstance(newspaper_one, Book))  # False
# print(isinstance(newspaper_one, object))  # True, all classes are derived from object
# print(isinstance(book_one, object))  # True, all classes are derived from object
# print("-----------------------------------------------------------------------")
#
# # TODO: Access the class attribute
#
# print("Book types: ", Book.get_book_types())
#
# # TODO: Use the static method to access a singleton object
# library = Book.get_book_list()
# library.append(book_one)
# library.append(book_one)
# print(library)
# print("-----------------------------------------------------------------------")
# print("-----------------------------------------------------------------------")
# print()
print("                             chapter 2: Inheritance and Composition")
print()
