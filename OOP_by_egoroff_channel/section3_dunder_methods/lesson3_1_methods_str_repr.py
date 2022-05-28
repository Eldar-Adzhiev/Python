# 3.1 Магические методы. Методы __str__ и __repr__


# class Lion:
#     def __init__(self, name):
#         self.name = name
#
# q = Lion('Bob')
# print(q)

# Метод __repr__ отвечает за то как будет отображен объект для разработчика
# т.е. внутри системы

# class Lion:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"The object Lion - {self.name} "
#
# q = Lion('Bob')
# print(q)

# =========================================================================
# Метод __str__ отвечает за то как будет отображен объект для пользователя

class Lion:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Lion - {self.name} "

q = Lion('Bob')
print(q)



































