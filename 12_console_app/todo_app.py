"""
Практическая работа по созданию менеджера задач
"""

TXT_MAX_LENGTH: int = 50
FILLER_SYMBOL: str = '*'
tasks: dict[int, dict] = {}

ids_roster: list = []

main_menu: dict[int, str] = {
    1: 'Добавить новую задачу',
    2: 'Вывести список активных задач',
    3: 'Вывести список выполненных задач',
    4: 'Вывести задачу по ID',
    5: 'Редактировать задачу',
    6: 'Удалить задачу',
    7: 'Пометить задачу как выполненную',
    8: 'Снять пометку о выполнении задачи',
    0: 'Выход'
}

task_details: dict[int, dict[str, str]] = {
    1: {'detail': 'task_id', 'caption': 'ID задачи'},
    2: {'detail': 'is_done', 'caption': 'Статус задачи'},
    3: {'detail': 'title', 'caption': 'Название задачи'},
    4: {'detail': 'description', 'caption': 'Описание задачи'},
    5: {'detail': 'deadline', 'caption': 'Дедлайн задачи'},
    6: {'detail': 'priority', 'caption': 'Приоритет задачи'},
}

task_addition_submenu: dict[int, str] = {
    1: 'Добавить ещё одну задачу',
    2: 'Вернуться в главное меню'
}

task_removal_menu: dict[int, str] = {
    1: 'Удалить задачу по ID',
    2: 'Удалить все задачи',
    3: 'Вернуться в главное меню'
}

menus: dict[int, dict] = {
    1: {'caption': 'ГЛАВНОЕ МЕНЮ', 'menu': main_menu},
    2: {'caption': 'МЕНЮ', 'menu': task_addition_submenu},
    3: {'caption': 'УДАЛЕНИЕ', 'menu': task_removal_menu}
}


def show_menu(menu_caption: str, menu: dict[int, str]):
    """
    Выводит меню на консоль.

    Args:
        menu_caption (str): Заголовок меню.
        menu (dict[int, str]): Словарь с пунктами меню.
    Returns:
        None
    """
    menu_caption = f"  {menu_caption}  "  
        
    print(f"\n{menu_caption.center(TXT_MAX_LENGTH, FILLER_SYMBOL)}")
    for key, value in menu.items():
        print(f"{key}. {value}")
    print('\n')
    

def validate(user_input, ids: list) -> bool:
    """
    Валидирует введённое пользователем значение.

    Args:
        user_input (str): Введённое пользователем значение.
        ids (list): Список идентификаторов для валидации.
    Returns:
        bool: Результат валидации.
    """
    ids = list(ids)
    if 0 not in ids:
        ids.append(0)  # чтобы можно было из любого состояния вернуться в главное меню
    user_input = user_input.strip()
    
    is_valid = user_input.isnumeric() and int(user_input) in ids
    return is_valid
    

def get_user_choice(ids: list, selection_type: str = 'option') -> int:
    """
    Получает команду от пользователя и проверяет её на валидность.

    Args:
        ids (list): Список идентификаторов для валидации.
        selection_type (str, optional): Тип выбора. Дефолтное значение 'option'.   
    Returns:
        int: Команду пользователя.
    """
    if selection_type == 'option':
        info_txt = "Выберите нужную команду введя её номер: "
        warning_txt = "Вы ввели неверную команду. Попробуйте ещё раз."
    elif selection_type == 'task_id':
        info_txt = "\nВведите ID задачи: "
        warning_txt = "Вы ввели неверный ID. Попробуйте ещё раз."
    else:
        info_txt = "\nВведите идентификатор поля для редактирования: "
        warning_txt = "Вы ввели неверный идентификатор поля. Попробуйте ещё раз."

    valid_choice = False
    while not valid_choice:  # будет выполняться до тех пор, пока пользователь не введёт корректное значение
        user_input = input(info_txt)
        valid_choice = validate(user_input, ids)
    
        if not valid_choice:
            print(warning_txt, end='\n\n')
    
    return int(user_input)


def assign_id() -> int:
    """
    Присваивает уникальный идентификатор задаче.

    Args:
        None
    Returns:
        int: Уникальный идентификатор задачи.
    """
    new_id = 0

    if len(ids_roster) == 0:    
        new_id = 1
    else:
        new_id = max(ids_roster) + 1

    return new_id


def add_task():
    """
    Добавляет новую задачу в список задач.

    Args:
        None
    Returns:
        None
    """
    print(f"\n{' ДОБАВЛЕНИЕ ЗАДАЧИ (для отмены введите 0) '.center(TXT_MAX_LENGTH, FILLER_SYMBOL)}")

    new_task = dict()
    task_id = assign_id()
    new_task['task_id'] = task_id
    new_task['is_done'] = False

    task_details_count = len(task_details) 
    for ix in range(3, task_details_count+1):
        detail = task_details[ix]['detail']
        caption = task_details[ix]['caption']

        value = input(f"Введите {caption.lower()}: ")
        if value.strip() == '0':
            print("\nДЕЙСТВИЕ БЫЛО ОТМЕНЕНО", end='\n\n')
            input("\nНажмите любую клавишу чтобы продолжить...")
            return
        
        new_task[detail] = value

    tasks[task_id] = new_task
    ids_roster.append(task_id)

    print(f"\nЗАДАЧА {task_id} УСПЕШНО ДОБАВЛЕНА!", end='\n\n')

    menu_caption = menus[2]['caption']
    menu = menus[2]['menu']
    show_menu(menu_caption, menu)
    
    user_choice = get_user_choice(menu.keys())
    if user_choice == 1:
        add_task()


def check_tasks_existence(tasks_dict: dict = tasks, tasks_type: str = 'список задач') -> bool:
    """
    Проверяет существуют ли задачи в списке задач.

    Args:
        tasks_dict (dict, optional): Словарь задач. Дефолтное значение tasks.
        tasks_type (str, optional): Тип задач. Дефолтное значение 'список задач'.
    Returns:
        bool: Результат проверки.
    """
    tasks_count = len(tasks_dict)
    tasks_exist = bool(tasks_count)
    
    if not tasks_exist:
        print("\nВыбранное действие не может быть выполнено")
        print(f"так как ваш {tasks_type} пуст")
        input("\nНажмите любую клавишу чтобы продолжить...")
    
    return tasks_exist


def show_tasks(is_done: bool = False):
    """
    Выводит список задач на консоль.

    Args:
        is_done (bool, optional): Флаг выполненности задачи. Дефолтное значение False.
    Returns:
        None
    """
    tasks_filtered = {key: value for key, value in tasks.items() if value['is_done'] == is_done}
    tasks_exist = check_tasks_existence(tasks_filtered, f"список {'выполненных' if is_done else 'активных'} задач")

    if tasks_exist:
        print(f"\n{' СПИСОК ВАШИХ ЗАДАЧ '.center(TXT_MAX_LENGTH, FILLER_SYMBOL)}")
        
        for key, value in tasks_filtered.items():
            print(f"{key}. {value['title']}")    

        input("\nНажмите любую клавишу чтобы продолжить...")


def show_task_details(target_task: dict, show_status: bool = True):
    """
    Выводит детали задачи на консоль.

    Args:
        target_task (dict): Выбранная пользователем задача.
        show_status (bool, optional): Флаг вывода статуса задачи. Дефолтное значение True.    
    Returns:
        None
    """
    title = f' ЗАДАЧА С ID = {target_task['task_id']} '
    print(f"\n{title.center(TXT_MAX_LENGTH, FILLER_SYMBOL)}")
    
    task_details_count = len(task_details) 
    for ix in range(3, task_details_count+1):
        caption = task_details[ix]['caption']
        detail = task_details[ix]['detail']
        print(f"{caption} ({ix}): {target_task[detail]}")

    if show_status:
        is_done = target_task['is_done']
        status_color = f"{'\033[92m' if is_done else '\033[91m'}"
        status_txt = f"{status_color}{'выполнено' if target_task['is_done'] else 'не выполнено'}\033[00m"
        print(f"{task_details[2]['caption']} (2): {status_txt}")


def show_task_by_id():
    """
    Отображает выбранную пользователем задачу.

    Args:
        None
    Returns:
        None
    """
    tasks_exist = check_tasks_existence()
    if tasks_exist:
        target_id = get_user_choice(tasks.keys(), selection_type='task_id')

        if target_id == 0:
            print("\nДЕЙСТВИЕ БЫЛО ОТМЕНЕНО", end='\n\n')
            input("\nНажмите любую клавишу чтобы продолжить...")
            return

        target_task = tasks[target_id]
        show_task_details(target_task)

        input("\nНажмите любую клавишу чтобы продолжить...")


def edit_task():
    """
    Редактирует выбранную пользователем задачу.

    Args:
        None
    Returns:
        None
    """
    tasks_exist = check_tasks_existence()
    if tasks_exist:
        target_id = get_user_choice(tasks.keys(), selection_type='task_id')
        if target_id == 0:
            print("\nДЕЙСТВИЕ БЫЛО ОТМЕНЕНО", end='\n\n')
            input("\nНажмите любую клавишу чтобы продолжить...")
            return

        target_task = tasks[target_id]
        show_task_details(target_task, show_status=False)

        task_details_count = len(task_details)
        task_ixs = list(range(3, task_details_count+1))
        user_choice = get_user_choice(task_ixs, selection_type='detail_id')
        if user_choice == 0:
            print("\nДЕЙСТВИЕ БЫЛО ОТМЕНЕНО", end='\n\n')
            input("\nНажмите любую клавишу чтобы продолжить...")
            return

        target_detail = task_details[user_choice]['detail']
        target_caption = task_details[user_choice]['caption']

        updated_value = input(f"Введите новое значение для {target_caption.lower()}: ")
        if updated_value.strip() == '0':
            print("\nДЕЙСТВИЕ БЫЛО ОТМЕНЕНО", end='\n\n')
            input("\nНажмите любую клавишу чтобы продолжить...")
            return

        target_task[target_detail] = updated_value

        print(f"\nЗАДАЧА {target_id} УСПЕШНО ОБНОВЛЕНА!")
        input("\nНажмите любую клавишу чтобы продолжить...")


def ask_confirmation():
    """
    Запрашивает подтверждение действия у пользователя.

    Args:
        None
    Returns:
        bool: Результат подтверждения.
    """
    show_menu('ВЫ УВЕРЕНЫ?', {0: 'Нет', 1: 'Да'})
    user_choise = get_user_choice([0, 1])
    is_confirmed = False if user_choise == 0 else True 
    if not is_confirmed:
        print("\nДЕЙСТВИЕ БЫЛО ОТМЕНЕНО")
    
    return is_confirmed


def remove_task():
    """
    Удаляет задачи из списка по выбору пользователя.

    Args:
        None
    Returns:
        None
    """
    tasks_exist = check_tasks_existence()
    if tasks_exist:

        menu_caption = menus[3]['caption']
        menu = menus[3]['menu']
        show_menu(menu_caption, menu)
        user_choice = get_user_choice(menu.keys())

        if user_choice == 1:
            print(f"\n{' УДАЛЕНИЕ ЗАДАЧИ ПО ID '.center(TXT_MAX_LENGTH, FILLER_SYMBOL)}")
            target_id = get_user_choice(tasks.keys(), selection_type='task_id')
            if target_id == 0:
                print("\nДЕЙСТВИЕ БЫЛО ОТМЕНЕНО", end='\n\n')
                input("\nНажмите любую клавишу чтобы продолжить...")
                return
            
            is_confirmed = ask_confirmation()
            if is_confirmed:
                del tasks[target_id]
                print(f"\nЗАДАЧА {target_id} УСПЕШНО УДАЛЕНА!")
            
        elif user_choice == 2:
            
            is_confirmed = ask_confirmation()
            if is_confirmed:
                tasks.clear()
                print("\nВСЕ ЗАДАЧИ УСПЕШНО УДАЛЕНЫ!")
        
        else:
            return 

        input("\nНажмите любую клавишу чтобы продолжить...")


def change_task_status(is_done: bool = False):
    """
    Изменяет статус выбранной пользователем задачи.

    Args:
        is_done (bool, optional): Флаг выполненности задачи. Дефолтное значение False.
    Returns:
        None
    """
    tasks_filtered = {key: value for key, value in tasks.items() if value['is_done'] == is_done}
    tasks_exist = check_tasks_existence(tasks_filtered, f"список {'выполненных' if is_done else 'активных'} задач")

    if tasks_exist:
        task_ids = list(tasks_filtered.keys())
        target_id = get_user_choice(task_ids, selection_type='task_id')
        if target_id == 0:
            print("\nДЕЙСТВИЕ БЫЛО ОТМЕНЕНО", end='\n\n')
            input("\nНажмите любую клавишу чтобы продолжить...")
            return

        target_task = tasks_filtered[target_id]
        target_task['is_done'] = not is_done

        if is_done:
            print(f"\nЗАДАЧА {target_id} ПЕРЕМЕЩЕНА В СПИСОК ВЫПОЛНЕННЫХ!")
        else:
            print(f"\nЗАДАЧА {target_id} ПЕРЕМЕЩЕНА В СПИСОК АКТИВНЫХ!")

        input("\nНажмите любую клавишу чтобы продолжить...")


def main():
    """
    Мастер-функция для работы с приложением.

    Args:
        None
    Returns:
        None
    """
    print("\nДобро пожаловать в Todo-List-App!", end='\n\n')

    while True:
        menu_caption = menus[1]['caption']
        menu = menus[1]['menu']
        show_menu(menu_caption, menu)
        user_choice = get_user_choice(menu.keys())
        
        match user_choice:
            case 0:
                break
            case 1:
                add_task()
            case 2:
                show_tasks()
            case 3:
                show_tasks(True)
            case 4:
                show_task_by_id()
            case 5:
                edit_task()
            case 6:
                remove_task()
            case 7:
                change_task_status()
            case 8:
                change_task_status(is_done=True)


if __name__ == '__main__':
    main()