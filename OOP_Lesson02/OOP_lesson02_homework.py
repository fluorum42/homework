"""
Створити клас Employee.
Конструктор має приймати наступні аргументи: ім’я, ЗП за один робочий день.
Створити метод work(self, …) який повертає строку “I come to the office.”
Створити класи Recruiter та Developer, які наслідують клас Employee.
Перевизначити методи work  в класах R та D, щоб вони повертали значення:
“I come to the office and start to coding.” - для Developer
“I come to the office and start to hiring.” - для Recruiter
Перевизначити методи  __str__, щоб они повертали строку: “Посада: Ім’я”
Зробити можливим порівнювати Employee по рівню ЗП.
Створити метод check_salary(self, days), який розраховує ЗП за передану кількість днів.
** Зробити можливим, щоб метод check_salary рахував ЗП з початку місяця до поточного дня, не враховуючи вихідні дні.
Додати в конструктор класу Developer атрибут tech_stack (список з назвами технологій).
Для класу Developer зробити порівняння за кількістю технологій.
Зробити можливим операцію додавання об’єктів класу Developer. Результатом має бути новий об’єкт
В якому name = name1 + ‘ ’ + name2, a tech_stack - список з технологій двох об’єктів (тільки унікальні значення),
ЗП - більша з двох.
"""
from datetime import datetime, timedelta


class Employee:
    def __init__(self, name, day_salary):
        self.name = name
        self.day_salary = day_salary

    def __work__(self):
        return "I come to the office."

    def __str__(self):
        return f'{self.__class__} {self.name}'

    def __lt__(self, other):
        return self.day_salary < other.day_salary

    def __le__(self, other):
        return self.day_salary <= other.day_salary

    def __gt__(self, other):
        return self.day_salary > other.day_salary

    def __ge__(self, other):
        return self.day_salary >= other.day_salary

    def __eq__(self, other):
        return self.day_salary == other.day_salary

    def __ne__(self, other):
        return self.day_salary != other.day_salary

    def __check_salary__(self, days):
        return self.day_salary * days

    def __check_salary2__(self):
        today = datetime.now()
        first_day = datetime.now().replace(day=1) - timedelta(days=0)
        daygenerator = (first_day + timedelta(x) for x in range((today - first_day).days + 1))
        work_days = sum(1 for day in daygenerator if day.weekday() < 5)
        return self.day_salary * work_days


class Recruiter(Employee):
    def __work__(self):
        init_str = super().__work__()
        return init_str[:-1] + " and start hiring."


class Developer(Employee):
    def __init__(self, name, day_salary, tech_stack):
        super().__init__(name, day_salary)
        self.tech_stack = tech_stack

    def __work__(self):
        init_str = super().__work__()
        return init_str[:-1] + " and start coding."

    def __lt__(self, other):
        return self.tech_stack < other.tech_stack

    def __le__(self, other):
        return self.tech_stack <= other.tech_stack

    def __gt__(self, other):
        return self.tech_stack > other.tech_stack

    def __ge__(self, other):
        return self.tech_stack >= other.tech_stack

    def __eq__(self, other):
        return self.tech_stack == other.tech_stack

    def __ne__(self, other):
        return self.tech_stack != other.tech_stack

    def __add__(self, other):
        res = [self.name, other.name]
        for i in self.tech_stack:
            if i not in other.tech_stack:
                res.append(i)
        if self.day_salary > other.day_salary:
            res.append(str(self.day_salary))
        else:
            res.append(str(other.day_salary))
        return ' '.join(res)


if __name__ == '__main__':
    worker = Employee('Roy', 76)
    print(worker.__work__())
    worker2 = Developer('Jack', 89, tech_stack=['a', 'c'])
    worker4 = Developer('Bob', 93, tech_stack=['a', 'b', 'c', 'd', 'e'])
    print(worker2.__work__())
    worker3 = Recruiter('Sam', 94)
    print(worker3.__str__())
    print(worker3.__ne__(worker2))
    print(worker.__check_salary__(12))
    print(worker4.__lt__(worker2))
    print(worker4.__add__(worker2))
    print(worker.__check_salary2__())
