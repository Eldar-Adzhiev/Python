# 6.1 Словари Python. Операции и методы словаря

# d = {key: value}

# d = {
#     'moskva': 495,
#     'piter': 812,
#     'penza': 8412
# }

# print(d)

# второй способ создать словарь

# r = dict(moskva=495, piter=812, penza=8412)
# print(r)

# создание словаря из списка

# a = [['moskva',111], ['piter', 222], ['penza', 333]]
# t = dict(a)
# print(t)

# инциализировать ключи определенным значением

# q = dict.fromkeys(['a','b','c'], 100)
# print(q)

# Создать пустой словарь

# v = {}
# print(v, type(v))
#
# v = dict()
# print(v, type(v))

# ================================================================

# d = {
#     1:'one',
#     2: 'two',
#     3: 'three'
# }
#
# print(d[3])

# Добавить значение в словарь
# d[4] = 'four'
# d[5] = 'five'
# print(d)

# Изменение значения ключа

# d[3] = 'Три'
# print(d)

# Создание словаря из целого предложения

# person = {}

# s = "IVANOV IVAN Samara SGU 5 4 5 5 4 3 5"
# s = s.split()
# person['lastName'] = s[0]
# person['firstName'] = s[1]
# person['city'] = s[2]
# person['university'] = s[3]
# person['marks'] = []
# for i in s[4:]:
#     person['marks'].append(int(i))
# print(s)
# print(person)

# Удаление элемента из словаря

d = {
    1:'one',
    2: 'two',
    3: 'three'
}

# del d[2]
# print(d)
#
# print(len(d))  # Длина словаря
# print(5 not in d)

# Итерация словаря

# for key in d:
#     print(key, d[key])

# Методы словаря

# d.clear()
# print(d)

# print(d.get(1))
#
# d.setdefault(2,'seven')
# print(d)
#
# print(d.pop(3))
# print(d)
#
# print(d.popitem())
# print(d)

print(d.keys())

print(d.values())
for value in d.values():
    print(value)

print(d.items())
for para in d.items():
    print(para[0], para[1])

for key, value in d.items():
    print(key, value)
