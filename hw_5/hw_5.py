# # Написать скрипт который в создаст список целых чисел.
list_1 = list(range(71))
# print(list_1)
#
# #Написать скрипт который в создаст список целых чётных чисел.
# list_2 = list(range(0,71,2))
# print(list_2)
#
# #Написать скрипт который в создаст список целых нечётных чисел.
# list_3 = list(range(1,71,2))
# print(list_3)

#Написать скрипт который из списка целых чисел выведет чётные числа.
# list = []
# for i in list_1:
#     if i % 2==0:
#         list.append(i)
# print(list)

#Написать скрипт который из списка целых чисел выведет нечётные числа.
# list = []
# for i in list_1:
#     if i % 2==1:
#         list.append(i)
# print(list)

#Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.
# list = []
# for i in list_1:
#     if i % 5 == 0:
#         list.append(i)
# print(list)

# Написать скрипт который из списка целых чисел выведет количество чётных чисел которые делятся на 5 без остатка.
# list = []
# for i in list_1:
#     if i % 5 == 0:
#         list.append(i)
# print(len(list))

# Написать скрипт который в создаст список целых рандомных чисел.
# import random
#
# list_random = random.sample(range(100),70)
# print(list_random)

# Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его списки по 5 элементов.
# def chunkedList (list_name, chunked_size):
#     chunked_list = list()
#     for i in range(0, len(list_name), chunked_size):
#         chunked_list.append(list_name[i:i + chunked_size])
#     print(chunked_list)
#
#
# chunkedList(list_random,5)

# Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка, список чётных и список нечётных чисел.
# def output_of_even_and_odd_numbers(list_name):
#     list_of_odd_numbers = []
#     for i in list_name:
#         if i % 2==1:
#             list_of_odd_numbers.append(i)
#     print(list_of_odd_numbers)
#     list_of_even_numbers = []
#     for k in list_name:
#         if k % 2==0:
#             list_of_even_numbers.append(k)
#     print(list_of_even_numbers)
#
#
# output_of_even_and_odd_numbers(list_1)

# Написать скрипт который сгенерирует список под названием 5_stars из списков по 5 элементов целых чисел.
# list_for_stars_1 = [1,3,34,5,2]
# list_for_stars_2 = [91,7,62,4,87]
# stars_5 = []
# stars_5.append(list_for_stars_1)
# stars_5.append(list_for_stars_2)
# print(stars_5)

# Написать скрипт который выведет список из сумм каждого внутреннего списка из  5_stars

# result_sum_lists_of_list = []
# for list_number in stars_5:
#     result_sum_lists_of_list.append(sum(list_number))
#
# print(result_sum_lists_of_list)


# 13) Написать функцию которая на вход получает список 5_stars, а вернёт 2 списка.
# В одном списке внутренние списки из 5_stars сумма чисел которых >= 100,
# а другой сумма чисел которых < 100. Если какого-то списка не получится, то вместо него вернуть текст “No lists”

stars_5 = [[5,12,45,2,4],[1,23,4,66,7], [1,2,3,4,5]]

def star_5(list_name):
    list1 = []
    list2 = []





star_5(stars_5)


