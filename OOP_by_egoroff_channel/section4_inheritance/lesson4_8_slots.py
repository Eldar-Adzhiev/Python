# 4.8 Slots

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(2,3)
print(p1.x)
print(p1.y)
p1.q = 100
print(p1.q)


# Slots -  нужен для того что бы ограничить создание атрибутов
class PointSlots:

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

p2 = PointSlots(2,3)
print(p1.x)
print(p1.y)
del p2.y #  удалили атрибут y
# p2.q = 12 # Пытаемся создать атрибут котрый не должен быть
p2.y = 12 # создаем атрибут который доступен в слотс






























