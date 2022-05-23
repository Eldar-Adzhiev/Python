# 2.5 Публичные, приватные, защищенные атрибуты и методы

class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_public_data(self):
        print(self.name, self.balance, self.passport)

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)

    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob', 100000, 54865656)
account1.print_private_data()
print(account1.__name)
print(account1.__balance)
print(account1.__passport)

# =====================================================================

"""Создайте класс Student, у которого есть:

конструктор __init__, принимающий 3 аргумента и создает приватные 
атрибуты __name, __age, __branch;
приватный метод __display_details , который выводит на экран 
информацию о студенте в следующем виде
Имя: <name>
Возраст: <age>
Направление: <branch>

метод access_private_method, который вызывает приватный метод 
__display_details"""

class Student:

    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print("Имя:", self.__name)
        print("Возраст:", self.__age)
        print("Направление:", self.__branch)

    def access_private_method(self):
        self.__display_details()


obj = Student("Adam Smith", 25, "Information Technology")
obj.access_private_method()

# =============================================================================

"""В этом задании научимся просто вызывать защищенные и приватные 
методы у экземпляров класса."""


class PizzaMaker:
    def __make_pepperoni(self):
        print("Вызов __make_pepperoni")

    def _make_barbecue(self):
        print("Вызов _make_barbecue")


print(PizzaMaker.__dict__.keys())

maker = PizzaMaker()
maker._make_barbecue()
maker._PizzaMaker__make_pepperoni()
