# 5.4 Инструкция raise

raise exception

try:
    [1,2,3][15]
except (KeyError, IndexError) as error:
    print('LoolupError')
    print(f'Logging erroe: {repr(error)}')
except ZeroDivisionError as err:
    print('ZeroDivisionError')
    print(f'Logging error: {err} {repr(err)}')