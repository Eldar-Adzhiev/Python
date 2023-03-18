# Регулярные выражения #2: квантификаторы {m,n}, +, * , ?

import re

"""
{m, n}
m - минимальное число совпадений с выражение
n - максимальное число совпадений с выражением
"""
text = "Google, Gooogle, Goooooogle"
match = re.findall(r"o{2,5}", text)

print(match)

# Минирный режим

text = "Google, Gooogle, Goooooogle"
match = re.findall(r"o{2,5}?", text)

print(match)

#===================================================================

# Краткие формы записи квантификаторов
"""
{m} - повторение выражения ровно m раз = {m,n}
{m,} - повторение от m и более раз
{,n} - повторение не более n раз

минорный режим
m,}?
{,n}? 
"""

text = "Google, Gooogle, Goooooogle"
match = re.findall(r"Go{2,}gle", text)

print(match)

#---------------------

text = "Google, Gooogle, Goooooogle"
match = re.findall(r"Go{,4}gle", text)

print(match)

# ----------------

phone = "89181234567"
match = re.findall(r"8\d{10}", phone)
print(match)

#===================================================================

"""
{0,} - от нуля и до бесконечности
{1,} - от 1 и до бесконечности
?  - от нуля до одного = {0,1}
* - от нуля и до бесконечности
+ - от 1 и до бесконечности
"""


text = "стеклянный, стекляный"
match = re.findall(r"стеклянн?ый", text)

print(match)

text = "стеклянный, стекляный"
match = re.findall(r"стеклянный", text)

print(match)

