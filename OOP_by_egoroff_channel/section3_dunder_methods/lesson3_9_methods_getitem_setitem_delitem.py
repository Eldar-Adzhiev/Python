# 3.9 Методы __getitem__ , __setitem__ и __delitem__
"""Для того что бы можо было обращаться по индексу - __getitem__
что бы устанавливать по индексу - __setitem__
 для удаления по индексу - __delitem__"""

# class Vector:
#
#     def __init__(self, *args):
#         self.values = list(args)
#
#     def __repr__(self):
#         return str(self.values)
#
# v1 = Vector(1,2,3,4,3,2)
# print(v1)
# v2 = Vector(34,343,2,2,23)
# print(v2)
# # print(v2[1]) # Мы не можем обращаться по индексу
# # Изначально любые классы не поддерживают индексирование
# # для того что бы можно было индексировать понадобиться метод __getitem__
#

class Vector:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError("Индекс за границами нашей коллекции")

    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key] = value
        else:
            raise IndexError("Индекс за границами нашей коллекции")

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError("Индекс за границами нашей коллекции")



v2 = Vector(34, 343, 2, 2, 23)
print(v2)
print(v2[1])
v2[1] = 100
print(v2)
print(v2[1])
del v2[13]
print(v2)
