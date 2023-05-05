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
        for char, cnt in sorted(self.char_dict.items(), key=lambda item: item[1]):
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


# read_file = CharStat(file_path, 'voyna-i-mir.txt')
# read_file.char_stat()


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


# ==============================================================================================================


"""Реализация с github"""

# import zipfile
# import os
# from termcolor import cprint
#
# class CharStat:
#     def __init__(self, path_to_file=None, path_to_archive=None, filename_in_archive=None):
#         self.stat = {}
#         self.is_data_ready = False
#
#         if path_to_file:
#             self.path_to_file = path_to_file
#             if self.check_path_to_file():
#                 self.file_name = os.path.basename(path_to_file)
#                 self.is_data_ready = True
#         else:
#             self.path_to_archive = path_to_archive
#             self.filename_in_archive = filename_in_archive
#             if path_to_archive or filename_in_archive:
#                 if self.check_archive():
#                     self.zfile = None
#                     self.path_to_file = path_to_archive
#                     self.file_name = filename_in_archive
#                     self.unzip()
#                     self.is_data_ready = True
#             else:
#                 cprint('Файл не найден', color='red')
#
#         if self.is_data_ready:
#             print('Данные готовы к обработке.')
#         else:
#             cprint('Не удалдось подготовить данные к обработке.', color='red')
#
#     def check_path_to_file(self):
#         if self.path_to_file:
#             if os.path.isfile(self.path_to_file):
#                 cprint(f'Обработка файла {self.path_to_file}!', color='cyan')
#                 return True
#             else:
#                 cprint('Файл не найден!', color='red')
#         else:
#             cprint('Не указан файл для анализа из архива!', color='red')
#         return False
#
#     def check_archive(self):
#         if self.path_to_archive:
#             if zipfile.is_zipfile(self.path_to_archive):
#                 if not self.filename_in_archive:
#                     cprint('Не указан файл для анализа из архива!', color='red')
#                 else:
#                     fn = os.path.join(os.path.dirname(self.path_to_archive), self.filename_in_archive)
#                     cprint(f'Обработка файла {fn}!', color='cyan')
#                     return True
#             else:
#                 cprint(f'Указанный файл {path_to_archive} не архив !', color='red')
#         else:
#             cprint('Не указан путь к архиву!', color='red')
#
#         return False
#
#     def find_file(self, name):
#         for filename in self.zfile.namelist():
#             if name == filename:
#                 return True
#             else:
#                 return False
#
#     def unzip(self):
#         self.zfile = zipfile.ZipFile(self.path_to_file, 'r')
#         if self.find_file(os.path.join(os.path.dirname(self.path_to_file), self.file_name)):
#             os.remove(os.path.join(os.path.dirname(self.path_to_file), self.file_name))
#         self.zfile.extractall(os.path.dirname(self.path_to_file))
#
#     def print_header(self):
#         print(f'')
#         print('+', f'{chr(45):-^9}', '+', f'{chr(45):-^10}', '+', sep='')
#         print('|', '  Буква  ', '|', '  Кол-во  ', '|', sep='')
#         print('+', f'{chr(45):-^9}', '+', f'{chr(45):-^10}', '+', sep='')
#
#     def print_result(self):
#         print('+', f'{chr(45):-^9}', '+', f'{chr(45):-^10}', '+', sep='')
#         print('|', '  Итого  ', '|', f'{sum(self.stat.values()): ^10}', '|', sep='')
#         print('+', f'{chr(45):-^9}', '+', f'{chr(45):-^10}', '+', sep='')
#
#     def print_body(self):
#
#         for char, cnt in sorted(self.stat.items()):
#             print('|', f'{char: ^9}', '|', f'{cnt: ^10}', '|', sep='')
#
#     def print_stat(self):
#         if self.is_data_ready:
#             if not self.stat:
#                 self.get_stat()
#
#             self.print_header()
#             self.print_body()
#             self.print_result()
#
#     def get_stat(self):
#         if self.is_data_ready:
#             with open(os.path.join(os.path.dirname(self.path_to_file), self.file_name), mode='r',
#                       encoding='CP1251') as file:
#                 for line in file:
#                     for char in line:
#                         if char.isalpha():
#                             self.stat[char] = self.stat.setdefault(char, 0) + 1
#             return self.stat
#
#
# if __name__ == '__main__':
#     src_file_path = './python_snippets/voyna-i-mir.txt'
#     path_to_archive = './python_snippets/voyna-i-mir.txt.zip'
#     filename_in_archive = 'voyna-i-mir.txt'
#
#     war_and_peace = CharStat(path_to_file=src_file_path,
#                              path_to_archive=path_to_archive,
#                              filename_in_archive=filename_in_archive)
#
#     war_and_peace.print_stat()

# ==============================================================================================================

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

from abc import ABC, abstractmethod


class BaseCharStat(ABC):

    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name
        self.char_dict = {}

    @abstractmethod
    def sort(self):
        """ Method for sorted by letters"""
        pass

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
        for char, cnt in self.sort():
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


class SortCharByKeys(BaseCharStat):

    def sort(self):
        return sorted(self.char_dict.items())


class SortCharByValueASC(BaseCharStat):

    def sort(self):
        return sorted(self.char_dict.items(), key=lambda item: item[1])


class SortCharByValueDESC(BaseCharStat):

    def sort(self):
        return sorted(self.char_dict.items(), key=lambda item: item[1], reverse=True)


if __name__ == '__main__':
    file_path = Path("python_snippets/voyna-i-mir.txt.zip").resolve()
    a = SortCharByValueDESC(file_path, 'voyna-i-mir.txt')
    a.char_stat()
