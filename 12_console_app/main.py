# Задача:
# Название - title
# Описание - description
# Срок выполнения - deadline
# Приоритет - priority (низкий, средний, высокий)
# Статус - is_done


def add_task(tasks, task_id):
    task_id += 1
    print("--------------Добавление задачи--------------")
    task = dict()
    task['task_id'] = task_id

    title = input("Введи название задачи: ")
    task['title'] = title

    description = input("Введи описание задачи: ")
    task['description'] = description

    deadline = input("Введи дедлайн задачи: ")
    task['deadline'] = deadline

    deadline = input("Введи приоритет задачи (низкий, средний, высокий): ")
    task['priority'] = deadline

    task['is_done'] = False
    tasks.append(task)

    print(f"--------------Задача {task_id} успешно  добавлена--------------")
    return task_id


def print_tasks(tasks):
    print("--------------Список ваших задач:--------------")
    for task in tasks:
        print(f"{task['task_id']}. {task['title']}")
    print("-----------------------------------------------")


def print_task_by_id(tasks):
    target_task_id = int(input("Введи ID задачи: "))

    task_id = task_exists(tasks, target_task_id)
    if task_id == -1:
        print(f"Нет задачи с ID = {target_task_id}")
        return

    print(f"--------------Задача с ID = {target_task_id}--------------")
    print(f"Название: {tasks[task_id]['title']}")
    print(f"Описание: {tasks[task_id]['description']}")
    print(f"Дедлайн: {tasks[task_id]['deadline']}")
    print(f"Приоритет: {tasks[task_id]['priority']}")
    if tasks[task_id]['is_done']:
        print(f"Статус: выполнено")
    else:
        print(f"Статус: не выполнено")


def task_exists(tasks, task_id):
    i = 0

    while i < len(tasks):
        if tasks[i]['task_id'] == task_id:
            return i
        i += 1

    return -1


def edit_task(tasks):
    target_task_id = int(input("Введи ID задачи которую хотите изменить: "))

    task_id = task_exists(tasks, target_task_id)
    if task_id == -1:
        print(f"Нет задачи с ID = {target_task_id}")
        return

    title = input("Введи название задачи: ")
    tasks[task_id]['title'] = title

    description = input("Введи описание задачи: ")
    tasks[task_id]['description'] = description

    deadline = input("Введи дедлайн задачи: ")
    tasks[task_id]['deadline'] = deadline

    deadline = input("Введи приоритет задачи (низкий, средний, высокий): ")
    tasks[task_id]['priority'] = deadline


def main():
    tasks = list()
    task_id = 0
    print("Добро пожаловать в Todo-List-App!")

    while True:
        print("-----------------------------------------------")
        print("Главное меню:")
        print("1. Добавить новую задачу")
        print("2. Вывести список задач")
        print("3. Редактировать задачу")
        print("4. Вывести задачу по ID")
        print("0. Выход")
        cmd = int(input("Выберите нужную команду: "))

        if cmd == 0:
            print("До скорой встречи!)")
            break
        elif cmd == 1:
            task_id = add_task(tasks, task_id)
        elif cmd == 2:
            print_tasks(tasks)
        elif cmd == 3:
            edit_task(tasks)
        elif cmd == 4:
            print_task_by_id(tasks)
        else:
            print("Вы ввели несуществующую команду!!!")
        print("-----------------------------------------------")


main()
