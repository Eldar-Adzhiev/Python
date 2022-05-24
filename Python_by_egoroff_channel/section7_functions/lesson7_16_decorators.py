# 7.16 Декораторы в Python Часть 1

# def decarator(func):
#
#     def inner():
#         print("Start decorator")
#         func()
#         print("End decorator")
#
#     return inner
#
# def say():
#     print('Hello world')
#
# # d = decarator(say)
# # print(d)
# # d()
#
# say = decarator(say)
# print(say)
# say()

# ======================================================================
# Когда функция принемает аргументы

# def decarator(func):
#
#     def inner(name):
#         print("Start decorator")
#         func(name)
#         print("End decorator")
#
#     return inner
#
# def say(name):
#     print('Hello', name)
#
# say = decarator(say)
# print(say)
# say("Eldar")

# ======================================================================
# Когда функция принемает неопределенное колличество аргументов

# def decarator(func):
#
#     def inner(*args, **kwargs):
#         print("Start decorator")
#         func(*args, **kwargs)
#         print("End decorator")
#
#     return inner
#
# def say(name, surname = 'Adzhiev'):
#     print('Hello', name, surname)
#
# say = decarator(say)
# print(say)
# say("Eldar")

# ======================================================================
# Когда функция принемает неопределенное колличество аргументов

def header(func):

    def inner(*args, **kwargs):
        print("<h1>")
        func(*args, **kwargs)
        print("</h1>")

    return inner

def table(func):

    def inner(*args, **kwargs):
        print("<table>")
        func(*args, **kwargs)
        print("</table>")

    return inner


@table
@header # say = table(header(say))
def say(name, surname = 'Adzhiev'):
    print('Hello', name, surname)


# say = table(header(say))
say("Eldar")

# print("==========================================================")

# # say = header(table(say))
# say("Eldar")

















