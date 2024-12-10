nums = []

for i in range(5):
    num = int(input("Введите число: "))
    nums.append(num)

sum_over_ten = 0
for num in nums:
    if num > 10:
        sum_over_ten += num

print(f"Сумма чисел в списке, которые больше 10 равна: {sum_over_ten}")