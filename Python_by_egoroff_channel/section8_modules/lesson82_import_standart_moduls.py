# 8.2 Импорт стандартных модулей

import pprint
# import math as m
# from math import e, pi, factorial
# from math import *  # импорт все функции модуля маз

def say_hello(name):
    print(f'Hello,{name}')


def summa(*args):
    return sum(args)


def factorial(n):
    pr = 1
    for i in range(1, n+1):
        pr += 1
    return pr

my_str = "YOU'RE BREATHTAKING"
my_num1 =2
my_num2 = 3

# pprint.pprint(locals())
# pprint.pprint(dir(m))
# pprint.pprint(p)























