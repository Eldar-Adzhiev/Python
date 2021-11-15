numbers_list = [1,2,23,4,5,6,7,232]
numbers_list_1 = [1,3,4,5,6,6,75,3]
empty_list = []
next_empty_list = list()
list_in_list = list(numbers_list)
list_item = numbers_list_1 [0] # Выбор элемента из списка список начинается с 0
numbers_list = [7] * 6 # Создаем в листе шесть семерок
numbers_list = list(range(10)) # Создаем список от 0 до 9
numbers_list_1 = list(range(10,30,5))# Cоздаем список от 10 до 29 шагом 5 (10,15,20,25)
numbers_list_2 = list(range(30,10, -1)) #Создаем список от 30 до 11
multi_list = [True, 123,13.5, "Eldar", "123", [123,24], {1: '1'}, (1,2,3,4,5)]

print(multi_list)
for i in multi_list:
    print(i, type(i)) # Итерация списков

for eldar in range(len(multi_list)): ### len - показывает длину списка
    list_item = multi_list[eldar]
    print('eldar =', list_item)

item = 0
while item< len(multi_list):  ### Итерация чрез while
    list_item = multi_list[item]
    print(list_item, type(list_item))
    item +=1


number_list_1 = list(range(5))
number_list_2 = [0,1,2,3,4,5]

print('number_list_1 =', number_list_1)
print('number_list_2 =', number_list_2)

if number_list_1 == number_list_2:
    print(number_list_1 == number_list_2)
else:
    print("not equal")

names = ['Vadim', 'Alexey', 'Julia']

names.pop(2) # delete item with index
names.remove('Vadim') # Delete item with name

names.insert(1, 'Inna')  # Добавляем элемент в список. Точка указывает на местоположение элемента
alex_index = names.index('Alexey') # uznaem index itema
add_item =  ['Elena', 'Misha']
names.append(add_item)

names = names + add_item
names.sort() # Сортировка
print(names)


digits = [1,2,5,63,34,45,765,345345,]

min_digit = min(digits)   # вывести минимум из списка
max_digit = max(digits)   # Вывести максимальное значение из списка

print('Min =', min_digit)
print('Max =', max_digit)