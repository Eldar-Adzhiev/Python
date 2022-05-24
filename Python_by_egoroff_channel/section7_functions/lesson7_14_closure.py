# 7.14 Замыкания в Python. Closure Python

# def main_func():
#
#     def inner_func():
#         print('hello from inner func')
#
#     inner_func()
#
# print(main_func()) # main_func  возращает  None так как  функция
# # вызывается внутри без return


# def main_func(value):
#
#     # name = value
#
#     def inner_func():
#         print('hello from inner func', value)
#
#     return inner_func
#
# r = main_func('Misha')
# r()
#
# v = main_func('Vasya')
# v()

# =====================================================================

# def adder(value):
#     def inner(a):
#         return value + a
#
#     return inner
#
# a2 = adder(2)
# print(a2(10))

# =====================================================================

# Счет сколько раз былавызвана функция

# def counter():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#
#     return inner
#
# e = counter()
# print(e())
# print(e())
# print(e())
# print(e())

# =====================================================================

"""Ваша задача создать функцию multiply, которая принимает один 
аргумент. Функция должна запомнить это значение, и вернуть результат 
умножения этого числа с переданным вновь значением (см. примеры)"""

# def multiply(value):
#
#     def inner(value_inner):
#         return value_inner * value
#
#     return inner
#
# f_2 = multiply(2)
# print("Умножение 2 на 5 =", f_2(5)) #10
# print("Умножение 2 на 15 =", f_2(15)) #30
# f_3 = multiply(3)
# print("Умножение 3 на 5 =", f_3(5)) #15
# print("Умножение 3 на 15 =", f_3(15)) #45

# =====================================================================










