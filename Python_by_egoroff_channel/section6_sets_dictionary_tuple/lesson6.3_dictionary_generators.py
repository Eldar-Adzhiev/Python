# 6.3 Генераторы словарей

# d = {i: i**2 for i in range(1,11)}

# d = {}
# for i in range(1, 11):
#     d[i] = i**2
#
# print(d)

# ==================================================================

# d = {word: len(word) for word in ['hello', 'hi', 'www']}
#
# print(d)

# ============================================================

data = {
    "Джефф Безос": "177",
    "ИлоН Маск": "126",
    "бернар АрноО": "150",
    "БиЛл Гейтс": "124"
}

# new_data = {key.title(): int(value) for key, value in data. items()}

# new_data = {}
#
# for key, value in data.items():
#     new_data[key.title()] = int(value)
# print(data)
# print(new_data)

# ====================================================================

users = [
    [0, "Bob", "password"],
    [1, "code", "python"],
    [2, "Stack", "overflow"],
    [3, "username", "1234"],
    [51, "qwerty", "1234"]
]

new_users = {user[0]: user for user in users}
print(new_users)


