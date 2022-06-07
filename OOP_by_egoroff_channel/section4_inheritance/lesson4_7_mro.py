# 4.7 MRO - порядок разрешения методов

class A:
    def hello(self):
        print('hello from A')

class B:
    def hello(self):
        print('hello from B')

class C(A, B):
    pass


C().hello()
print(C.__mro__)