# 9.2 Работаем с JSON в Python. Парсинг JSON, сохраняем JSON в файл
import json

# str_json = '''{
#     "response": {
#         "count": 32363,
#         "items": [{
#                 "id": 287350527,
#                 "first_name": "Sonya",
#                 "last_name": "Kargina",
#                 "photo_50": "https://pp.vk.me/c421526/v421526527/b2c1/J2EL--qCZa8.jpg"},
#
#                 {"id": 341523166,
#                 "first_name": "Slava",
#                 "last_name": "Kholod",
#                 "photo_50": "https://pp.vk.me/c630619/v630619166/3e321/eTxKNQSJMuk.jpg"
#             }]}}'''
# print(type(str_json))

# data = json.loads(str_json)
# print(type(data))
# print(data)
# print(data['response'])
# print(data['response']['count'])

# for item in data['response']['items']:
#     del item['id'] # Удаляем ключ  id
#     item['likes'] = 0 # Создаем новый ключ
# print(data['response']['items'])

# Создаем новый json
# new_json = json.dumps(data, indent=2 )
# print(new_json)

# Сохраняем в фаил

# with open('test_json.json', 'w') as file:
#     json.dump(data, file, indent=3)


# Парсим json из файла

with open('test_json.json', 'r') as file:
    data = json.load(file)

print(data)
print(type(data))