"""
1. Создание и работа со словарем:
Создайте словарь с именами студентов (ключи) и их оценками (значения).
"""
students = {'Mike': 75, 'Leo': 65, 'Donnie': 80, 'Raf': 100}

"""
2. Добавление элементов:
Создайте словарь и добавьте в него 3 новых элемента. Затем измените значение 
одного из существующих ключей.
"""
person = {
    'name': 'John',
    'last_name': 'Dow',
    'height': 173,
    'weight': 74
}

additional_info = [('race', 'caucasian'), ('eyes_color', 'green'), ('hair_color', 'blonde')]

person.update(additional_info)
person['last_name'] = 'Walker'

print(person)


"""
3. Проверка наличия ключа:
Напишите программу, которая проверяет, существует ли заданный ключ в 
словаре. Если существует, выведите его значение, иначе сообщите, что ключ 
отсутствует.
"""
key_to_check = 'marital status'
print(person.get(key_to_check, f"Ключ '{key_to_check}' не найден в словаре"))


"""
4. Объединение словарей:
Напишите программу, которая принимает два словаря и объединяет их. Если 
ключи совпадают, то значения должны суммироваться.
"""
students = {'Mike': 75, 'Leo': 65, 'Donnie': 80, 'Raf': 100}
new_students = {'Harry': 70, 'Hermione': 100, 'Ron': 72, 'Mike': 20}

for k, v in new_students.items():
    if not students.get(k, 0):
        students[k] = v
    else:
        students[k] += v

print(students)

"""
5. Обратный словарь:
Напишите программу, которая меняет местами ключи и значения в словаре.
"""
students = {'Mike': 95, 'Leo': 65, 'Donnie': 80, 'Raf': 100, 'Harry': 70, 'Hermione': 100, 'Ron': 72}

swapped_dict = {}
for k, v in students.items():
    if not swapped_dict.get(v, 0):
        swapped_dict[v] = k
    else:
        to_replace = int(input(f"""
            Ключ {v} уже существует и его значение равно: {swapped_dict[v]}.
            Вы хотите его заменить на новое значение: {k} (0 если "нет", 1 если "да")? 
        """))
        if to_replace:
            swapped_dict[v] = k
        
print(swapped_dict)