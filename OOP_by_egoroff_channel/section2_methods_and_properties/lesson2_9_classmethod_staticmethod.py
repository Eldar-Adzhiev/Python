# 2.9 Classmethod и staticmethod

class Example:
    # Эту функцию мы можем вызвать из класса, но не можем от
    # экземпляра
    def hello():
        print('hello')

    # Эту функцию мы можем вызвать из экземпляра, но не можем
    # от класса
    def instance_hello(self):
        print(f'instance hello', {self})

    # Для того что бы вызывать функцию как от класса так и от
    # экземпляра класса используем декоратор @staticmethod
    @staticmethod
    def static_hello():
        print("static_hello")

    @classmethod
    def class_hello(cls):
        print(f'instance hello', {cls})


# q = Example()
# q.instance_hello()
# Example.instance_hello()
# q.hello()
# Example.hello()

""" @staticmethod можно использовать когда вам нужна функция внутри 
класса а не выносить за класс"""
# # staticmethod
# y = Example()
# y.static_hello()
# Example.static_hello()


"""@classmethod нужен когда мы хотим, делать какую-то обработку
не над экземплярами класса, а над целым классом"""
# classmethod
# Example.class_hello()
# a = Example()
# a.class_hello()

# ==========================================================================

""" Создайте класс Robot, у которого есть:

атрибут класса population. В этом атрибуте будет хранится общее 
количество роботов, изначально принимает значение 0;
конструктор __init__, принимающий 1 аргумент name. Данный метод должен
сохранять атрибут name и печатать сообщение вида "Робот <name> был 
создан". Помимо инициализации робота данный метод должен увеличивать 
популяцию роботов на единицу;
метод destroy, должен уменьшать популяцию роботов на единицу и печатать
сообщение вида "Робот <name> был уничтожен"
метод say_hello, которой печатает сообщение вида "Робот <name> 
приветствует тебя, особь человеческого рода"
метод класса  how_many, который печатает сообщение вида 
"<population>, вот сколько нас еще осталось"""

class Robot:

    population = 0

    def __init__(self, name):
        self.name = name
        print(f'Робот {name} был создан')
        Robot.population += 1

    def destroy(self):
        print(f'Робот {self.name} был уничтожен')
        del self
        Robot.population -= 1


    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')

    @classmethod
    def how_many(cls):
        print(f'{cls.population}, вот сколько нас еще осталось')

r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many() # печатает "1, вот сколько нас еще осталось"
r2.destroy() # печатает "Робот R2-D2 был уничтожен"
Robot.how_many()

