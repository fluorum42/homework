import logging
import traceback
from employees import Employee
from empl_exceptions import EmailAlreadyExistsException


def main():
    epm1 = Employee('Roy', 76, 'roy@email')



if __name__ == '__main__':
    try:
        main()
    except EmailAlreadyExistsException as err:
        print('Email already exists!')
        Log_Format = "%(levelname)s %(asctime)s - %(message)s"

        logging.basicConfig(filename="logs.txt",
                            filemode="w",
                            format=Log_Format,
                            level=logging.ERROR)

        logger = logging.getLogger()
        logger.error("EmailAlreadyExistsException")
        with open('/home/polina/Документи/polina/homework/OOP_lesson04/logs.txt', 'a+') as file:
            file.write(traceback.format_exc())
