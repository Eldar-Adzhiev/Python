# Создать текстовый файл (Для этог нам нужно знать путь где будет лежать файл)

# file_path = 'C:/Users/eadzh/Documents/QA/Python/lesson_7_Python_Files_txt_csv/'
# file_name = 'txt_lesson_7.txt'
# file_path_name = file_path + file_name

# print(file_path_name)
#
# f = open(file_path_name, 'w')
# f.write('Hello \nguys')
# f.close()

# with open(file_path_name, 'w') as txt_files: # 'w' - все время перезаписывает файл все время
#     name = 'Eldar '
#     surname = 'Adzhiev'
#     full_name = name + surname
#
#     txt_files.write(full_name)

# with open(file_path_name, 'a') as txt_files:  # 'a' - добавляет надписи в файл
#     name = '\nAlexey '
#     surname = 'Borisovec'
#     full_name = name + surname
#
#     txt_files.write(full_name)

#============================================================================

# Через input !!!!
# with open(file_path_name, 'w') as txt_files:
#     name = input('name: ')
#     surname = input('surname: ')
#     full_name = name +'\n' + surname
#
#     txt_files.write(full_name)

#============================================================================

#  КАК  ПИСАТЬ ТЕКСТ В ФАЙЛЫ ЕСЛИ ЕСТЬ СПИСОК СЛОВ  К ПРИМЕРУ СПИСОК ИМЕН!
file_path = 'C:/Users/eadzh/Documents/QA/Python/lesson_7_Python_Files_txt_csv/'
file_name = 'txt_lesson_7.txt'
file_path_name = file_path + file_name

names_list = ['Julia', 'Alina', 'lyana', 'Dmitry']

# with open(file_path_name, 'w') as txt_files:
#     for i in names_list:
#
#         txt_files.write(i)
#         txt_files.write('\n')

# with open(file_path_name, 'w') as txt_files: # Тоже самое только без for
#
#     txt_files.write('\n'.join(names_list)

#============================================================================

# ПРОЧИТАТЬ ФАЙЛ

with open(file_path_name, 'r') as txt_files:

    read_file = txt_files.readlines()

    for i in read_file:
        print(i.rstrip()) # rstrip - глушит пустые строки


