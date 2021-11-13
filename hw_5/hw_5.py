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
import random

list_random = random.sample(range(100),70)
print(list_random)

# Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его списки по 5 элементов.
def chunkedList (list_name, chunked_size):
    chunked_list = list()
    for i in range(0, len(list_name), chunked_size):
        chunked_list.append(list_name[i:i + chunked_size])
    print(chunked_list)


chunkedList(list_random,5)

# Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка, список чётных и список нечётных чисел.
