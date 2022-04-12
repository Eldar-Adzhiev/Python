# 4.3 Обход всех цифр числа с помощью while

# number = 73408
# m = 0
# s = 0
# while number > 0:
#     last_digit = number % 10
#     s = s + last_digit
#     if last_digit > m:
#         m = last_digit
#     number = number // 10
# print(s + m)


# =====================================================================

# number = 1234567890
# count = 0
# while number > 0:
#     last_digit = number % 10
#     if last_digit < 3:
#         count = count + 1
#     number = number // 10
# print(count)

# =====================================================================

"""Программа принимает на вход одно натуральное число и выводит
его цифры в столбик в обратном порядке."""

number = int(input())

while number > 0:
    last_digit = number % 10
    print(last_digit)
    number = number //10

# =========================================================================

"""Программа принимает на вход одно натуральное число и выводит на
экран сумму цифр данного числа"""

number = int(input())

s = 0
while number > 0:
    last_digit = number % 10
    s += last_digit
    number = number //10

print(s)


