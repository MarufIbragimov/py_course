
def is_valid(value):
    is_valid = False
    if type(value) is not str:
        if value >= 0:
            is_valid = True

    return is_valid   


class Employee:
    def __init__(self, per_hour, hours_worked):
        self.per_hour = per_hour
        self.hours_worked = hours_worked

    def __calculate_salary(self):
        salary = self.per_hour * self.hours_worked
        return salary
    
    def display_info(self):
        print(self.__calculate_salary())


class Student:
    def __init__(self, grade=0):
        self.__grade = grade

    def get_grade(self):
        return self.__grade
    
    def set_grade(self, grade):
        if type(grade) is not int:
            print('Неприемлемый тип данных. Валидны только целые числа')
        elif not 0 <= grade <= 100:
            print('Оценка может быть только в диапазоне от 0 до 100')
        else:
            self.__grade = grade


class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @width.setter
    def width(self, width):
        if not is_valid(width):
            print("Невалидное значение")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        if not is_valid(height):
            print("Невалидное значение")
        else:
            self.__height = height


class SecureData:
    def __init__(self, password, data=None):
        self.__password = str(password)
        self.__data = data

    def __check_password(self, password):
        is_correct = self.__password == password
        return is_correct
    
    def get_data(self):
        password = input("Введите пароль для доступа к данным: ")
        if self.__check_password(password):
            return self.__data
        else:
            print('Неверный пароль')


class ATM:
    def __init__(self, cash_balance, pin):
        self.__cash_balance = cash_balance
        self.__pin = str(pin)

    def check_balance(self):
        return self.__cash_balance
    
    def __check_pin(self, pin):
        is_correct = self.__pin == pin
        return is_correct
    
    def withdraw(self, amount):
        if is_valid(amount) and amount <= self.__cash_balance:
            pin = input("Введите pin-код: ")
            if not self.__check_pin(pin):
                print("Неверный pin-код")
            else:
                self.__cash_balance -= amount
        else:
            print("Неверное значение")
        
    def change_pin(self, old_pin, new_pin):
        if not self.__check_pin(str(old_pin)):
            print("Неверный pin-код")
        else:
            self.__pin = str(new_pin)
             