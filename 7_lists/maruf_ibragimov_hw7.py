"""
2. Максимум и минимум списка:
Напишите программу, которая возвращает максимум и минимум из списка чисел.
"""
nums = []

for i in range(5):
    num = int(input("Введите число: "))
    nums.append(num)

min_num = nums[0]
max_num = nums[0]

for num in nums:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
    

print(f"Минимальное значение в списке: {min_num}")
print(f"Максимальное значение в списке: {max_num}")


"""
3. Частота элемента:
Напишите программу, которая принимает список и число, и возвращает, сколько 
раз это число встречается в списке.
"""
nums = []

for i in range(5):
    num = int(input("Введите число: "))
    nums.append(num)

target = int(input("Введите искомое число: "))

counter = 0
for num in nums:
    counter += num == target

print(f"Искомое число {target} встречается в списке {counter} раз")


"""
4. Удвоение элементов:
Напишите программу, которая принимает список и возвращает новый список, в 
котором каждый элемент удвоен.
"""
nums = []

for i in range(5):
    num = int(input("Введите число: "))
    nums.append(num)

doubled = [num * 2 for num in nums]

print(nums)
print(doubled)


"""
5. Сумма чисел с определённым условием: - опционально
Найдите сумму всех чисел в списке, которые больше 10.
"""
nums = []

for i in range(5):
    num = int(input("Введите число: "))
    nums.append(num)

sum_over_ten = 0
for num in nums:
    if num > 10:
        sum_over_ten += num

print(f"Сумма чисел в списке, которые больше 10 равна: {sum_over_ten}")