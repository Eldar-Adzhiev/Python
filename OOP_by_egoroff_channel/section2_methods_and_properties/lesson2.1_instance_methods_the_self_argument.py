# 2.1 Методы экземпляра. Аргумент self

# class Cat:
#     def hello():
#         print("Hello world from kitty")
#
# Cat.hello()
#
# Bob =Cat()
#
# # Bob.hello() # при вызове метода, объект с которым он связан будет автоматически подставляться в аргумент метода
#
# class Cat:
#     def hello(*args):
#         print("Hello world from kitty")
#
# jim =Cat()
# jim.hello()
#
# # Мы можете дать любое название этому аргументу, но в pep8 принято называть его self (мы об этом поговорим на следующем занятии.
#
#
# """Создайте класс Lion. В нем должен быть метод roar, который
# печатает на экран "Rrrrrrr!!!"
#
# Необходимо написать только определение класса
#
# Пример работы с классом Lion"""
#
# class Lion:
#
#     def roar(self):
#         print("Rrrrrrr!!!")
#
# simba = Lion()
# simba.roar()
#
# # ==============================================================================
#
# """Создайте класс Counter, экземпляры которого будут подсчитывать
# внутри себя значения.
#
# В классе Counter нужно определить метод start_from, который принимает
# один необязательный аргумент - значение, с которого начинается подсчет,
# по умолчанию равно 0
#
# Также нужно создать метод increment, который увеличивает счетчик на 1.
#
# Затем необходимо создать метод display, который печатает фразу "Текущее
# значение счетчика = <value>" и метод reset,  который обнуляет
# экземпляр счетчика"""
#
# class Counter:
#
#     counter =0
#
#     def start_from(self, counter=0):
#         self.counter = counter
#
#     def increment(self):
#         self.counter += 1
#
#     def display(self):
#         print("Текущее значение счетчика =", self.counter)
#
#     def reset(self):
#         self.counter =0
#
# c1 = Counter()
# c1.start_from()
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 1"
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 2"
# c1.reset()
# c1.display() # печатает "Текущее значение счетчика = 0"
#
# c2 = Counter()
# c2.start_from(3)
# c2.display() # печатает "Текущее значение счетчика = 3"
# c2.increment()
# c2.display() # печатает "Текущее значение счетчика = 4"

# ==================================================================================

"""Создайте класс Point. У этого класса должны быть

метод set_coordinates, который принимает координаты по x и по y, и 
сохраняет их в экземпляр класса соответственно в атрибуты x и y 
метод get_distance, который обязательно принимает экземпляр класса 
Point и возвращает расстояние между двумя точками по теореме Пифагора.
В случае, если в данный метод передается не экземпляр класса Point 
необходимо вывести сообщение "Передана не точка"""

class Point:
    x = 0
    y = 0

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, obj):
        if isinstance(obj, Point):
            return ((obj.x - self.x)**2 + (obj.y - self.y)**2)**0.5
        else:
            print("Передана не точка")

p1 =Point()
p2 = Point()
p1.set_coordinates(1,2)
p2.set_coordinates(4,6)
print(p1.x, p1.y)
print(p2.x, p2.y)
d = p1.get_distance(p2)
print(d)
p1.get_distance(10)











