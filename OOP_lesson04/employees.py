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
Додати до класу Employee методи save_email(self) та validate(self) та атрибут email
Створити виняток EmailAlreadyExistsException
Метод save_email має викликатись в кінці методу __init__ та записувати email в файл emails.txt
Метод validate має перевіряти чи існує імейл в файлі. Якщо імейл вже існує, то викликати
помилку EmailAlreadyExistsException
В головному файлі програми (app.py або main.py) весь код, який знаходиться в блоці
if __name__ == ‘__main__’ перенести в нову функцію main() і викликати цю функцію в
name == main блоці.
Огорнути виклик функції main() в блок try/except.
У разі виникнення винятку EmailAlreadyExistsException записати в файл logs.txt повідомлення у вигляді:
%дата% %час% | %traceback%
"""
from datetime import datetime, timedelta
from empl_exceptions import EmailAlreadyExistsException


class Employee:
    def __init__(self, name, day_salary, email):
        self.name = name
        self.day_salary = day_salary
        self.email = email
        self.validate()
        self.save_email()  # -> write email to file

    def validate(self):
        """
        1. Read the file with emails.
        2. Check that self.email in file.
        3. If not: do nothing
        4. Else: raise EmailAlreadyExistsException
        :return:
        """
        with open('/home/polina/Документи/polina/homework/OOP_lesson04/empl_emails') as f:
            for line in f:
                if self.email in line:
                    raise EmailAlreadyExistsException
                else:
                    pass
            # return EmailAlreadyExistsException

    def save_email(self):
        """Open file in append mode a+. Write email."""
        with open('/home/polina/Документи/polina/homework/OOP_lesson04/empl_emails', 'a+') as f:
            f.write(self.email + '\n')

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
    def __init__(self, name, day_salary, email, tech_stack):
        super().__init__(name, day_salary, email)
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
