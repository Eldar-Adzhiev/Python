# 4.3 Переопределение методов в Python


# class Person: #parent
#
#     name = 'adam'
#
#     def breathe(self):
#         print('Человек дышит')
#
#     def walk(self):
#         print('Человек идет')
#
# class Doctor(Person): #subclass
#
#     name = 'sklifosovski'
#
#     def breathe(self):
#         print('Доктор дышит')
#
# d = Doctor()
# p = Person()
# p.breathe()
# d.breathe()
# print(p.name)
# print(d.name)

# преопределение магических методов

class Person: #parent

    def __init__(self, name):
        print('init Person')
        self.name = name

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек идет')


class Doctor(Person): #subclass

    def breathe(self):
        print('Доктор дышит')

    def __str__(self):
        return f"Doctor {self.name}"

d = Doctor('Adam')
p = Person('jonh')

print(p)
print(d)










