# 2.2 Инициализация объекта. Метод init

class Cat:

     def __init__(self, name, breed = 'pers', age = 0, color = 'black'):
         self.name = name
         self.breed = breed
         self.age = age
         self.color = color

# =======================================================================

"""Создайте класс Vehicle, у которого есть:

конструктор __init__, принимающий максимальную скорость и пробег. 
Их необходимо сохранить в атрибуты экземпляра max_speed и mileage 
соответственно"""

class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)# 240 18

# =====================================================================

'''Создайте класс Laptop, у которого есть:

конструктор __init__, принимающий 3 аргумента: бренд, модель и цену 
ноутбука. На основании этих аргументов нужно для экземпляра создать 
атрибуты brand, model, price и также атрибут laptop_name - строковое 
значение, следующего вида: "<brand> <model>"'''

class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{brand} {model}'

laptop1 = Laptop('msi', 'neznau', 86000)
laptop2 = Laptop('apple', 'Pro', 100000)

hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price) # выводит 57000
print(hp.laptop_name) # выводит "hp 15-bw0xx"

# ======================================================================

"""Создайте класс SoccerPlayer, у которого есть:

конструктор __init__, принимающий 2 аргумента: name, surname. Также во
 время инициализации необходимо создать 2 атрибута экземпляра: goals и 
 assists - общее количество голов и передач игрока, изначально оба 
 значения должны быть 0
метод score, который принимает количество голов, забитых игроком, по 
умолчанию данное значение равно единице. Метод должен увеличить общее 
количество забитых голов игрока на переданное значение;
метод make_assist, который принимает количество передач, сделанных
игроком за матч, по умолчанию данное значение равно единице. Метод
должен увеличить общее количество сделанных передач игроком на 
переданное значение;
метод statistics, который вывод на экран статистику игрока в виде:
<Фамилия> <Имя> - голы: <goals>, передачи: <assis"""

class SoccerPlayer:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0


    def score(self, goals=1):
        self.goals +=goals

    def make_assist(self, assists = 1):
        self.assists += assists

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')

leo = SoccerPlayer('Leo', 'Messi')
leo.score(700)
leo.make_assist(500)
leo.statistics() # выводит "Messi Leo - голы: 700, передачи: 500"
kokorin = SoccerPlayer('Alex', 'Kokorin')
kokorin.score()
kokorin.statistics()





















