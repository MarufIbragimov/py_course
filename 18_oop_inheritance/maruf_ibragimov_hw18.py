import math


# task #2
class Vehicle:
    def __init__(self, brand, speed):
        self.__brand = brand
        self.__speed = speed

    def describe(self):
        print(f"Brand: {self.__brand}, speed: {self.__speed}")


class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.__fuel_type = fuel_type

    def describe(self):
        super().describe()
        print(f"Fuel-type: {self.__fuel_type}")


# task #3
class Person:
    def introduce(self):
        return 'Hi, I am a person.'
    

class Student(Person):
    def introduce(self):
        intro1 = super().introduce()
        return f"{intro1} I am a student"


# task #4
class Shape:
    def area(self):
        return 0
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        area = self.__width * self.__height
        return area
    

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        area = math.pi * self.__radius ** 2
        return round(area, 2)
    

shapes = [Rectangle(5, 7), Circle(23)]
total_area = 0
for shape in shapes:
    total_area += shape.area()

print(total_area)