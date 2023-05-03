# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile
from pathlib import Path
from pprint import pprint

file_path = Path("python_snippets/voyna-i-mir.txt.zip").resolve()

# zip_file = zipfile.ZipFile(file_path)
# print([text_file.filename for text_file in zip_file.infolist()])
#
# def unzip_file(file_path):
#     with zipfile.ZipFile(file_path) as myzip:
#         with myzip.open('voyna-i-mir.txt') as file:
#             for line in file.read().decode('cp1251'):
#                 print(line)
#
# unzip_file(file_path)


# def read_file_from_zip_archive(file_path, file_name):
#     with zipfile.ZipFile(file_path) as myzip:
#         with myzip.open(file_name) as file:
#             for char in file.read().decode('cp1251'):
#                 print(char)

def read_file_from_zip_archive(file_path, file_name):
    char_dict = {}
    with zipfile.ZipFile(file_path) as myzip:
        with myzip.open(file_name) as file:
            for char in file.read().decode('cp1251'):
                if char.isalpha():
                    if char in char_dict:
                        char_dict[char] += 1
                    else:
                        char_dict[char] = 1
    pprint(f'+{"":-^12}+{"":-^11}+')
    pprint(f"| {'Буква':^10} | {'Частота':^9} |")
    pprint(f'+{"":-^12}+{"":-^11}+')
    for key in char_dict.keys():
        pprint(f"| {key:^10} | {char_dict[key]:^10}|")
    pprint(f'+{"":-^12}+{"":-^11}+')

    value_count = 0
    for value in char_dict.values():
        value_count += value
    pprint(f"| {'Итого':^10} | {value_count:^10}|")




read_file_from_zip_archive(file_path, 'voyna-i-mir.txt')

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
