# 2.10 Пространство имен класса

# class DepartmentIT:
#     PYTHON_DEV = 3
#     GO_DEV = 3
#     REACT_DEV = 2
#
#     def info(self):
#         print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)
#
#     def info2(self):
#         print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV,DepartmentIT.REACT_DEV)
#
#     @property
#     def info_prop(self):
#         print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)
#
#     @classmethod
#     def info_class(cls):
#         print('info_class')
#         print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV )
#
#     @staticmethod
#     def info_static():
#         print('info_static')
#         print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)
#
#     def make_backend(self):
#         print('Python and Go')
#
#     def make_frontend(self):
#         print('React')
#
# it1 = DepartmentIT()
# it1.info()
# it1.info2()
# it1.info_prop
# it1.info_class()
# it1.info_static()

# ========================================================================

"""Создайте базовый класс User, у которого есть:

1. метод __init__, принимающий имя пользователя и его роль. Их
необходимо сохранить в атрибуты экземпляра name и role соответственно

Затем создайте класс Access , у которого есть:

2. приватный атрибут класса __access_list , в котором хранится список 
['admin', 'developer']
приватный статик-метод __check_access , который принимает название 
роли и возвращает True, если роль находится в списке __access_list , 
иначе - False 
3. публичный статик-метод get_access , который должен принимать экземпляр
класса User и проверять есть ли доступ у данного пользователя к ресурсу
при помощи метода __check_access  . Если у пользователя достаточно прав,
выведите на экран сообщение «User <name>: success», если прав 
недостаточно - «AccessDenied». Если передается тип данных отличный от
экземпляр класса Userнеобходимо вывести"""

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Access:

    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(role_name):
        if role_name in Access.__access_list:
            return True
        else:
            return False

    @staticmethod
    def get_access(user_instance):
        if not isinstance(user_instance, User):
            print("AccessTypeError")
        elif Access.__check_access(user_instance.role) == True \
                and isinstance(user_instance, User):
            print(f'User {user_instance.name}: success')
        elif Access.__check_access(user_instance.role) == False \
                and isinstance(user_instance, User):
            print("AccessDenied")


user1 = User('batya99', 'admin')
Access.get_access(user1)

zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya)

Access.get_access(5) # печатает AccessTypeError
















