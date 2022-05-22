# 8.3 Импорт собственных модулей в Python

import lesson82_import_standart_moduls

from lesson82_import_standart_moduls import say_hello

print(lesson82_import_standart_moduls.factorial(10))

say_hello('Eldar')

print(__name__)


# Koд который выполняется только при запуске данного модуля
if __name__ == '__main__':
    print(123)
    print('hello')