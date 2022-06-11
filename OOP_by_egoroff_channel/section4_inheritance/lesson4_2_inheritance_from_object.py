# 4.2 Наследование от object и от других встроенных типов

# class Person:
#     pass
#
# class Doctor(Person):
#     pass
#
# class Architect(Person):
#     pass
#
# # Любой класс наследуется от Объекта
#
# print(issubclass(Person, object))


# ======================================================================

"""
Создайте класс NewInt, который унаследован от целого типа int,
то есть мы будем унаследовать поведение целых чисел и значит
экземплярам нашего класса будут поддерживать те же операции, что и
целые числа.

Дополнительно в классе NewInt нужно создать:

- метод repeat, который принимает одно целое положительное число n
(по умолчанию равное 2), обозначающее сколько раз нужно продублировать
данное число. Метод repeat должен возвращать новое число,
продублированное n раз (см пример ниже);
- метод to_bin, который возвращает двоичное представление числа в виде
числа (может пригодиться функция bin)
"""

class NewInt(int):

    def __init__(self, value):
        self.value = value

    def repeat(self, n=2):
        return int(str(self.value)*n)

    def to_bin(self):
        return bin(self.value)[2:]

a = NewInt(9)
print(a.repeat())  # печатает число 99
d = NewInt(a + 5)
print(d.repeat(3)) # печатает число 141414
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin()) # печатает 100011 - двоичное представление числа 35

