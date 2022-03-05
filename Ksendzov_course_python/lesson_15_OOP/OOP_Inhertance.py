class Animal:
    def make_a_sound(self):
        print("AAuuuFFF!!!")

class Cat(Animal):
    def tgdk(self):
        print("tgdk-tgdk-tgdk")

    #redefinition
    def make_a_sound(self):
        print('Meayyy')


# murzik = Cat()
#
# murzik.tgdk()
# murzik.make_a_sound()

#------------------------

class Table():
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h

class DeskTable(Table):
    def square(self):
        return self.width * self.length

t1 = DeskTable(1.5, 0.8, 1.5)
print(t1.square())

class ComputerTable(DeskTable):
    def square(self, monitor=0.0):
        return self.width * self.length - monitor

t2 = ComputerTable(1.5, 0.8, 1.5)
print(t2.square(0.4))

class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        self.length = l
        self.width = w
        self.height = h
        self.places = p

    def params(self):
        print('length', self.length)
        print('width', self.width)
        print('height', self.height)
        print('places', self.places)


class KitchenTable2(Table):
    def __init__(self, l, w, h, p):
        Table.__init__(self, l, w, h)
        self.places = p

    def params(self):
        print('length', self.length)
        print('width', self.width)
        print('height', self.height)
        print('places', self.places)

t3 = KitchenTable(1.5, 0.8, 1.5, 5)
t4 = KitchenTable2(1.5, 0.8, 1.5, 4)

t3.params()
print('-------------------')
t4.params()