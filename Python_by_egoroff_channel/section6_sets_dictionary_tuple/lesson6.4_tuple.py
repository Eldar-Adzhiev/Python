# 6.4 Кортежи (tuple). Операции и методы кортежей

# Создание кортежа
a = (1,2,3,4,5)
print(a, type(a))

a = 1,2,3,4,5
print(a, type(a))

b = tuple(range(5))
print(b, type(b))

# Создать пустой кортеж

c = ()
d = tuple()
print(c, d, type(c), type(d))

# Методы кортежей
#  Длина кортежа
print(len(a))

# in
print(2 in a, 5 in a, 6 not in a)

# Сложение кортежей
print(a +b)

# Дублирование кортежей
print(a*10)

# Min and Max, sum func (Только числа)
print(min(a))
print(max(a))
print(sum(a))

a = 1,2,3,4,5, 'hellom', False

print(a.index("hellom"))

# Если список внутри кортежа,то список внутри можно изменить

a = (1,[2,3],4,5, 'hellom', False)

a[1].append(100)
print(a)

"""Кортеж понадобиться если:
1. Нужно гарантировать неизменяемость элементов
2. Кортежи занимают меньше места в памяти"""

# Преобразовать кортеж в список
a = list(a)
print(type(a))




































