# 5.9 Генераторы списков Python | List comprehension

# [выражение for val in коллекция]
# [выражение for val in коллекция if условие]

a = [2 for i in range(10)]
print(a)

a = [(i,j,k) for i in 'abc' for j in [1,2,3] for k in "@#$"]
print(a)
