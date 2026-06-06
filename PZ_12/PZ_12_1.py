class Employee:
    def __init__(self, surname, position, salary):
        self.surname = surname
        self.position = position
        self.salary = salary

class Squad:
    def __init__(self):
        self.employees = [
            Employee("Иванов", "Менеджер", 50000),
            Employee("Петров", "Разработчик", 80000),
            Employee("Сидоров", "Дизайнер", 60000),
            Employee("Козлов", "Тестировщик", 55000)
        ]

    def print_salaries(self):
        for emp in self.employees:
            print(f"{emp.surname}: {emp.salary}")

squad = Squad()
squad.print_salaries()