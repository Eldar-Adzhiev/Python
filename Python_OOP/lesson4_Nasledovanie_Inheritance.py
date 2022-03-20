# # Простое наследование методов родительского класса
#
# class Table:
#     def __init__(self, l, w, h):
#         self.length = l
#         self.width = w
#         self.height = h
#
#
# class KitchenTable(Table):
#     def setPlaces(self, p):
#         self.places = p
#
#
# class DeskTable(Table):
#     def square(self):
#         return self.width * self.length
#
#
# t1 = KitchenTable(2, 2, 0.7)
# print(t1)
# t2 = DeskTable(1.5, 0.8, 0.75)
# print(t2)
# t3 = KitchenTable(1, 1.2, 0.8)
# print(t3.__dict__)
#
# # Полное переопределение метода надкласса
#
# class ComputerTable(DeskTable):
#     def square(self, e):
#         return self.width * self.length - e
#
# ct1 = ComputerTable(2,2,2)
#
# print(ct1.square(1))
#
# # Дополнение, оно же расширение, метода
#
# class ComputerTable2(DeskTable):
#     def square(self, e):
#         return DeskTable.square(self) - e
# ct2 = ComputerTable2(3,3,3)
# print(ct2.square(1))
#
# class KitchenTable(Table):
#     def __init__(self, l, w, h, p):
#         Table.__init__(self, l, w, h)
#         self.places = p

# Практическая работа

""""Разработайте программу по следующему описанию.
В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный 
номер объекта, и свойство, в котором хранится принадлежность команде. У солдат есть метод 
"иду за героем", который в качестве аргумента принимает объект типа "герой". У героев есть 
метод увеличения собственного уровня. 
В основной ветке программы создается по одному герою для каждой команды. В цикле 
генерируются объекты4солдаты. Их принадлежность команде определяется случайно. Солдаты 
разных команд добавляются в разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя, 
принадлежащего команде с более длинным списком, поднимается уровень. 
Отправьте одного из солдат первого героя следовать за ним. Выведите на экран 
идентификационные номера этих двух юнитов.
"""
from random import randint

class Person:
    count = 0
    def __init__(self,  komanda):
        self.id = Person.count
        Person.count += 1
        self.komanda = komanda

class Hero(Person):
    def __init__(self, komanda):
        Person.__init__(self, komanda)
        self.level = 1


    def up_level(self):
        self.level += 1


class Soldat(Person):
    def __init__(self, komanda):
        Person.__init__(self, komanda)
        self.my_hero = None


    def idy_za_hero(self, hero):
        self.my_hero = hero.id

hero_1 = Hero(1)
print(hero_1.komanda)
hero_2 = Hero(2)
print((hero_2.komanda))

army_1 = []
army_2 = []

for i in range(20):
    n = randint(1,2)
    if n == 1:
        army_1.append(Soldat(n))
    else:
        army_2.append(Soldat(n))
    print("army_1 =", army_1)
    print("army_2 =", army_2)

print("Kollichestvo soldat v army_1 =", len(army_1), "Kollichestvo soldat v army_2 =",len(army_2), sep="\n")

print("LEVEL_do Hero_1 =", hero_1.level)
print("Level_do Hero_2 =", hero_2.level)

if len(army_1) > len(army_2):
    hero_1.up_level()
else:
    hero_2.up_level()

print("LEVEL Hero_1 =", hero_1.level)
print("Level Hero_2 =", hero_2.level)

army_1[0].idy_za_hero(hero_1)
print("ID pervogo soldata =", army_1[0].id,  "ID hero_1 =", hero_1.id, sep='\n')







