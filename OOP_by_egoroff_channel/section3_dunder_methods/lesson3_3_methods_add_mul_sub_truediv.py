# 3.3 Магические методы __add__, __mul__, __sub__ и __truediv__

# Метод __add__ = прибавлние

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def __add__(self, other):
#         print("__add__ call")
#         if isinstance(other, BankAccount):
#             return self.balance + other.balance
#         if isinstance(other, (int, float)):
#             return self.balance + other
#         raise NotImplemented
#
#     def __radd__(self, other): # Для того что бы можно было ставить цифру впереди экземпляра
#
#         print("__radd__ call")
#         return self+other
#
# t = BankAccount('Misha', 80)
# print(t+12)
# print(12 + t)

# ========================================================================

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print("__add__ call")
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return self.balance + other
        raise NotImplemented

    def __mul__(self, other):
        print("__add__ call")
        if isinstance(other, BankAccount):
            return self.balance * other.balance
        if isinstance(other, (int, float)):
            return self.balance * other
        if isinstance(other, str):
            return self.name + other
        raise NotImplemented

    def __radd__(self, other): # Для того что бы можно было ставить цифру впереди экземпляра

        print("__radd__ call")
        return self+other

t = BankAccount('Misha', 80)
print(t * 12)
print(t * 'TT')

# ======================================================================













