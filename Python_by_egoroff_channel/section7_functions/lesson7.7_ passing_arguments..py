# 7.7 Передача аргументов. Сопоставление аргументов по имени и позиции

# позиционный

def f(a,b,c):
    print(a,b,c)

f(1,2,3)

# по имени
f(b=10, c=20, a=30)

# комбинированный
f(5, c=60, b=15)

# аргументы по умолчанию
def f(a,b,c='Неизвестно'):
    print(a,b,c)

f(2,3)
f('ghbdt', 'dd', 'ddd')

# =========================================================================

# Изменяемые объекты в качестве значений по умолчанию
# Если в качеств аргумента использовать пустой список (my_list=[]) то все вызовы
# будут добавлять элементы в список, поэтому создается с значением по умолчанию my_list=None
def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    print(my_list, id(my_list))

def append_to_dict(key, value, my_dict=None):
    if my_dict is None:
        my_dict = {}
    my_dict[key]= value
    print(my_dict)

append_to_dict(10, 100)
append_to_dict(20, 200)












