# Вывести таблицу умножения от 1 до 10
# n = 10
#
import math

# i in [1, 2, 3, 4, 5, 6, 7, 8, ,9, 10]
# i = 10

# j in [1, 2, 3, 4, 5, 6, 7, 8, ,9, 10]
# j = 10

# 1 * 1 = 1 | 1 * 2 = 2 | ..... | 1 * 10 = 10
# 2 * 1 = 2 | 2 * 2 = 2 | ..... | 2 * 10 = 20
# ........
# 10 * 1 = 10 | 10 * 2 + 20 | ..... | 10 * 10 = 100

# for i in range(1, 10 + 1):
#     for j in range(1, 10 + 1):
#         print(f"{j} * {i} = {i * j} | ", end=" ")
#     print()

# print("Hello", end=" ")
# print("World!")

# for i in range(1, 10 + 1):
#     print(i, end=' ')

#
# for student in students:
#     print(student)

# numbers = ["Tom"]
# numbers2 = numbers * 3

# print(numbers)
# print(numbers2)

# name = "Vasya"
# print(name[2])


# students = ["Tom", "Sam", "Bob"]
# students2 = ["Tom", "Bob", "Sam"]
#
# if students == students2:
#     print("All students are equal")
# else:
#     print("Some students are not equal")

# for student in students:
#     print(student)
#
# i = 0
# while i < len(students):
#     print(f"{i + 1}. {students[i]}")
#     i += 1

# student1, student2, student3 = students
# print(student1)
# print(student2)
# print(student3)

# fact = "Vasya is cool and handsome!"
#
# substring = fact[6:8]
# print(substring)

# students = ["Tom", "Sam", "Bob", "Jim", "Alex", "Vasya"]
#
# bad_students = students[1:5:2]
# print(bad_students)


# print(students.count("Tommmy"))
# print(students)
# students.pop()
# print(students)
# print(students.index("Jim"))


# students.append("Gleb")
# students.insert(1, "Rock")

# print(students)

# print(students)
# students.remove("Gleb")
# students.clear()
# print(students)

# nums = [11, 2, 33, 4, 5, 6, 7, 88, 9, 10]
# print(nums)
#
# nums.sort()
# print(nums)
#
# nums.reverse()
# print(nums)

# Задача: Получить у пользователя список учеников. И вывести этот список на консоль
# students = []
#
# for i in range(5):
#     name = input("Enter student's name: ")
#     students.append(name)
#
# print(students)
#
# for student in students:
#     print(student)

# Задача: Получить от пользователя набор чисел, и вывести их сумму
# nums = []
#
# for i in range(5):
#     num = int(input("Enter a number: "))
#     nums.append(num)
#
# total = 0
# for num in nums:
#     total = total + num

# print(total2)

students = ["Tom", "Sam", "Bob", "Jim", "Alex", "Vasya"]
name = "Tommy"
if name in students:
    print("Yes, he is")
else:
    print("Nope")