#  5.5 Вложенные циклы

# for i in range(3):
#     for j in range(5):
#         print(j, i)
#     print()

# ==================================================================================

# Длина пароля 3. Переберем все цифры буквы и символы

# from string import printable
#
# print(printable)
#
# for b1 in printable:
#     for b2 in printable:
#         for b3 in printable:
#             print(b1, b2, b3)

# Таблица умножения

# for i in range(1,10):
#     for j in range(1,10):
#         print(j,"*",i, "=", i*j, end="  ")
#     print()

#===================================================================================

# """Сколько шестибуквенных слов, начинающихся и заканчивающихся
# согласной буквой и содержащих ровно 2 гласные, можно составить
# из букв Т, Ы, К, В, А? Каждая из допустимых букв может входить
# в слово несколько раз"""
#
# k = 0
#
# for b1 in 'tukva':
#     for b2 in 'tukva':
#         for b3 in 'tukva':
#             for b4 in 'tukva':
#                 for b5 in 'tukva':
#                     for b6 in 'tukva':
#                         rez = b1 + b2 + b3 + b4 + b5 +b6
#                         if rez[0] in 'tkv' and rez[-1] in 'tkv':
#                             if rez.count('a') + rez.count("u")==2:
#                                 k+=1
#
# print(k)

# ====================================================================================

# Можно также использовать while

for i in range(1, 100001):
    x = i
    s = 0
    while x>0:
        s +=x%10
        x //=10
    print(i,s)


