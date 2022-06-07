# 4.6 Множественное наследование


# class Doctor:
#
#     def can_cure(self):
#         print('im Doctor i can cure')
#
# class Builder:
#
#     def can_build(self):
#         print('im Builder i can build')
#
# class Person(Doctor, Builder):
#     pass
#
# s = Person()
# s.can_cure()
# s.can_build()

# ==========================================================================

# class Doctor:
#
#     def can_cure(self):
#         print('im Doctor i can cure')
#
#     def can_build(self):
#         print('im Doctor i can build')
#
# class Builder:
#
#     def can_build(self):
#         print('im Builder i can build')
#
# class Person(Doctor, Builder):
#     pass
#
# print(Person.__mro__)
# s = Person()
# s.can_cure()
# s.can_build()

# ==========================================================================

# class Doctor:
#
#     def graduate(self):
#         print('Ура, я отучился на доктора')
#
#     def can_build(self):
#         print('im Doctor i can build')
#
# class Builder:
#
#     def graduate(self):
#         print('Ура, я отучился на Строителя')
#
#     def can_build(self):
#         print('im Builder i can build')
#
# class Person(Builder, Doctor):
#     def graduate(self):
#         print('Посмотрим кем я стал')
#         super().graduate()
#         Doctor.graduate(self)
#
# print(Person.__mro__)
# s = Person()
# s.graduate()

# ==========================================================================

class Doctor:

    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print('Ура, я отучился на доктора')

    def can_build(self):
        print('im Doctor i can build')

class Builder:

    def __init__(self, rank):
        self.rank = rank

    def graduate(self):
        print('Ура, я отучился на Строителя')

    def can_build(self):
        print('im Builder i can build')

class Person(Builder, Doctor):

    def __init__(self, rank, degree):
        super().__init__(rank)
        Doctor.__init__(self, degree)

    def __str__(self):
        return f"Person {self.rank} {self.degree}"

print(Person.__mro__)
s = Person(5, 'spec')
print(s)
















