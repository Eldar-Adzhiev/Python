# Написать функцию которая сгенерирует список имен
# Написать функцию которая сгенерирует список возрастов
# Написать функцию которая получив на вход два готовых списка сделесписко списков с именем и возрастом
import datetime

import names


def names_function():
    lis_with_names = []
    for i in range(20):
        name = names.get_full_name()
        lis_with_names.append(name)

    return lis_with_names

names_function()
print(names_function())

def age_function():
    list_with_ages = []
    for i  in range(20):
        age = datetime.date().year
        list_with_ages.append(age)
    print(list_with_ages)

age_function()