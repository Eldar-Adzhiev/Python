# 5.3 Цикл for. Обход списков и строк

# Пройтись по списку

a = [43,65,3,54,6,4,2,1,]

# for i in a:
#     print(i)

# Обход по значению
# a = [43,65,3,54,6]
#
# for i in a:
#     print(i, a.index(i))

# Обход по индексам
# n = len(a)
# for i in range(n):
#     print(i, a[i])
#     a[i] += 5
# print(a)

# Исключить все дубли в списке

# a = [1,2,3,4,32,4,5,3,5]
# b = []
#
# for i in a:
#     if not i in b:
#         b.append(i)
# print(b)

# Создавать список четных и не четных выводим на каких индекса лежат

a = [1,2,3,4,32,4,5,3,5]

chet = []
nechet = []

for i in range(len(a)):
    if a[i]%2 ==0:
        chet.append(i)
    else:
        nechet.append(i)
print(chet)
print(nechet)

# Обход строки. Находим большие и маленькие буквы

# s = "hellP world"
#
# for i in s:
#     if i >="a" and i<="z":
#         print(i, "small")
#     elif "A"<=i<="Z":
#         print(i, "big")
#     else:
#         print(i)

# Обход элементов по парам

vowels  = 'aeiou'
s = 'aertiooikjoaklfggfg'
n = len(s)
for i in range(n-1):
    if s[i] in vowels and s [i+1] in vowels:
        print(s[i], s[i+1])

# =======================================================================================

"""Заполняем список
Ваша задача создать список из n строк. Программа сперва будет принимать 
натуральное число n, а затем n строк в каждой отдельной строке. В качестве ответа
выведите получившийся список.

Sample Input 1:
4
Джон
Пол
Ринго
Джордж

Sample Output 1:
['Джон', 'Пол', 'Ринго', 'Джордж']

Sample Input 2:
2
black
white

Sample Output 2:
['black', 'white']"""

n = int(input())

l = []

for i in range(n):
    s = input()
    l.append(s)

print(l)

# ===================================================================================
























