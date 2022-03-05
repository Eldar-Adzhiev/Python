# 1) Создать переменную типа string
a = "Name"

# 2) Создать переменную типа Integer
b = 28

# 3) Создать переменную типа Float
c = 28.6

# 4) Создать переменную типа Bytes
d = b'byte'
print(d)
print(type(d))

# 5) Cоздать переменную типа List
e = ['apple', 'dog', 32]
print(e)
print(type(e))

# 6) Cоздать переменную типа Tuple
thisTuple = ("abc", 32, True)
print (thisTuple)
print(type(thisTuple))

# 7) Создать переменную Set
thisSet = {"qwe", 32, False}
print(thisSet)
print(type(thisSet))

# 8) Создать переменную Frozen Set
thisFrozenSet = frozenset({"qwer", 123, True})
print(thisFrozenSet)
print(type(thisFrozenSet))

# # 9) Создать переменную Dict
thisDict = {"name": "Eldar", "age": "28"}
print(thisDict)
print(type(thisDict))

10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных
print(a,b,c,d,e,thisTuple, thisSet, thisFrozenSet, thisDict)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(thisTuple))
print(type(thisSet))
print(type(thisFrozenSet))
print(type(thisDict))

11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
name = "Eldar"
secondname = "Adzhiev"
print(name + " " + secondname)

12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
a = 12
b = 4
n = a + b
print(n)

# 13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
k = a / b
print(k)

# 14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
z = a*b
print(z)

 # 15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
x = a // b
print(x)

# 16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.
i = 13
r = 3
g = i/r
print(int(g))
