# 5.3 Обработка исключений try-except

try:
    a + b
    int('hello')
    1/0
except ZeroDivisionError:
    print('Чувак ты делишь на ноль')
except ValueError:
    print('ValueError')
except NameError:
    print('NameError')

# ==============================================================================

a = 'hello'
d = {}

try:
    4 +2
except Exception:
    print('Выполнилась обработка ')
else:
    print('else выполняется если не произошло исключение в try')
finally:
    print('finally выполняется вегда')

"""
try - можно использовать с множеством исключений котрые вы отлавливаете
так же может иметь блоки else и finally которые используются только один раз
"""

