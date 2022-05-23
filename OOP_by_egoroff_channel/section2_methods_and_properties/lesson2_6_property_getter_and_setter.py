# 2.6 Геттеры и сеттеры, property атрибуты

# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#
# a = BankAccount('Ivan', 100)
# print('balance =', a.balance)
# print('name =', a.name)
# a.balance = 'hello'
# print('balance =', a.balance)

# Для того что бы можно было в баланс мы могли устанавливать только цифры


# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
#     def get_balance(self):
#         return self.__balance
#
#     def set_balance(self, value):
#         if not isinstance(value, (int, float)):
#             raise ValueError('Баланс должен быть числом')
#         self.__balance = value
#
#
# b = BankAccount('Tniya', 100)
# # b.set_balance('sadasdsad') # Выведет ошибку
# b.set_balance(300)
# print(b.get_balance()) # Вывудет установленный баланс

#===========================================================================

# Для того что бы все время не использовать методы get_balance и set_balance
# можно использовать class property

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print("get_balance")
        return self.__balance

    def set_balance(self, value):
        print("set_balance", value)
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):
        print("delete_balance")
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)


c = BankAccount('Misha', 400)
print(c.balance)
c.balance = 777
print(c.balance)
del c.balance

# =======================================================================

"""Создайте класс UserMail, у которого есть:

конструктор __init__, принимающий 2 аргумента: логин и почтовый 
адрес. Их необходимо сохранить в экземпляр как атрибуты login и 
__email (обратите внимание, защищенный атрибут)
метод геттер get_email, который возвращает защищенный атрибут __email;
метод сеттер set_email, который принимает в виде строки новую почту. 
Метод должен проверять, что в новой почте есть только один символ @ и
после нее есть точка. Если данные условия выполняются, новая почта 
сохраняется в атрибут __email, в противном случае выведите сообщение 
"ErrorMail:<почта>";
создайте свойство email, у которого геттером будет метод get_email, 
а сеттером - метод set_email"""


class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, value):
        if isinstance(value, str) \
                and value.count('@') == 1 \
                and "." in value[value.find('@'):]:
            self.__email = value
        else:
            print(f'ErrorMail:{value}')

    email = property(fget=get_email, fset=set_email)


k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3] # ErrorMail:[1, 2, 3]
k.email = 'prince@still@.wait'  # ErrorMail:prince@still@.wait
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait