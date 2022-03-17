class Person:
    def __init__(self, name, surname, qualification = 1):
        self.name = name
        self.surname = surname
        self.qualification = qualification


    def info(self):
        try:
            return self.name, \
                   self.surname, \
                   self.qualification
        except:
            print("No info")

    def __del__(self):
        print(f"До свидания,мистер {self.name}")


em1 = Person("Eldar", "adzhiev", 5)
# em1.name("Eldar")
# em1.surname("adzhiev")
# em1.qualification(5)
em2 = Person("Zuhra", "Adzhieva", 5 )
# em2.name("Zuhra")
# em2.surname("Adzhieva")
# em2.qualification(5)
em3 = Person("Iva","ivkin")
# em3.name("Iva")
# em3.surname("ivkin")

print(em1.info())
print(em2.info())
print(em3.info())

if em1.qualification<em3.qualification and em1.qualification<em2.qualification:
    em1.__del__()
if em2.qualification<em1.qualification and em2.qualification<em3.qualification:
    em2.__del__()
if em3.qualification<em1.qualification and em3.qualification<em2.qualification:
    em3.__del__()

input()
