# Сделать функцию которая на вход принимает год и определяет высокосный или нет

def year():
    a = int(input('Input year'))
    if a % 4 == 0:
        print('Visokosniy')
    else:
        print("Ne visokosniy")

year()