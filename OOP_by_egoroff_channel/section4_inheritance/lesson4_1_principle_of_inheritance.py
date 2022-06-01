# 4.1 Принцип наследования в ООП

# class Doctor:
#
#     def can_breath(self):
#         print('Я могу дышать')
#
#     def can_walk(self):
#         print('Я могу ходить')
#
#     def can_cure(self):
#         print('Я могу лечить')
#
#
# class Architect:
#
#     def can_breath(self):
#         print('Я могу дышать')
#
#     def can_walk(self):
#         print('Я могу ходить')
#
#     def can_build(self):
#         print('Я могу построить здание')


# d = Doctor()
# d.can_cure()
# a = Architect()
# a.can_build()

"""Для того что код не дублировался в классах.
Мы можем одинаковые методы вынести в базовый класс
и наследовать эти методы от базового класса"""


# class Person:
#
#     def can_breath(self):
#         print('Я могу дышать')
#
#     def can_walk(self):
#         print('Я могу ходить')
#
#
#
# class Doctor(Person):
#
#     def can_cure(self):
#         print('Я могу лечить')
#
# class Ortoped(Doctor):
#     pass
#
#
# class Architect(Person):
#
#     def can_build(self):
#         print('Я могу построить здание')
#
#
#
#
# d = Doctor()
# d.can_cure()
# d.can_breath()
# d.can_walk()
#
# o = Ortoped()
# o.can_walk()
# o.can_breath()
# o.can_cure()
#
# a = Architect()
# a.can_build()
# a.can_breath()
# a.can_walk()
# print(issubclass(Doctor, Person))
# print(isinstance(d, Person))

# =======================================================================

"""Ваша задача создать пустые классы Vehicle Car Plane Boat RaceCar, 
которые находятся в следующей иерархии:
Класс Vehicle является базовым классом, от которого наследуются все 
остальные.

Необходимо написать только определение классов
"""

# class Vehicle:
#     pass
#
#
# class Car(Vehicle):
#     pass
#
#
# class RaceCar(Car):
#     pass
#
#
# class Plane(Vehicle):
#     pass
#
#
# class Boat(Vehicle):
#     pass

# =======================================================================

"""
Создайте базовый класс Vehicle, у которого есть:

конструктор __init__, принимающий название транспортного средства, 
его максимальную скорость и пробег. Их необходимо сохранить в 
атрибуты экземпляра name, max_speed и mileage соответственно
метод display_info , который печатает информацию в следующем виде:
Vehicle Name: {name}, Speed: {max_speed}, Mileage: {mileage}
Затем создайте подкласс Bus , унаследованный от Vehicle. Оставьте 
его пустым
"""

# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def display_info(self):
#         print(f'Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}')
#
# class Bus(Vehicle):
#     pass

# bus_99 = Bus("Ikarus", 66, 124567)
# bus_99.display_info()
# #печатает "Vehicle Name: Ikarus, Speed: 66, Mileage: 124567"

# =======================================================================

"""
Создайте базовый класс  Person, у которого есть:

1. конструктор __init__, который должен принимать на вход имя и 
записывать его в атрибут name
2. метод get_name, который возвращает атрибут name;
3. метод  is_employee, который возвращает  False
Затем создайте подкласс Employee , унаследованный от Person. 
В нем должен быть реализован:

1. метод  is_employee, который возвращает  True
"""

class Person:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False

class Employee(Person):

    def is_employee(self):
        return True


emp1 = Person("vasya")
print(emp1.get_name(), emp1.is_employee())  # vasya False

emp2 = Employee("gena bukin")
print(emp2.get_name(), emp2.is_employee())  # gena bukin True

