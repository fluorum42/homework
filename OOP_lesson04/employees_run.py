from employees import Employee
from empl_exceptions import EmailAlreadyExistsException


def main():
    epm1 = Employee('Roy', 76, 'roy@email')



if __name__ == '__main__':
    try:
        main()
    except EmailAlreadyExistsException as err:
        print("Email already exists!")
