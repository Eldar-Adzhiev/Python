

class car:

    color = 'red'
    form = 'sedan'
    engine = '3'
    speed = 100

    def moove(self, speed):
        self.speed = speed

    def changecolor(self, color):
        self.color = color



obj1 = car()
obj2 = car()

print('color = ', obj1.color)
print('form = ', obj1.form)
print('engine = ', obj1.engine)
print('speed = ', obj1.speed)

print('----------------------------------')

print('2_color = ', obj2.color)
print('2_form = ', obj2.form)
print('2_engine = ', obj2.engine)
print('2_speed = ', obj2.speed)

print('----------------------------------')

obj1.moove(50)
obj1.changecolor('black')
print('odj1_change_speed = ', obj1.speed)
print('odj1_change_color = ', obj1.color)

print('----------------------------------')

obj2.moove(70)
print('odj1_change_speed = ', obj2.speed)