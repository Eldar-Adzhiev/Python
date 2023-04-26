#  сохраняющие скобки и группировка

import re

text = "lat=5, lon=7"

match = re.findall(r"\w+\s*=\s*\d+", text)
print(match)

#===================================================================
"""
Если хотим найти определенные ключи
"""
text = "lat=5, lon=7, a=5"

match = re.findall(r"lat\s*=\s*\d+|lon\s*=\s*\d+", text)
print(match)


match = re.findall(r"(?:lat|lon)\s*=\s*\d+", text) # ?: - Без сохранения ключа
print(match)

match = re.findall(r"(lat|lon)\s*=\s*\d+", text) # - Сохранения первого уровня
print(match)

match = re.findall(r"((lat|lon)\s*=\s*\d+)", text) #  - Сохранения двойного уровня
print(match)

#===================================================================
"""
Отдельно сохраним ключи и значения
"""

match = re.findall(r"(lat|lon)\s*=\s*(\d+)", text)
print(match)

match = re.findall(r"(lat|lon)\s*=\s*(?:\d+)", text) # Список ключей
print(match)

#===================================================================
"""

"""
text = "<p> Картинка <img src='bg.jpg'> в тексте</p>"

match = re.findall(r"<img\s+[^>]*src=[\"'](.+?)[\"']", text)
print(match)

text = "<p> Картинка <img src='bg.jpg'> в тексте</p>"

match = re.findall(r"<img\s+[^>]*src=([\"'])(.+?)\1", text) # \i - (i натуральное число)
print(match)

#===================================================================
"""
Обращение по имени
"""
text = "<p> Картинка <img src='bg.jpg'> в тексте</p>"

match = re.findall(r"<img\s+[^>]*src=(?P<q>[\"'])(.+?)(?P=q)", text) # (?P<name>) ... (?P=name)
print(match)