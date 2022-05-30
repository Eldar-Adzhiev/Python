# 3.8 Полиморфизм в Python

# class Rectangle:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def get_rect_area(self):
#         return self.a * self.b
#
#
# class Square:
#
#     def __init__(self, a):
#         self.a = a
#
#     def get_sq_area(self):
#         return self.a ** 2
#
# class Circle:
#
#     def __init__(self, r):
#         self.r = r
#
#     def get_circle_area(self):
#         return 3.14 * self.r**2
#
# rect1 = Rectangle(3, 4)
# rect2 = Rectangle(12, 5)
# print(rect1.get_rect_area(),
#       rect2.get_rect_area())
#
# sq1 = Square(5)
# sq2 = Square(7)
# print(sq1.get_sq_area(),
#       sq2.get_sq_area())
#
# figures = [rect1, rect2, sq1, sq2]
#
# #Что бы обойти все метеды нужно использовать условный оператор
# for figure in figures:
#     if isinstance(figure, Square):
#         print(figure.get_sq_area())
#     elif isinstance(figure, Circle):
#         print(figure.get_circle_area())
#     else:
#         print(figure.get_rect_area())

# ===============================================================================

"""Для того что бы не использовать условный оператор
нужно все методы переименовать в один. Это и будет полиморфизм.
Питон будет понимать какой метод к какому объекту относится"""

# class Rectangle:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return f'Rectangle {self.a}x{self.b}'
#
#     def get_area(self):
#         return self.a * self.b
#
#
# class Square:
#
#     def __init__(self, a):
#         self.a = a
#
#     def __str__(self):
#         return f'Square {self.a}x{self.a}'
#
#     def get_area(self):
#         return self.a ** 2
#
# class Circle:
#
#     def __init__(self, r):
#         self.r = r
#
#     def __str__(self):
#         return f'Circle raduis = {self.r}'
#
#     def get_area(self):
#         return 3.14 * self.r**2
#
# rect1 = Rectangle(3, 4)
# rect2 = Rectangle(12, 5)
#
#
# sq1 = Square(5)
# sq2 = Square(7)
#
# cirl1 = Circle(3)
# cirl2 = Circle(2)
#
#
#
# figures = [rect1, rect2, sq1, sq2, cirl1, cirl2]
#
# for figure in figures:
#     print(figure, figure.get_area())

# =========================================================================

"""Создайте класс UnitedKingdom, у которого необходимо реализовать:

статический метод capital, который печатает строку "London is the 
capital of Great Britain."
статический метод language, который печатает строку "English is the
primary language of Great Britain."
Создайте класс Spain, у которого необходимо реализовать:

статический метод capital, который печатает строку "Madrid is the 
capital of Spain."
статический метод language, который печатает строку "Spanish is the 
primary language of Spain."""

class UnitedKingdom:

    @staticmethod
    def capital():
        print("London is the capital of Great Britain.")

    @staticmethod
    def language():
        print("English is the primary language of Great Britain.")


class Spain:

    @staticmethod
    def capital():
        print("Madrid is the capital of Spain.")

    @staticmethod
    def language():
        print("Spanish is the primary language of Spain.")

obj_uk = UnitedKingdom()
obj_spa = Spain()
for country in (obj_spa, obj_uk):
    country.capital()
    country.language()