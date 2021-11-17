import json

# Создание файла

path = 'C:/Users/eadzh/Documents/QA/Python/lesson_9_dict_json/'
file_name = 'f_json.json'
full_name = path + file_name

dict_item = {
    1: 'Julia',
    2: [1,2,3,4,56],
    3: {'name': 'Vadim', 'age':'32', 'salary':10000}
}

# with open(full_name, 'w') as jf:
#     json.dump(dict_item,jf)

#=======================================================================

# Чтение файла
with open(full_name, 'r') as js:
    json_data = js.read()
    json_odject = json.loads(json_data)

    print('json_data', json_data, type(json_data))
    print('json_object', json_odject, type(json_odject))
