#Создание базового класса "Работник" и его наследование для создания классов
#"Менеджер" и "Инженер". В классе "Работник" будут общие методы, такие как
#"работать" и "получать зарплату", а классы-наследники будут иметь свои
#уникальные методы и свойства, такие как "управлять командой" и "проектировать
#системы".

class Worker:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def work(self):
        return f"{self.name} выполняет свою работу."

    def receive_salary(self):
        return f"{self.name} получает зарплату в размере {self.base_salary} руб."

class Manager(Worker):
    def __init__(self, name, base_salary, team_size):
        super().__init__(name, base_salary)
        self.team_size = team_size

    def manage_team(self):
        return f"{self.name} управляет командой из {self.team_size} человек."

class Engineer(Worker):
    def __init__(self, name, base_salary, specialization):
        super().__init__(name, base_salary)
        self.specialization = specialization

    def design_systems(self):
        return f"{self.name} проектирует системы в области: {self.specialization}."

worker = Worker("Иван Иванов", 50000)
print(worker.work())
print(worker.receive_salary())

manager = Manager("Анна Петрова", 80000, 10)
print(manager.work())
print(manager.manage_team())
print(manager.receive_salary())

engineer = Engineer("Сергей Сидоров", 90000, "Разработка ПО")
print(engineer.work())
print(engineer.design_systems())
print(engineer.receive_salary())