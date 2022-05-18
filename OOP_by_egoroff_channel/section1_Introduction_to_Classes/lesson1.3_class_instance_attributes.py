#  1.3 Атрибуты экземпляра класса

class Person:
    name = 'Ivan'
    age = 30


man = Person()    # Создаём ЭК и связываем его с переменной man
print(man.age)    # Получаем текущее значение атрибута age в ЭК man
man.money = 100   # Создаём в ЭК атрибут money со значением 100
print(man.money)  # Получаем текущее значение атрибута money в ЭК man
man.money = 250   # Изменяем текущее значение атрибута money в ЭК man на 250
print(man.money)  # Получаем текущее значение атрибута money в ЭК man
delattr(man, 'money')  # Удаляем атрибут money из ЭК
print(hasattr(man, 'money'))  # Проверяем наличие атрибута money в ЭК man: False


# ============================================================================

man = Person()
print(man.__dict__)
print('-------')
print(Person.__dict__)


man = Person()
print(man.__dict__)# Печатает пустой словарь: {}
man.name = 'Alex'
print(man.__dict__)# Печатает словарь: {'name': 'Alex'}


man = Person()
print(man.__dict__)
man.name = 'Alex'
print('Атрибуты ЭК:', man.__dict__)
print('Атрибуты класса:', Person.__dict__)

"""Ниже определен пустой класс SuperHero. Ваша задача  создать два ЭК 
и сохранить их в переменные batman и superman

Для ЭК, хранящегося в переменной batman, необходимо создать

атрибут can_fly со значением False
атрибут damage со значением 175
Для ЭК, хранящегося в переменной superman, необходимо создать

атрибут can_fly со значением True
атрибут damage со значением 285
атрибут alter_ego со значением 'Кларк Кент'
Ничего выводить на экран в этом задании не требуется"""


class SuperHero:
    pass

batman = SuperHero()
superman = SuperHero()

batman.can_fly =False
batman.damage = 175

print(batman.__dict__)

superman.can_fly = True
superman.damage = 285
superman.alter_ego = 'Кларк Кент'









