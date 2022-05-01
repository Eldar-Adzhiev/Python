# 6.2 Ситуации, где полезно использовать словарь

# 1. Подсчет колличества объектов
"""При таком использовании в словаре ключи будут являться объектами,
а значение ключа - количество появления
этих объектов"""


# s =input()
# d = {}
#
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)
#
# for i in sorted(d):
#     print(i, d[i])




# 2. Замена разряженного списка

""" Вместо списка(массива) из большого количества элементов,
в котором предпологается, что не все элементы будут использоваться"""


# s =input()
# d = {}
#
# for i in s:
#     if i.isalpha():
#         d[i] = d.get(i,0) + 1
# print(d)

# 3. Установить соответствие между объектами

# words = {}
#
# while True:
#     s = input()
#     if s in words:
#         print("Слово", s ,"переводится как", words[s])
#     else:
#         print("Введите перевод слова", s)
#         words[s] = input()


# 4. Хранение данных об объекте

contacts = {
    "John Kennedy": {
        'birthday': "29 may 1917", 'city': 'Brookline',
        'phone': None, 'children': 3
    },
    "Arnold Schwarzenegger": {
        'birthday': "30 july 1947", 'city': 'Gradec',
        'phone': '555 - 555 - 555', 'children': 5
    },
    "Donald John Trump": {
        'birthday': "14 july 1946", 'city': 'New York',
        'phone': '777 - 777 - 777', 'children': 4
    }
}

persons = ["John Kennedy", "Arnold Schwarzenegger", "Donald John Trump"]

for person in persons:
    print(person)
    for data in contacts[person]:
        print(contacts[person] [data])



