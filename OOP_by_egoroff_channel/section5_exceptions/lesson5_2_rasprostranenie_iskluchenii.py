# 5.2 Распространение исключений

# def third():
#     print('start third')
#     try:
#         1/0
#     except ZeroDivisionError:
#         print('Обработалось исключение ZeroDivisionError')
#     print('finish third')
#
# def second():
#     print('start second')
#     third()
#     print('finish second')
#
# def first():
#     print('start first')
#     second()
#     print('finish first')
#
#
# print('hello')
# first()

# ==============================================================================

def third():
    print('start third')
    1/0
    print('finish third')

def second():
    print('start second')
    third()
    print('finish second')

def first():
    print('start first')
    try:
        second()
    except ZeroDivisionError:
        print('Обработалось исключение ZeroDivisionError')
    print('finish first')


print('hello')
first()

