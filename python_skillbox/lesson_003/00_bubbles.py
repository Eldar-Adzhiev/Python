# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(100, 100)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг


def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)


point = sd.get_point(300, 300)
bubble(point=point, step=10)

# Нарисовать 10 пузырьков в ряд
for i in range(100, 1000, 100):
    point = sd.get_point(i, 100)
    bubble(point=point, step=10)
# Нарисовать три ряда по 10 пузырьков
for x in range(100, 301, 100):
    for y in range(100, 1001, 100):
        point = sd.get_point(y, x)
        bubble(point=point, step=10)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    bubble(point=point, step=step)

sd.pause()
