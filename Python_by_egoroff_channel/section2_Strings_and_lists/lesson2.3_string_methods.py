"""Петя записался в кружок по программированию. На первом занятии Пете задали написать простую программу. Программа должна делать
следующее: в заданной строке, которая состоит из прописных и строчных латинских букв, она:
удаляет все гласные буквы,перед каждой согласной буквой ставит символ ".",все прописные согласные буквы заменяет на строчные.
Гласными буквами считаются буквы "A", "O", "Y", "E", "U", "I", а согласными — все остальные.
На вход программе подается ровно одна строка, она должна вернуть результат в виде одной строки, получившейся после обработки."""


# Codeforces

#  Sample Output: .c.d.f.r.c.s

t = input().lower()

t = t.replace("a","")
t = t.replace("o","")
t = t.replace("y","")
t = t.replace("e","")
t = t.replace("u","")
t = t.replace("i","")
t = ".".join(t)

print("."+ t)