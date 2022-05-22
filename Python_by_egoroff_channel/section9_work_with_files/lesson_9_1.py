# 9.1 Чтение и запись данных. Функция open

file = open('test_file.txt', encoding='utf-8')
# print(file.read())  # read - Cчитывает весь фаил целиком
# print(file.read(10)) # Считывает первые 10 символов
# print(file.read(10)) # Следующие 10 символов
# file.seek(0) # Передвигает курсор в начало
# print(file.read(10)) # Считывает первые 10 символов
# print(file.readline())

# Выведем весь текст с помошью цикла for
# for row in file:
#     print(row)

# Выведем весь текст по буквам
# for row in file:
#     for letter in row:
#         print(letter)

# s = file.readlines()
# print(s)
file.close()

# Запись данных в фаил - w - удаляет записи и пишет по новой

file = open('test_file.txt', 'w',  encoding='utf-8')
file.write('Hello')
print()

# a - апдеит файла
file = open('test_file.txt', 'a',  encoding='utf-8')
file.write('\nHello')
print()
file.close()

# Режим а+ поддерживает и запись и чтение файла
file = open('test_file.txt', 'a+',  encoding='utf-8')
file.write('\nHello')
print(file.read())




