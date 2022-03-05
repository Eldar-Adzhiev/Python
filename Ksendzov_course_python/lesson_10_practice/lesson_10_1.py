#Создать массив из любых трех цифр
import random
import secrets

import names

a  = [1,2,3]

# Итерировать этот список и вывести в консоль
for i in a:
    print(i)

# Сгенерировать список из 20 цифр
b = list(range(20))
print(b)

# Cгенерировать список где числа деляться только на два без остатка
c = [i for i in range(20) if i % 2 == 0 and i > 0] # Тернарный оператор
print(c)

# Сгенерировать нечетные числа до 20
c1 = [i for i in range(20) if i % 2 == 1 and i > 0]
print(c1)

# Cгенерировать список нечетных без  for
d = list(range(2,21,2))
print(d)

# Сгенерировать список слов где слово (item_1, item_2  и т.д до 20)
i = 0
c = ['item_'+ str(i) for i in range(20)]
print(c)

# Cгенерировать список из 20 имен
list_names = []
for k in range(20):
    k = names.get_full_name()
    list_names.append(k)
print(list_names)

# Cгененировать csv  файл в котором имя, возрвст и зарплата


# Cписок списков в котором каждый внутренний список будет содержать имяб возраст и зарплату
list_name_age_salary = []
for i in range(20):
    name_age_salary = []
    b = names.get_full_name()
    c = list(range(18, 90))
    d = list(range(1500,10000))
    e = secrets.choice(c)
    h = secrets.choice(d)
    name_age_salary.append(b)
    name_age_salary.append(e)
    name_age_salary.append(h)
    list_name_age_salary.append(name_age_salary)
print(list_name_age_salary)
























