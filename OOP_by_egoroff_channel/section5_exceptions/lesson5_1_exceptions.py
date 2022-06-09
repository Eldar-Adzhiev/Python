# 5.1 Исключения в Python

# print('hello')
# print('hello1')
# print('hello2')
# # 'hello'[9]
# # a+b
# print ('hello3')
# print('hello4')
# print('hello5')

# =====================================================================
# Обработка ошибки

# print('hello')
# print('hello1')
# print('hello2')
# try:
#     int('hello')
# except ValueError:
#     print('неправильное преобразование')
# print ('hello3')
# print('hello4')
# print('hello5')

# ===============================================================

"""
Все исключения являются классами.
"""

# t = IndexError()
# print(isinstance(t, LookupError))
#
# # Так же можно просто обратится к классу родителя
#
# print('hello')
# print('hello1')
# print('hello2')
# try:
#     {}[5]
# except LookupError:
#     print('неправильное преобразование')
# print ('hello3')
# print('hello4')
# print('hello5')

# ================================================================

print('hello1')
print('hello2')
raise ValueError('Неправильное значение')
print ('hello3')
print('hello4')
print('hello5')