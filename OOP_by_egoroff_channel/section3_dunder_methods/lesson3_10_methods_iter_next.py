# 3.10 Магические методы __iter__ и __next__


# class Student:
#
#     def __init__(self, name, surname, marks):
#         self.name = name
#         self.surname = surname
#         self.marks = marks
#
#
# igor = Student('Igor', 'Nikolaev', [2,3,4,5,6,5,5,5])
#
# """в данной реализации экземпляр класса нельзя проитерировать"""
#
# for i in igor:
#     print(i)

# ========================================================================

# class Student:
#
#     def __init__(self, name, surname, marks):
#         self.name = name
#         self.surname = surname
#         self.marks = marks
#
#     def __getitem__(self, item):
#         return self.marks[item]
#     #когд есть  __iter__ итерация будет по этому методу, если удалить то по __getitem__
#     def __iter__(self):
#         print('call iter')
#         return iter(self.name)
#
#
#
# igor = Student('Igor', 'Nikolaev', [2,3,4,5,6,5,5,5])
#
# """в данной реализации экземпляр класса нельзя проитерировать"""
#
# for i in igor:
#     print(i)

# ========================================================================
# Если нужно проитерировать сам класс нужно добавить метод __next__

class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.marks[item]

    def __iter__(self):
        print('call iter')
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter



igor = Student('Igor', 'Nikolaev', [2,3,4,5,6,5,5,5])

"""в данной реализации экземпляр класса нельзя проитерировать"""

for i in igor:
    print(i)