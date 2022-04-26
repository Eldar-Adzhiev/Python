# 5.6 Вложенные списки

# a = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]
# b = ['hello', 'hi', 'world']
#
# print(len(a))
# print(len(a[0]))
# print(a[2][3])

#  Обход всех элементов вложеных списков

a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]

# for i in a:
#     for j in i:
#         print(j, end=' ')
#     print()

#  Обход всех элементов вложеных списков по индексам (по строкам)

# for i in range(3):
#     for j in range(4):
#         print(a[i][j], end=' ')
#     print()

#  Обход всех элементов вложеных списков по индексам (по столбцам)

# for i in range(4):
#     for j in range(3):
#         print(a[i][j], end=' ')
#     print()

# Заполнение вложеных списков

a = []
n = int(input()) #stroka
m = int(input())  #stolb

for i in range(n):
    a.append([0]*m)
for i in a:
    print(i)

for i in range(n):
    b = []
    for i in range(m):
        b.append(int(input()))
    a.append(b)
for i in a:
    print(i)


