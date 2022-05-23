# 2.4 Моносостояние для экземпляров класса

class Cat:

     breed = 'pers'

a = Cat()
b = Cat()

a.breed = 'siam'
b.color = 'black'
c = Cat()

# Сделаем так что бы при изменении одного экземпляра, это затрагивало все

class Cat:
    __shared_attr = {      # Формирование единого словаря атрибутов класса
        'breed': 'pers',   # При изменении значений - эти значения обновятся
        'color': 'black'   # во всех экземплярах класса
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr  # Передаём в инициализатор ссылку на
                                           # созданный моно-словарь


cat1 = Cat()
cat2 = Cat()
print(cat1.__dict__)  # Проверим словарь атрибутов ЭК cat1
print(cat2.__dict__)  # Проверим словарь атрибутов ЭК cat
cat1.breed, cat1.color = 'pers', 'white'  # Меняем атрибуты у cat1
print('cat1:', cat1.__dict__)
print('cat2:', cat2.__dict__) # Видим, что у cat2 тоже поменялись атрибуты
cat2.breed, cat2.color = 'siam', 'gray'  # Меняем атрибуты у cat2
print('cat1:', cat1.__dict__) # Меняется и у cat1
print('cat2:', cat2.__dict__)

# У всех экземпляров будет одинаковое состояние










