# 2.7 Декоратор Property

# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
#     def get_balance(self):
#         print("get_balance")
#         return self.__balance
#
#     def set_balance(self, value):
#         print("set_balance", value)
#         if not isinstance(value, (int, float)):
#             raise ValueError('Баланс должен быть числом')
#         self.__balance = value
#
#     def delete_balance(self):
#         print("delete_balance")
#         del self.__balance
#
#     my_balance = property(get_balance)
#     # my_balance = my_balance.getter(get_balance)
#     my_balance = my_balance.setter(set_balance)
#     my_balance = my_balance.deleter(delete_balance)
#
# a = BankAccount('Ivan', 100)
# print(a.my_balance)
# a.my_balance = 999
# print(a.my_balance)

# ========================================================================

# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#     @property
#     def my_balance(self):
#         print("get_balance")
#         return self.__balance
#
#     # my_property_balance = my_balance
#
#     @my_balance.setter
#     def my_balance(self, value):
#         print("set_balance", value)
#         if not isinstance(value, (int, float)):
#             raise ValueError('Баланс должен быть числом')
#         self.__balance = value
#
#     @my_balance.deleter
#     def my_balance(self):
#         print("delete_balance")
#         del self.__balance
#
#     # my_balance = property(my_balance)
#     # my_balance = my_balance.getter(get_balance)
#     # my_balance = my_property_balance.setter(my_balance)
#     # my_balance = my_balance.deleter(delete_balance)
#
# # b = BankAccount('Misha', 200)
# # print(b.my_balance)
#
# eldar = BankAccount('Eldar', 100000000)
# print(eldar.my_balance)
# eldar.my_balance = 110000000
# print(eldar.my_balance)
# del eldar.my_balance

# ========================================================================

""" Создайте класс Notebook, у которого есть:

конструктор __init__, принимающий 1 аргумента: список записей, в
принципе там могут быть любые значения. Необходимо сохранить его в
защищенном атрибуте ._notes
свойство notes_list, которое распечатает содержимое атрибута ._notes
в виде упорядоченного списка (см. пример ниже)
note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list

После этого на экране вы должны увидеть

1.Buy Potato
2.Buy Carrot
3.Wash car"""

# class Notebook:
#
#     def __init__(self, notes):
#         self._notes = notes
#
#     @property
#     def notes_list(self):
#         for i in self._notes:
#             print(f'{int(self._notes.index(i))+1}.{i}')
#
#
# note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
# note.notes_list

# ========================================================================

""" Создайте класс Money, у которого есть:

конструктор __init__, принимающий 2 аргумента: dollars, cents. 
По входным аргументам вам необходимо создать атрибут экземпляра 
total_cents. 
свойство геттер dollars, которое возвращает количество имеющихся 
долларов;
свойство сеттер dollars, которое принимает целое неотрицательное 
число - количество долларов и устанавливает при помощи него новое 
значение в атрибут экземпляра total_cents, при этом значение центов 
должно сохранятся. В случае, если в сеттер передано число, не 
удовлетворяющее условию, нужно печатать на экран сообщение 
"Error dollars";
свойство геттер cents, которое возвращает количество имеющихся центов;
свойство сеттер cents, которое принимает целое неотрицательное число
меньшее 100 - количество центов и устанавливает при помощи него новое
значение в атрибут экземпляра total_cents, при этом значение долларов
должно сохранятся. В случае, если в сеттер передано число, не 
удовлетворяющее условию, нужно печатать на экран сообщение "Error cents";
метод __str__ (информация по данному методу), который возвращает 
строку вида "Ваше состояние составляет {dollars} долларов {cents} 
центов". Для нахождения долларов и центов в методе __str__ 
пользуйтесь свойствами"""

class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars*100+cents

    @property
    def dollars(self):
        return self.total_cents//100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value >= 0:
            self.total_cents = value * 100 + self.cents
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents%100

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and 100 > value >= 0:
            self.total_cents = self.dollars*100 + value
        else:
            print("Error cents")

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
print(Bill.total_cents) # 10199
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов