# 4.4 Расширение класса в Python

class Person:

    def breathe(self):
        print('Человек дышит')

class Doctor(Person):

    def sleep(self):
        print("Doctor is sleeping")

p = Person()
# p.sleep()
d = Doctor()
d.sleep()















