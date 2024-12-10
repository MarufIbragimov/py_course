"""
2. Таблица умножения для числа
Напишите программу, которая выводит таблицу умножения для числа N.
"""
num = int(input("Введите целое число: "))

result = 0

print(f"Таблица умножения для {num}:")
for multiplier in range(1, 10+1):
    result = num * multiplier
    print(f"{num} * {multiplier} = {result}")


############################################################################################################################################
# ОПЦИОНАЛЬНО
############################################################################################################################################

"""
№1 Пробежка

В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. 
По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
"""
x = int(input("Введите стартовую дистанцию: "))
y = int(input("Введите итоговую дистанцию: "))

counter = 1
while x < y:
    counter += 1
    x *= 1.1

print(f"Пробег спортсмена на {counter} день, составит {round(x, 2)} километров")


"""
№2 Банковские проценты

Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чего дробная часть копеек отбрасывается. 
Определите, через сколько лет вклад составит не менее y рублей.
"""
x = float(input("Введите начальную сумму: "))
p = float(input("Введите значение процента: "))
y = float(input("Введите итоговую сумму: "))

counter = 0

while x < y:
    counter += 1
    x *= (1 + p/100)
    x = (x * 10000)//100/100 # отбрасываем дробную часть копеек

print(f"Через {counter} лет размер вклада составит {x} рублей")


"""
№3 Второй максимальный в последовательности

Последовательность состоит из различных натуральных чисел и завершается числом 0. 
Определите значение второго по величине элемента в этой последовательности.
"""
largest = 0
second_largest = 0

while True:
    num = int(input("Введите натуральное число: "))

    if num == 0:
        break

    if num > largest:
        second_largest = largest
        largest = num

if second_largest != 0:
    print(f"{second_largest} является вторым по величине числом в введённой последовательности.")
else:
    print("Недостаточное количество чисел в последовательности.")


"""
№4 Сумма элементов последовательности - 2

Найдите сумму последовательности натуральных чисел, если признаком окончания последовательности является два подряд идущих числа 0. 
Числа стоящие после двух нулей в решении задачи участвовать не должны.
"""
sequence = input("Введите последовательность натуральных чисел разделённых запятой: ")

res = 0
zeroes_counter = 0

for num in sequence.split(','):
    num = int(num)
    
    if num == 0:
        zeroes_counter += 1
    else:
        zeroes_counter = 0 # обнуляем счётчик нулей

    if zeroes_counter == 2:
        break

    res += num

print(f"Сумма чисел в последовательности, до подряд идущих нулей, составляет: {res}")


"""
#5 Числа Фибоначчи

Последовательность Фибоначчи определяется так:

φ0=0,φ1=1,...,φn=φn−1+φn−2.

По данному числу n≥1 определите n-е число Фибоначчи φn.
"""
num = int(input("Введите натуральное число: "))

x1, x2 = 0, 1

counter = 0
res = 0

while True:
    res = x1 + x2
    x1 = x2
    x2 = res

    counter += 1

    if counter == num:
        break

print(f"Под порядковым номером {num} в последовательности Фибоначчи находится цифра: {x1}")


"""
№6 Раздвоитель

Исполнитель “Раздвоитель” преобразует натуральные числа. 
У него есть две команды: “Вычесть 1” и “Разделить на 2”, первая команда уменьшает число на 1, вторая команда уменьшает число в два раза, 
если оно чётное, иначе происходит ошибка.

Дано два натуральных числа A и B (A>B). Напишите алгоритм для Раздвоителя, который преобразует число A в число B и при этом содержит минимальное число команд. 
Команды алгоритма нужно выводить по одной в строке, первая команда обозначается, как -1, вторая команда как :2.
"""
num = int(input("Введите начальное число: "))
target = int(input("Введите итоговое число: "))

if target >= num:
    print("Итоговое значение должно быть меньше начального")
else:
    while num != target:
        if num % 2 == 0:
            num /= 2
            print(f":2, result: {num}")
        else:
            num -= 1
            print(f"-1, result: {num}")


"""
№7 Максимальное количество подряд равных

Дана последовательность натуральных чисел, завершающаяся числом 0. 
Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.
"""
prev = 0
repetition_counter = 1
max_sequence = 0

while True:
    num = int(input("Введите натуральное число: "))

    if num == 0:
        break

    if num == prev:
        repetition_counter += 1
        if repetition_counter > max_sequence:
            max_sequence = repetition_counter
    else:
        repetition_counter = 1

    prev = num

if max_sequence != 0:
    print(f"Наибольшее число равнозначных подряд идущих элементов последовательности: {max_sequence}.")
else:
    print("Равнозначных чисел идущих подряд в последовательности не обнаружено.")


"""
№8 Максимальная длина монотонного фрагмента

Дана последовательность натуральных чисел, завершающаяся число 0. 
Определите наибольшую длину монотонного фрагмента последовательности (то есть такого фрагмента, где все элементы либо больше предыдущего, либо меньше).
"""
prev = 0
increasing_sequence_counter = 1
decreasing_sequence_counter = 1
max_sequence = 0

while True:
    num = int(input("Введите натуральное число: "))

    if num == 0:
        break

    if num > prev:
        increasing_sequence_counter += 1
        if increasing_sequence_counter > max_sequence:
            max_sequence = increasing_sequence_counter
    else:
        increasing_sequence_counter = 1

    if num < prev:
        decreasing_sequence_counter += 1
        if decreasing_sequence_counter > max_sequence:
            max_sequence = decreasing_sequence_counter
    else:
        decreasing_sequence_counter = 1

    prev = num

if max_sequence != 0:
    print(f"Наибольшее число монотонной последовательности элементов: {max_sequence}.")
else:
    print("Монотонной последовательности не обнаружено.")


"""
№9 Стандартное отклонение

Дана последовательность натуральных чисел x1,x2,...,xn. 
Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.
"""
counter = 0
res = 0

# так как списки мы ещё не проходили, будем использовать строку для сохранения последовательности 
sequence = '' 

while True:
    num = int(input("Введите натуральное число: "))

    if num == 0:
        break

    counter += 1
    res += num
    sequence += f'{num},'

mean = res / counter

diffs = 0
for x in sequence.split(','):
    if len(x) > 0:
        diffs += (int(x) - mean) ** 2    
dispersion = diffs / (counter - 1)


stdev = dispersion ** (1/2)

print(f"Стандартное отклонение последовательности равно: {round(stdev, 2)}")