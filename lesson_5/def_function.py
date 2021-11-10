import names  ### Импортировали библиотеку которая поможет генерировать случайные имена.
import randomtimestamp as rd ### Импортировали библиотеку которая поможет генерировать даты.
# Что бы не писать длинное имя через  "as"  назвали его  "rd"
import random

def function_name (a, b):  # Создание функции
    result = a + 100
    result_2 = b + 1000

    print("Hello my first function")
    print("result =",result )
    print("result_2", result_2)

# function_name() ## Вызов функции

def function_name2(name, b_date ):
    result = name + " was born in " + str(b_date)
    print(result)

for i in range (0, 10):
    user_name = names.get_full_name() # Генерируем имена
    gen_date = rd.random_date()

    function_name2(user_name, gen_date)

def gen_weight():
    weight = random.randint(35,100)
    return weight

for i in range(10):
    u_weight = gen_weight()
    print("your weight = ", u_weight)





