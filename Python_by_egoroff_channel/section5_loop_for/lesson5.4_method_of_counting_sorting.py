#  5.4 Метод подсчета. Сортировка подсчетом Python

# Любые числа от 0 до 5. Задача посчитать сколько раз встречается каждая цифра

# a = [0, 1, 2, 3, 2, 1, 3, 3, 2, 4, 3, 5, 3, 2]
#
# count = [0, 0, 0, 0, 0, 0]
#
# for i in a:
#     count[i] += 1
# print(count)
#
# for i in range(6):
#     if count[i]>0:
#         print(i, count[i])

# ======================================================================================

# s = "abczjhdf HG jgkfyGg jhgkdf 543 *(^($&*#"
#
# letters = [0]*26
#
# for i in s.lower():
#     if i>='a' and i<='z':
#         nomer = ord(i) - 97
#         letters[nomer] +=1
#
# for i in range(26):
#     if letters[i]>0:
#         print(chr(i+97)*letters[i], end='')

# =======================================================================================

a = []

import random

for i in range(10):
    a.append(random.randint(-10, 10))

count = [0] * 21

for i in a:
    count[i + 10] += 1
print(a)
for i in range(21):
    if count[i] > 0:
        print(i - 10, count[i])
