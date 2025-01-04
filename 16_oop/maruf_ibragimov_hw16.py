import math


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f'Название: {self.title}, Автор: {self.author}, Год: {self.year}.')


class Student:
    def __init__(self, name, age, grades=[]):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if len(self.grades) == 0:
            return 0
        else:
            return sum(self.grades) / len(self.grades)
    

class Circle:
    def __init__(self, radius):
        if radius < 0:
            print('Радиус должен быть больше 0')
        else:
            self.radius = radius

    def area(self):
        area = math.pi * self.radius ** 2
        return area
    
    def circumference(self):
        circumference = 2 * math.pi * self.radius
        return circumference
    

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        is_adult = self.age >= 18
        return is_adult
    

class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            print('Ширина и высота должны быть больше 0')
        else:
            self.width = width
            self.height = height

    def is_square(self):
        is_square = self.width == self.height
        return is_square
    
    def resize(self, new_width, new_height):
        if new_width < 0 or new_height < 0:
            print('Новые размеры должны быть больше 0')
        else:
            self.width = new_width
            self.height = new_height

    
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print('Сумма должна быть больше 0')
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print('Сумма должна быть больше 0')
        elif amount > self.balance:
            print('Недостаточно средств')
        else:
            self.balance -= amount

    def check_balance(self):
        print(self.balance)


class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(f'Гав-гав, меня зовут {self.name}!')