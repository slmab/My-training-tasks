# TODO здесь писать код

class Person:
    def __init__(self, name='', surname='', age=0):
        self.__name = name
        self.__surname = surname
        self.__age = age


class Employee(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.salary = 0

    def employee_salary(self):
        pass


class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def manager_salary(self):
        self.salary = 13000
        return self.salary


class Agent(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def agent_salary(self, sales):
        self.salary = 5000 + sales * 0.05
        return self.salary


class Worker(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def worker_salary(self, hours):
        self.salary = 100 * hours
        return self.salary


employee_list = [
    Manager(name='Вася', surname='Петров', age=24).manager_salary(),
    Manager(name='Вася', surname='Петров', age=24).manager_salary(),
    Manager(name='Вася', surname='Петров', age=24).manager_salary(),
    Agent(name='Вася', surname='Петров', age=24).agent_salary(50000),
    Agent(name='Вася', surname='Петров', age=24).agent_salary(100000),
    Agent(name='Вася', surname='Петров', age=24).agent_salary(10000),
    Worker(name='Вася', surname='Петров', age=24).worker_salary(160),
    Worker(name='Вася', surname='Петров', age=24).worker_salary(120),
    Worker(name='Вася', surname='Петров', age=24).worker_salary(180)
]

print(employee_list)
