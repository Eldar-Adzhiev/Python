# 1) Создать 2 переменных типа String с разными значениями
a = "eldar"
b = "adzhiev"

# 2) Создать 4 переменных типа Integer с разными значениями
new_int = 12
new2_int = 32
new3_int = 17
new4_int = 56

# 3) Создать 3 переменных типа Float с разными значениями
new_float = 64.4
new2_float = 77.13
new3_float =732.6

# 4) Реализовать 15 варианта сравнения int переменных с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.
if new_int > new2_int:
    print('new_int')
else:
    print('new2_int')

if new_int < new3_int:
    print('new_int')
else:
    print('new3_int')

if new_int >= new4_int:
    print('new_int')
else:
    print('False')

if new_int <= new4_int:
    print('True')
else:
    print('False')

if new_int != new4_int:
    print('True')
else:
    print('False')

if new2_int > new3_int:
    print('new2_int')
else:
    print('new2_int')

if new2_int < new3_int:
    print('new2_int')
else:
    print('new3_int')

if new2_int >= new4_int:
    print('new2_int')
else:
    print('new4_int')

if new2_int <= new4_int:
    print('new2_int')
else:
    print('new4_int')

if new2_int != new4_int:
    print('new2_int')
else:
    print('new4_int')

if new3_int >= new4_int:
    print('new3_int')
else:
    print('new4_int')

if new3_int <= new4_int:
    print('new3_int')
else:
    print('new4_int')

if new3_int != new4_int:
    print('new3_int')
else:
    print('new4_int')

if new3_int > new4_int:
    print('new3_int')
else:
    print('new4_int')

if new3_int < new4_int:
    print('new3_int')
else:
    print('new4_int')

# 5) Реализовать 9 варианта сравнения Float переменных с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.

if new_float > new2_float:
    print('new_float')
else:
    print('new2_float')

if new_float < new2_float:
    print('new_float')
else:
    print('new2_float')

if new_float >= new2_float:
    print('new_float')
else:
    print('new2_float')

if new_float <= new2_float:
    print('new_float')
else:
    print('new2_float')

if new_float != new2_float:
    print('new_float')
else:
    print('new2_float')

if new2_float > new3_float:
    print('new2_float')
else:
    print('new3_float')

if new2_float < new3_float:
    print('new2_float')
else:
    print('new3_float')

if new2_float >= new3_float:
    print('new2_float')
else:
    print('new3_float')

if new2_float <= new3_float:
    print('new2_float')
else:
    print('new3_float')

# 6) Реализовать 10 варианта сравнения int переменных с операторами >, <, >=, <=, != и условными выражениями (end, or, not). Pезультаты весвести в консоль.

if new_int > 0  and new3_int < 100:
    c = new_int + new3_int
    print(c)
else:
    print('false')

if new_int >= 0 or new2_int <= 13:
    sum_new_and_new2 = new2_int + new_int
    print(sum_new_and_new2)
else:
    print('false')

if new_int < new2_int and new2_int > new3_int or (not new4_int > new_int):
    sum_new = new_int + new2_int + new3_int + new4_int
    print(sum_new)

if new_int > new2_int and new2_int > new3_int and new3_int > new4_int:
    print('true')
else:
    print('false')

