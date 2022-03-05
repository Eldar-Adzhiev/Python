# name = input('What is your name?')
# print('Hello ', name)

# Сделать функицию которая спросит первую букву, спросит колличество (целочисло)
# необходимо создать список которое выведет эту букву по списку столько раз сколько было целое число
e = []
def function():

    a = input('first letter')
    b = int(input('number'))

    for i in range(b):
        e.append(a+str(b))
    return e

print(function())

# Создать файл и внести в него список который создает функция

file = 'C:/Users/eadzh/Documents/QA/Python/lesson_10_practice/1.txt'

with open(file, 'w') as f:
    writer = f.writelines('\n'.join(e))