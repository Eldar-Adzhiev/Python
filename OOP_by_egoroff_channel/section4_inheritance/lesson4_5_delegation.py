# 4.5 Делегирование в Python

# class Person:
#
#     def breathe(self):
#         print('Человек дышит')
#
# class Doctor(Person):
#
#
#     def breathe(self):
#         super().breathe()
#         print("Доктор дышит")
#         super().breathe()
#
#
# p = Person()
# d = Doctor()
# d.breathe()

# ==================================================================

# class Person:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def breathe(self):
#         print('Человек дышит')
#
#
# class Doctor(Person):
#
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def breathe(self):
#         super().breathe()
#         print("Доктор дышит")
#         super().breathe()
#
#
# p = Person('Ivan', 'Ivanov')
# d = Doctor('Petr', 'Petrov', 25)
# print(p.name, p.surname)
# print(d.name, d.surname, d.age)

# ============================================================

# Заменяем дублирование кода с помощью делегирования

# class Person:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def breathe(self):
#         print('Человек дышит')
#
#
# class Doctor(Person):
#
#     def __init__(self, name, surname, age):
#         super().__init__(name, surname,)
#         self.age = age
#
#     def breathe(self):
#         super().breathe()
#         print("Доктор дышит")
#
#
#
# p = Person('Ivan', 'Ivanov')
# d = Doctor('Petr', 'Petrov', 25)
# print(p.name, p.surname)
# print(d.name, d.surname, d.age)

# =====================================================================

"""
Создайте базовый класс  Person, у которого есть:

1. конструктор __init__, который должен принимать на вход имя и
номер паспорта и записывать их в атрибуты name, passport
2. метод display, который печатает на экран сообщение «<имя>:
<паспорт>»;

Затем создайте подкласс Employee , унаследованный от Person. В нем
должен быть реализован:

1. метод  __init__, который принимает именно в таком порядке четыре
значения: имя, паспорт, зарплату и отдел. Их нужно сохранить в
атрибуты  name, passport, salary,department. При этом создание
атрибутов name, passportнеобходимо делегировать базовому классу
Person
"""

# class Person:
#
#     def __init__(self, name, passport):
#         self.name = name
#         self.passport = passport
#
#     def display(self):
#         print(f'{self.name}: {self.passport}')
#
#
# class Employee(Person):
#
#     def __init__(self, name, passport, salary, department):
#         super().__init__(name, passport)
#         self.salary = salary
#         self.department = department
#
#
# a = Employee('Raul', 886012, 200000, "QA")
# a.display()  # печатает "Raul: 886012"

# ====================================================================

"""
Создайте базовый класс Vehicle, у которого есть:

1. метод __init__, принимающий название транспортного средства, 
пробег и вместимость. Их необходимо сохранить в атрибуты экземпляра
name, mileage и  capacity соответственно

2. метод fare , который возвращает стоимость проезда из расчета  
capacity * 100:

3. метод display , который печатает строку следующего вида:

Total <name> fare is: <метод fare>

Затем создайте подкласс Bus , унаследованный от Vehicle. В нем 
необходимо:

1. переопределить метод __init__. Он должен принимать два значения:
название транспортного средства и пробег. Необходимо делегировать 
создание атрибутов name, mileage и  capacityбазовому классу, в 
качестве аргумента передайте capacity  значение 50

2. переопределить метод fare . Он должен получить стоимость проезда 
у родительского класса и увеличить ее на 10%. 

После создайте подкласс Taxi , унаследованный от Vehicle. В нем 
необходимо:

1. переопределить метод __init__. Он должен принимать два значения: 
название транспортного средства и пробег. Необходимо делегировать 
создание атрибутов name, mileage и  capacityбазовому классу, в 
качестве аргумента передайте capacity  значение 4

2. переопределить метод fare . Он должен получить стоимость проезда
у родительского класса и увеличить ее на 35%. 
"""


class Vehicle:

    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity*100

    def display(self):
        print(f'Total {self.name} fare is: {self.fare()}')


class Bus(Vehicle):

    def __init__(self, name, mileage):
        super().__init__(name, mileage, capacity=50)

    def fare(self):
        return super().fare() + (super().fare() * 10/100)


class Taxi(Vehicle):

    def __init__(self, name, mileage):
        super().__init__(name, mileage, capacity=4)

    def fare(self):
        return super().fare() + (super().fare() * 35 / 100)



sc = Vehicle('Scooter', 100, 2)
sc.display()

merc = Bus("Mercedes", 120000)
merc.display()

polo = Taxi("Volkswagen Polo", 15000)
polo.display()

# ====================================================================


