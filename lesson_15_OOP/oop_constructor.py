
class Car:

    def car_action(self, act_1, act_2):
        self.a_moove = act_1
        self.a_stop = act_2

car_1 = Car()
car_1.car_action('Move', 'Stop')

print('Car_1', car_1.a_moove, car_1.a_stop)

car_2 = Car()
car_2.car_action('Fly', 'Swim')

print('Car_2', car_2.a_moove, car_2.a_stop)


#CONSTRUCTOR
#-----------------------------------------------------------------

class Truck:
    def __init__(self, act_1, act_2):
        self.act_1 = act_1
        self.act_2 = act_2

truck_1 = Truck('Drive', 'Cheel')
print('Truck', truck_1.act_1, truck_1.act_2)

truck_2 = Truck('Fly', 'Swim')
print('Truck', truck_2.act_1, truck_2.act_2)


#---------------------------------------------------------------

class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print('display_count', Employee.emp_count)

    def display_employee(self):
        print('Name', self.name, 'Salary = ', self.salary)

emp_1 = Employee('Eldar', 1000)

emp_1.age = 20 #Новый параметр для конкретного работника

emp_2 = Employee('George', 1300)
emp_2 = Employee('Dmitry', 200)

emp_1.display_employee()
emp_2.display_employee()

employee_count = Employee.emp_count
print('employee_count = ', employee_count)

print('Emp_1_Name = ', emp_1.name, 'Emp_1_age = ', emp_1.age, 'Emp_1_salary = ', emp_1.salary )


