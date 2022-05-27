# 2.11 Практика по методам и свойствам (property)

from string import digits

#
# class User:
#
#     def __init__(self, login, password):
#         self.login = login
#         self.__password = password
#
#     @property
#     def password(self):
#         print('getter called')
#         return self.__password
#
#     @staticmethod
#     def is_include_number(password):
#         for digit in digits:
#             if digit in password:
#                 return True
#         return False
#
#     @password.setter
#     def password(self, value):
#         print('setter called')
#         if not isinstance(value, str):
#             raise TypeError('Пароль должен быть строкой')
#         if len(value) < 4:
#             raise ValueError("Длина пароля слишком мала, минимум должно быть 4 симфола")
#         if len(value) > 12:
#             raise ValueError("Длина пароля слишком велика, минимум должно быть 12 симфола")
#         if not User.is_include_number(value):
#             raise ValueError("Пароль должен содержать хотябы одну цифру")
#         self.__password = value
#
# r = User('aaa', 123)
# r.password = '123aaa'

# Для того что бы проверка пароля делалась при создании
# эземпляра класса. переименуем защишенную переменную __password
# равной имени свойства сеттер

from string import digits


class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def password(self):
        print('getter called')
        return self.__password

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if len(value) < 4:
            raise ValueError("Длина пароля слишком мала, минимум должно быть 4 симфола")
        if len(value) > 12:
            raise ValueError("Длина пароля слишком велика, минимум должно быть 12 симфола")
        if not User.is_include_number(value):
            raise ValueError("Пароль должен содержать хотябы одну цифру")
        self.__password = value


k = User('aaa', 123)












