# Создать структуру данных для студентов из имен и фамилий, можно случайных. Придумать структуру данных, чтобы
# указывать, в какой группе учится студент (Группы Python, FrontEnd, FullStack, Java). Студент может учиться в
# нескольких группах. Затем вывести:
# студентов, которые учатся в двух и более группах;
# студентов, которые не учатся на фронтенде;
# студентов, которые изучают Python или Java.
students = {'Jules Winnfield', 'Jody McClusky', 'Butch Coolidge', 'Sandy Smithers', 'Larry Dimmick', 'Joe Cabbot', 'John Ruth', 'Marquis Warren', 'Vincent Vega', 'Pete Hicox'}
python = {'Larry Dimmick', 'Vincent Vega', 'Sandy Smithers'}
front_end = {'Jules Winnfield', 'Butch Coolidge', 'John Ruth', 'Vincent Vega'}
full_stack = {'Jody McClusky', 'Sandy Smithers', 'Pete Hicox'}
java = {'Marquis Warren', 'Larry Dimmick', 'Joe Cabbot'}
# выводим студентов, которые учатся в двух и более группах
# intersection = list(set(python) & set(front_end) & set(full_stack) & set(java))
# print(intersection)
intersection = []                # выводим студентов, которые учатся в двух и более группах
for student in python:
    if student in front_end:
        intersection.append(student)
    elif student in full_stack:
        intersection.append(student)
    elif student in java:
        intersection.append(student)
    for student in front_end:
        if student in full_stack:
            intersection.append(student)
        elif student in java:
            intersection.append(student)
        for student in full_stack:
            if student in java:
                intersection.append(student)
print(f'Students who study in two or more groups: {set(intersection)}')

not_front_end_stud = students - front_end           # студенты, которые не учатся на фронтенде
print(f'Students who do not study FrontEnd: {not_front_end_stud}')

stud_py_java = python | java          # студенты, которые изучают Python или Java
print(f'Students who study Python or Java: {stud_py_java}')
