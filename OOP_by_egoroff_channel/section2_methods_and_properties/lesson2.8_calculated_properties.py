# 2.8 Вычисляемые свойства

# class Square:
#     def __init__(self, s):
#         self.side = s
#
#     @property
#     def area(self):
#         return self.side ** 2
#
#
# b = Square(6)
# print(b.area)
#
# b.side = 10
# print(b.area)

# ==========================================================================
# Property  каждый раз считает квадрат. Что бы каждый раз не считать и
# можно применить следующее

# class Square:
#     def __init__(self, s):
#         self.side = s
#         self.__area = None
#
#     @property
#     def area(self):
#         if self.__area is None:
#             print("Вычесляем квадрат")
#             self.__area = self.side ** 2
#
#         print("Возвращаем квадрат без вычеслений")
#         return self.__area
#
# b = Square(6)
# b.area
# b.area

# =====================================================================

# Что бы начать изменять сторону квадрата

# class Square:
#     def __init__(self, s):
#         self.__side = s
#         self.__area = None
#
#     @property
#     def side(self):
#         return self.__side
#
#     @side.setter
#     def side(self, value):
#         self.__side = value
#         self.__area = None
#
#     @property
#     def area(self):
#         if self.__area is None:
#             print("Вычесляем квадрат")
#             self.__area = self.side ** 2
#
#         print("Возвращаем квадрат без вычеслений")
#         return self.__area
#
# b = Square(6)
# print(b.area)
# b.side = 3
# print(b.area)

# =====================================================================

"""Создайте класс Rectangle, у которого есть:

конструктор __init__, принимающий 2 аргумента: длину и ширину. 
свойство area, которое возвращает площадь прямоугольника;"""

# class Rectangle:
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     @property
#     def area(self):
#         return self.length * self.width
#
# r1 = Rectangle(3, 5)
# r2 = Rectangle(6, 1)
#
# print(r1.area) # 15
# print(r2.area) # 6

# ====================================================================

"""Создайте класс Date, у которого есть:

конструктор __init__, принимающий 3 аргумента: день, месяц и год. 
свойство date , которое возвращает строку определенного формата 
"<день>/<месяц>/<год>";
свойство usa_date, которое возвращает строку определенного формата
"<месяц>-<день>-<год>";"""

# one_dollar = 1
# print(f"{one_dollar:05}")

class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def date(self):
        return f'{self.day:02}/{self.month:02}/{self.year:04}'

    @property
    def usa_date(self):
        return f'{self.month:02}-{self.day:02}-{self.year:04}'



d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)

print(d1.date) # 05/10/2001
print(d1.usa_date) # 10-05-2001
print(d2.date) # 15/03/0999
print(d2.usa_date) # 03-15-0999
