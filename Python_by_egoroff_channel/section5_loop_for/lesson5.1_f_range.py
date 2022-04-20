# 5.1 Функция range и итерируемые объекты

print(list(range(5)))

# Range  с шагом

print(list(range(10,20,5)))

# Последовательность по убыванию
print(list(range(10,0, -1)))

# Посчитать сумму последовательности

print("Sum 1-4 =", sum(range(1,4)))

# Найти колличество элементов от и до

print("len from 5 to 20 =", len(range(5,20)))

# Присвоение переменных от и да

a,b,c = range(5,8)
print("a =", a)
print("b =", b)
print("c =", c)

r = range(1,7)
print("index r[2] =", r[2])

# Итерируемый объект

v = iter(range(5))
print(v)

# ===========================================================================================

"""Допишите программу так, чтобы она печатала на экран список, содержащий 
последовательность чисел 0,1,2,3,4,5,6,7,8,9 ?"""

print(list(range(10)))

# ===========================================================================================

"""Теперь необходимо передать в функцию range параметры, чтобы получилась 
последовательность чисел от 12 до 34 включительно"""

print(list(range(12,35 )))

# =======================================================================================

"""Теперь давайте добавим шаг. Необходимо сформировать последовательность 25, 33, 
41, 49, 57 .... , 169"""

print(list(range( 25,170,8)))

# ========================================================================================

"""Нам осталось поработать с убывающими последовательностями.
Сформируйте последовательность -11, -12, -13, -14 .... , -35"""

print(list(range(-11, -36, -1 )))

# ========================================================================================

"""Сформируйте последовательность 10, 9, 8, 7, ... , 0"""

print(list(range(10,-1,-1 )))

# =======================================================================================

"""И последняя последовательность 1000, 950, 900, 850, ... , 500"""

print(list(range(1000,499,-50)))

