# 3.2 Магические методы __len__ и __abs__

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __len__(self):
#         return len(self.name + self.surname)
#
# b = Person("a", "aaa")
# print(len(b))

# =====================================================================

class Otrezok:

    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self) # = self.x2 - self.x1

    def __abs__(self):
        return abs(self.x2 - self.x1)

q = Otrezok(2,9)
print(len(q))

w = Otrezok(10, 5)
print(len(w))







