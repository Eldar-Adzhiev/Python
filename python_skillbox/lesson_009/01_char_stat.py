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


class CharStat:

    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name
        self.char_dict = {}

    def _unzip_file(self):
        with zipfile.ZipFile(self.file_path) as myzip:
            myzip.extract(self.file_name)

    def _count_of_letters(self):
        with open(self.file_name, encoding='1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.char_dict:
                            self.char_dict[char] += 1
                        else:
                            self.char_dict[char] = 1

    def _print_header(self):
        print(f'')
        print('+', f'{chr(45):-^9}', '+', f'{chr(45):-^10}', '+', sep='')
        print('|', '  Буква  ', '|', '  Кол-во  ', '|', sep='')
        print('+', f'{chr(45):-^9}', '+', f'{chr(45):-^10}', '+', sep='')

    def _print_body(self):
        for char, cnt in sorted(self.char_dict.items()):
            print('|', f'{char: ^9}', '|', f'{cnt: ^10}', '|', sep='')

    def _print_result(self):
        print('+', f'{chr(45):-^9}', '+', f'{chr(45):-^10}', '+', sep='')
        print('|', '  Итого  ', '|', f'{sum(self.char_dict.values()): ^10}', '|', sep='')
        print('+', f'{chr(45):-^9}', '+', f'{chr(45):-^10}', '+', sep='')

    def char_stat(self):
        self._unzip_file()
        self._count_of_letters()
        self._print_header()
        self._print_body()
        self._print_result()

read_file = CharStat(file_path, 'voyna-i-mir.txt')
read_file.char_stat()



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

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
