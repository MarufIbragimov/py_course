"""
3. Четные числа
Напишите программу, которая выводит все четные числа от 1 до N.
"""
def print_even(n):
    for num in range(n+1):
        if num % 2 == 0:
            print(num)


print_even(10)


"""
4. Обратный порядок
Напишите программу, которая выводит числа от N до 1 (в обратном порядке).
"""
def countdown(n):
    for num in range(n, 0, -1):
        print(num)


countdown(10)


"""
6. Таблица умножения
Напишите программу, которая выводит таблицу умножения для числа, введенного 
с клавиатуры.
"""
def multiplication_table(num):    
    for i in range(1, 10+1):
        res = num * i
        print(f"{num} x {i} = {res}")

num = int(input("Введите число для вывода таблицы умножения: "))
multiplication_table(num)


"""
7. Сумма цифр числа
Напишите программу, которая находит сумму цифр числа, введенного с 
клавиатуры. Используйте цикл while.
"""
def summarize(num):
    res = 0
    
    while True:
        res += num % 10
        num //= 10  

        if num == 0:
            break

    print(res)

num = int(input("Введите число для нахождения суммы цифр: "))
summarize(num)


"""
8. Простые числа
Напишите программу, которая выводит все простые числа от 1 до N.
"""

def prime(num):
    is_prime = True
    for i in range(1, num + 1):
        if i not in (1, num) and num % i == 0:
            is_prime = False
        
    return is_prime


def print_primes(number):
    for i in range(2, number):
        if prime(i):
            print(i)


number = int(input("Введите число для нахождения простых чисел: "))
print_primes(number)


"""
9. “FizzBuzz”
Напишите программу, которая выводит числа от 1 до 100.
• Если число делится на 3, вместо него выводится Fizz.
• Если число делится на 5, вместо него выводится Buzz.
• Если делится и на 3, и на 5, выводится FizzBuzz.
"""

def fizzbuzz():
    for num in range(1, 100 + 1):
        if num % 5 == 0 and num % 3 == 0:
            print('FizzBuzz')
        elif num % 5 == 0:
            print('Buzz')
        elif num % 3 == 0:
            print('Fizz')
        else:
            print(num)

fizzbuzz()
        