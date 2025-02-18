from task import Task
import db


class ConsoleApplication:
    def __init__(self):
        self.tasks = list()
        self.current_id = 1

    def add_task(self):
        print("--------------Добавление задачи--------------")
        t = Task()

        title = input("Введи название задачи: ")
        t.title = title

        description = input("Введи описание задачи: ")
        t.description = description

        # deadline = input("Введи дедлайн задачи: ")
        # t.deadline = deadline

        priority_id = int(input("Введи приоритет задачи (низкий(1), средний(2), высокий(3)): "))
        priorities = ["низкий", "средний", "высокий"]
        if 1 > priority_id or priority_id > 3:
            print("Вы ввели неправильный ID приоритета!")
            return
        t.priority = priorities[priority_id]

        # self.tasks.append(t)
        task_id = db.create_task(t)
        print(f"--------------Задача {task_id} успешно  добавлена--------------")
        # self.current_id += 1

    def print_tasks(self):
        tasks = db.get_all_tasks()
        print("--------------Список ваших задач:--------------")
        for task in tasks:
            print(f"{task.task_id}. {task.title}")
        print("-----------------------------------------------")

    def task_exists(self, task_id):
        is_in_db = db.check_if_task_exists(task_id)


        # while i < len(self.tasks):
        #     if self.tasks[i].task_id == task_id:
        #         return i
        #     i += 1

        return is_in_db


    def edit_task(self):
        target_task_id = int(input("Введи ID задачи которую хотите изменить: "))

        task_index = self.task_exists(target_task_id)
        if task_index == -1:
            print(f"Нет задачи с ID = {target_task_id}")
            return

        title = input("Введи название задачи: ")
        self.tasks[task_index].title = title

        description = input("Введи описание задачи: ")
        self.tasks[task_index].description = description

        deadline = input("Введи дедлайн задачи: ")
        self.tasks[task_index].deadline = deadline

        priority = input("Введи приоритет задачи (низкий, средний, высокий): ")
        self.tasks[task_index].priority = priority


    def print_task_by_id(self):
        target_task_id = int(input("Введи ID задачи: "))

        task_id = self.task_exists(target_task_id)

        if not task_id:
            print(f"Нет задачи с ID = {target_task_id}")
            return
        t = db.get_task_by_id(target_task_id)
        print("--------------Список ваших задач:--------------")
        print(f"{t.task_id}. {t.title}")
        print("-----------------------------------------------")
        # print(f"--------------Задача с ID = {target_task_id}--------------")
        # print(f"Название: {self.tasks[task_id].title}")
        # print(f"Описание: {self.tasks[task_id].description}")
        # print(f"Дедлайн: {self.tasks[task_id].deadline}")
        # print(f"Приоритет: {self.tasks[task_id].priority}")
        # if self.tasks[task_id].is_done:
        #     print(f"Статус: Выполнено")
        # else:
        #     print(f"Статус: Не выполнено")

    def insert_fake_data(self):
        t1 = Task(self.current_id)
        t1.title = "Тестовый заголовок 1"
        t1.description = "Тестовое описание 1"
        t1.deadline = "31-12-2025"
        t1.priority = "низкий"
        t1.is_done = True
        self.tasks.append(t1)
        self.current_id += 1

        t2 = Task(self.current_id)
        t2.title = "Тестовый заголовок 2"
        t2.description = "Тестовое описание 2"
        t2.deadline = "30-12-2025"
        t2.priority = "средний"
        self.tasks.append(t2)
        self.current_id += 1
        print("Фейковые данные успешно добавлены!!!")

    def start(self):
        print("Добро пожаловать в Todo-List-App!")
        while True:
            print("-----------------------------------------------")
            print("Главное меню:")
            print("1. Добавить новую задачу")
            print("2. Вывести список задач")
            print("3. Редактировать задачу")
            print("4. Вывести задачу по ID")
            print("5. Удалить задачу по ID")
            print("6. Пометить задачу Выполнено / Не выполнено")
            print("7. Добавить фейковые данные")
            print("0. Выход")
            cmd = int(input("Выберите нужную команду: "))

            if cmd == 0:
                print("До скорой встречи!)")
                break
            elif cmd == 1:
                self.add_task()
            elif cmd == 2:
                self.print_tasks()
            elif cmd == 3:
                self.edit_task()
            elif cmd == 4:
                self.print_task_by_id()
            elif cmd == 7:
                self.insert_fake_data()
            # elif cmd == 5:
            #     delete_task(tasks)
            # elif cmd == 6:
            #     change_task_status(tasks)
            else:
                print("Вы ввели несуществующую команду!!!")
            print("-----------------------------------------------")
