"""
Гулливер https://acmp.ru/index.asp?main=task&id_task=773
"""
stdin = input()
nums = [int(num) for num in stdin.split(' ')]

res = nums[0]**2 * nums[1]

print(res)


"""
Два бандита https://acmp.ru/index.asp?main=task&id_task=33
"""
stdin = input()
nums = [int(num) for num in stdin.split(' ')]
total = sum(nums)
not_shot1 = total - 1 - nums[0]
not_shot2 = total -1 - nums[1]

print(not_shot1, not_shot2)


"""
Зарплата  https://acmp.ru/index.asp?main=task&id_task=21
"""
stdin = input()
nums = [int(num) for num in stdin.split(' ')]
min_salary = min(nums)
max_salary = max(nums)
diff = max_salary - min_salary
print(diff)