# # # Course: Python Object-Oriented Programming
# # print("                             chapter 1: Object-Oriented Python")
# #
# #
# # # TODO: create a basic class
# # class Book:
# #     # TODO: Properties defined at the class level are shared by all instances
# #     BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
# #
# #     # TODO: create a class method
# #     @classmethod
# #     def get_book_types(cls):
# #         return cls.BOOK_TYPES
# #
# #     # TODO: double-underscore properties are hidden from other classes
# #     __booklist = None
# #
# #     # initialization function/instance method
# #     def __init__(self, title, author, published_year, page_count, price,
# #                  summary, book_type):  # self must be included by convention
# #         self.title = title  # instance attribute
# #         self.author = author  # instance attribute
# #         self.published_year = published_year  # instance attribute
# #         self.page_count = page_count  # instance attribute
# #         self.price = price  # instance attribute
# #         self.summary = summary  # instance attribute
# #         self.__secret = "this is a secret attribute "  # secret attribute
# #         # __ means that this attribute is hidden by interpreter
# #
# #         if book_type not in Book.BOOK_TYPES:
# #             raise ValueError(f'{book_type} is not a valid book type')
# #         else:
# #             self.book_type = book_type
# #
# #     # TODO: create instance methods
# #     def get_title(self):
# #         return self.title
# #
# #     def get_author(self):
# #         return self.author
# #
# #     def get_published_year(self):
# #         return self.published_year
# #
# #     def get_page_count(self):
# #         return self.page_count
# #
# #     def get_price(self):
# #         if hasattr(self, "_discount"):
# #             return self.price - (self.price * self._discount)
# #         else:
# #             return self.price
# #
# #     def get_summary(self):
# #         return self.summary
# #
# #     def get_book_type(self):
# #         return self.book_type
# #
# #     def set_discount(self, amount):
# #         # noinspection PyAttributeOutsideInit
# #         self._discount = amount  # _ means that an attribute is only intended to be used by the class
# #
# #     # TODO: create a static method
# #     @staticmethod
# #     def get_book_list():
# #         if Book.__booklist is None:
# #             Book.__booklist = []
# #         return Book.__booklist
# #
# #
# # # TODO: Create instance of book class (Book object)
# #
# # book_one = Book("The Pragmatic Programmer", "Andy Hunt", 1999, 320, 39.99, "Illustrates the best approaches and "
# #                                                                            "\nmajor pitfalls of many different "
# #                                                                            "aspects of software development.",
# #                 "HARDCOVER")
# #
# # book_two = Book("The Obstacle Is The Way", "Ryan Holiday", 2014, 224, 14.99, "a modern take on the ancient "
# #                                                                              "philosophy of Stoicism, \n"
# #                                                                              "which helps you endure the "
# #                                                                              "struggles of life with grace and "
# #                                                                              "resilience ", "PAPERBACK")
# # print()
# # print("Book One")
# # print(f'Title: {book_one.get_title()}\n'
# #       f'Author: {book_one.get_author()}\n'
# #       f'Book Type: {book_one.get_book_type()}\n'
# #       f'Year Published: {book_one.get_published_year()}\n'
# #       f'Number Of Pages: {book_one.get_page_count()}\n'
# #       f'Cost: ${book_one.get_price()}\n'
# #       f'Summary: {book_one.get_summary()}')
# # print("\nBook Two")
# # print(f'Title: {book_two.get_title()}\n'
# #       f'Author: {book_two.get_author()}\n'
# #       f'Book Type: {book_two.get_book_type()}\n'
# #       f'Year Published: {book_two.get_published_year()}\n'
# #       f'Number Of Pages: {book_two.get_page_count()}\n'
# #       f'Cost: ${book_two.get_price()}\n'
# #       f'Summary: {book_two.get_summary()}')
# #
# # print()
# #
# # print("Books Prices Before Discount:")
# # print(f'Book One: {book_one.get_price()}')
# # print(f'Book Two: {book_two.get_price()}')
# #
# # book_one.set_discount(0.25)
# # book_two.set_discount(0.25)
# #
# # print("\nBooks Prices After Discount:")
# # print(f'Book One: {book_one.get_price()}')
# # print(f'Book Two: {book_two.get_price()}')
# # # print(book_one.__secret) # generates an error
# # # print(book_one._Book__secret) #prints out this is a secret attribute
# # print("-----------------------------------------------------------------------")
# #
# #
# # class Newspaper:
# #     def __init__(self, name):
# #         self.name = name
# #
# #
# # newspaper_one = Newspaper("The Washington Post")
# # newspaper_two = Newspaper("The New York Times")
# #
# # # TODO: use type() to inspect the object type
# # print(type(book_one))
# # print(type(newspaper_one))
# # print()
# # # TODO: compare two types together
# #
# # print(type(book_one) == type(book_two))
# # print(type(book_one) == type(newspaper_one))
# # print()
# #
# # # TODO: use isinstance to compare a specific instance to a knwon type
# #
# # print(isinstance(book_one, Book))
# # print(isinstance(newspaper_one, Newspaper))
# # print(isinstance(newspaper_one, Book))  # False
# # print(isinstance(newspaper_one, object))  # True, all classes are derived from object
# # print(isinstance(book_one, object))  # True, all classes are derived from object
# # print("-----------------------------------------------------------------------")
# #
# # # TODO: Access the class attribute
# #
# # print("Book types: ", Book.get_book_types())
# #
# # # TODO: Use the static method to access a singleton object
# # library = Book.get_book_list()
# # library.append(book_one)
# # library.append(book_one)
# # print(library)
# # print("-----------------------------------------------------------------------")
# # print("-----------------------------------------------------------------------")
# # print()
# print("                             chapter 2: Inheritance and Composition")
# print("Inheritance")
#
#
# class Publication:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price
#
#
# class Periodical(Publication):  # inherits from publication
#     def __init__(self, title, price, period, publisher):
#         super().__init__(title, price)
#         self.period = period
#         self.publisher = publisher
#
#
# # class Book(Publication):  # inherited from Publication class
# #     def __init__(self, title, author, pages, price):
# #         super().__init__(title, price)
# #         self.author = author
# #         self.pages = pages
# #
# #
# # class Magazine(Periodical):
# #     def __init__(self, title, publisher, price, period):
# #         super().__init__(title,price,period,publisher)
# #
# #
# # class Newspaper(Periodical):
# #     def __init__(self, title, publisher, price, period):
# #         super().__init__(title, price, period, publisher)
# #
# #
# # b1 = Book("Brave New World", "Aldous Hyxley", 311, 29.0)
# # n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
# # m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")
# #
# # print(b1.author)
# # print(n1.publisher)
# # print(b1.price, m1.price, n1.price)
# # print("-----------------------------------------------------------------------")
#
# from abc import ABC, abstractmethod
#
# # ABC = Abstract base class
# print("Abstract Base Class")
#
#
# class GraphicShape(ABC):  # 1. Inherit from Abstract Base Class (ABC)
#     def __init__(self):
#         super().__init__()
#
#     @abstractmethod  # tells python that each subclass much override this method
#     def calcArea(self):
#         pass
#
#
# class Circle(GraphicShape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calcArea(self):
#         return 3.14 * (self.radius ** 2)
#
#
# class Square(GraphicShape):
#     def __init__(self, side):
#         self.side = side
#
#     def calcArea(self):
#         return self.side * self.side
#
#
# # g = GraphicShape() #cannot instantiate graphic shape alone since it's an abstract class
# # instead use Square and Circle which are abstracted from G
# c = Circle(10)
# print(c.calcArea())
# s = Square(12)
# print(s.calcArea())
# print("-----------------------------------------------------------------------")
# print("Multiple Inheritance")
#
#
# class A:  # Base Class
#     def __init__(self):
#         super().__init__()
#         self.foo = 'foo'
#         self.name = 'Class A'
#
#
# class B:  # Base Class
#     def __init__(self):
#         super().__init__()
#         self.bar = 'bar'
#         self.name = 'Class B'
#
#
# class C(A, B):  # Base Class C that inherits from both Class A and Class B
#     def __init__(self):
#         super().__init__()
#
#     def showProps(self):
#         print(self.foo)
#         print(self.bar)
#         print(self.name)  # Will print 'Class A' since class C was listed first in the parameter
#
#
# class_c = C()
# class_c.showProps()
# print(C.__mro__)  # Method Resolution Order
# # class C => class A => class B
# print("-----------------------------------------------------------------------")
# print("Interfaces")
#
# from abc import ABC, abstractmethod
#
#
# class JSONify(ABC):  # Can be used anywhere through the program
#     @abstractmethod
#     def toJSON(self):
#         pass
#
#
# class GraphicShape(ABC):
#     def __init__(self):
#         super().__init__()
#
#     @abstractmethod
#     def calcArea(self):
#         pass
#
#
# class Circle(GraphicShape, JSONify):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calcArea(self):
#         return 3.14 * (self.radius ** 2)
#
#     def toJSON(self):
#         return f'{{\" Circle\" : {str(self.calcArea())} }}'
#
#
# c = Circle(10)
# print(c.calcArea())
# print(c.toJSON())
# print("-----------------------------------------------------------------------")
# print("Understanding Composition")
#
#
# class Book:
#     def __init__(self, title, price, author_firstname, author_lastname):
#         self.title = title
#         self.price = price
#         self.author_firstname = author_firstname
#         self.author_lastname = author_lastname
#         self.chapters = []
#
#     def addChapter(self, name, pages):
#         self.chapters.append((name, pages))
#
#
# book1 = Book("War and Peace", 39.0, "Leo", "Tolstoy")
#
# book1.addChapter("Chapter One", 123)
# book1.addChapter("Chapter Two", 197)
# book1.addChapter("Chapter Three", 237)
# print(book1.title)
# print(book1.chapters[:])
#
# print()
# print("After Composition")
# print()
#
#
# class Book:
#     def __init__(self, title, price, author=None):
#         self.title = title
#         self.price = price
#         self.author = author
#         self.chapters = []
#
#     def addChapter(self, chapter):
#         self.chapters.append(chapter)
#
#     def getBookPageCount(self):
#         res = 0
#         for ch in self.chapters:
#             res += ch.pageCount
#         return res
#
#
# class Author:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
#
# class Chapter:
#     def __init__(self, name, pageCount):
#         self.name = name
#         self.pageCount = pageCount
#
#
# Auth = Author("Leo", "Tolstoy")
# Book1 = Book("War and Peace", 39.0, Auth)
#
# Book1.addChapter(Chapter("Chapter 1", 100))
# Book1.addChapter(Chapter("Chapter 2", 150))
# Book1.addChapter(Chapter("Chapter 3", 200))
#
# print(Book1.author)
# print(Book1.title)
# print(Book1.getBookPageCount())
# print("-----------------------------------------------------------------------")
print("                             chapter 3: Magic Object Methods")
print("Magic Methods")
