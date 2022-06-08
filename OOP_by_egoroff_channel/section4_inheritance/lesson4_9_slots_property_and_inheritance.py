# 4.9 Slots: свойства(property) и наследования

class Rectangle:
    __slots__ = 'width', 'height'

    def __init__(self,a,b):
        self.width = a
        self.height = b

    @property
    def perimetr(self):
        return (self.width + self.height)*2

    @property
    def area(self):
        return self.height + self.width

class Square(Rectangle):
    __slots__ = 'color'
    
    def __init__(self, a, b,color):
        super(Square, self).__init__(a, b)
        self.color = color


















