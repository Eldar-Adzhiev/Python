class Warrior:
    health = 100

    def attack(self, ):
        self.health -= 20


elf = Warrior()
ork = Warrior()

print(elf.health)
print(ork.health)

who_kick_first = input()

if who_kick_first == "elf":
    while ork.health > 0:
        ork.attack() # Орк подвергся аттаке
        print(ork.health)
        elf.attack() # Эльф подвергся аттаке
        print(ork.health)
        if ork.health == 0:
            print("Elf win")
        else:
            print("Ork win")
if who_kick_first == "ork":
    while elf.health > 0:
        elf.attack() # Эльф подвергся аттаке
        print(ork.health)
        ork.attack() # Орк подвергся аттаке
        print(ork.health)
        if elf.health == 0:
            print("Ork win")
        else:
            print("Elf win")

# ====================================================================================

class Battle:
    def duel(self, elf, ork):
        who_kick_first = input()

        while elf.health > 0 and ork.health > 0:
            if who_kick_first == "elf":
                Warrior.attack(ork) # Орк аттакован
                print(ork.health)
            else:
                who_kick_first == "ork"
                Warrior.attack(elf) # Эльф аттакован
                print(elf.health)
        if elf.health > ork.health:
            print("Эльф победил")
        else:
            ork.health > elf.health
            print("Орк победил")



elfVSork = Battle()
elfVSork.duel(elf,ork)

#==========================================================================================
# Однако в программировании так делать не принято, потому что тогда объекты одного класса
# будут отличаться между собой по набору атрибутов. Это затруднит автоматизацию их
# обработки, внесет в программу хаос.
# Поэтому принято присваивать полям, а также получать их значения, путем вызова методов:

class User:
    def setName(self, name):
        self.name = name


    def getName(self):
        try:
            return self.name
        except:
            print("No name")

first = User()
second = User()

first.setName("Eldar")
print(first.getName())
second.getName()

User.setName(second, "Zuhra")
print(second.getName())