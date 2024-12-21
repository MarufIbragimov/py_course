# import sys

TXT_MAX_LENGTH: int = 50
FILLER_SYMBOL: str = '*'
tasks: dict[int, dict] = {}


main_menu: dict[int, str] = {
    1: 'Добавить новую задачу',
    2: 'Вывести список активных задач',
    3: 'Вывести список выполненных задач',
    4: 'Редактировать задачу',
    5: 'Вывести задачу по ID',
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

menus: dict[int, dict] = {
    1: {'caption': 'ГЛАВНОЕ МЕНЮ', 'menu': main_menu},
    2: {'caption': 'МЕНЮ', 'menu': task_addition_submenu}
}


def show_menu(menu_caption: str, menu: dict[int, str]):
    
    menu_caption = f"  {menu_caption}  "  
        
    print(f"\n{menu_caption.center(TXT_MAX_LENGTH, FILLER_SYMBOL)}")
    for key, value in menu.items():
        print(f"{key}. {value}")
    print('\n')
    

def validate(user_input, ids: list) -> bool:
    user_input = user_input.strip()
    
    is_valid = user_input.isnumeric() and int(user_input) in ids
    return is_valid
    

def get_user_choice(ids: list, is_option_selection: bool = True) -> int:

    if is_option_selection:
        info_txt = "Выберите нужную команду введя её номер: "
        warning_txt = "Вы ввели неверную команду. Попробуйте ещё раз."
    else:
        info_txt = "\nВведите ID задачи: "
        warning_txt = "Вы ввели неверный ID. Попробуйте ещё раз."

    valid_choice = False
    while not valid_choice:
        user_input = input(info_txt)
        valid_choice = validate(user_input, ids)
    
        if not valid_choice:
            print(warning_txt, end='\n\n')
    
    return int(user_input)


def assign_id() -> int:
    
    new_id = 0

    if len(tasks) == 0:    
        new_id = 1
    else:
        new_id = max(tasks.keys()) + 1

    return new_id


def add_task():
    
    print(f"\n{' ДОБАВЛЕНИЕ ЗАДАЧИ (для отмены введите 0) '.center(TXT_MAX_LENGTH, FILLER_SYMBOL)}")

    new_task = dict()
    task_id = assign_id()
    new_task['task_id'] = task_id
    new_task['is_done'] = False

    task_details_count = len(task_details) 
    for ix in range(3, task_details_count):
        detail = task_details[ix]['detail']
        caption = task_details[ix]['caption']

        value = input(f"Введите {caption.lower()}: ")
        if value.strip() == '0':
            print("\nДЕЙСТВИЕ БЫЛО ОТМЕНЕНО", end='\n\n')
            return
        
        new_task[detail] = value

    tasks[task_id] = new_task

    print(f"\nЗАДАЧА {task_id} УСПЕШНО ДОБАВЛЕНА!", end='\n\n')

    menu_caption = menus[2]['caption']
    menu = menus[2]['menu']
    show_menu(menu_caption, menu)
    
    user_choice = get_user_choice(menu.keys())
    if user_choice == 1:
        add_task()


def show_tasks(is_done: bool = False):
    print(f"\n{' СПИСОК ВАШИХ ЗАДАЧ '.center(TXT_MAX_LENGTH, FILLER_SYMBOL)}")
    
    tasks_to_print = {key: value for key, value in tasks.items() if value['is_done'] == is_done}
    if len(tasks_to_print) == 0:
        print(f"У вас нету {'выполненных' if is_done else 'активных'} задач")
    else:
        for key, value in tasks_to_print.items():
            print(f"{key}. {value['title']}")    

    input("\nНажмите любую клавишу чтобы продолжить...")


def show_task_details(target_task: dict):
    title = f' ЗАДАЧА С ID = {target_task['task_id']} '
    print(f"\n{title.center(TXT_MAX_LENGTH, FILLER_SYMBOL)}")
    
    task_details_count = len(task_details) 
    for ix in range(3, task_details_count):
        caption = task_details[ix]['caption']
        detail = task_details[ix]['detail']
        print(f"{caption}: {target_task[detail]}")

    is_done = target_task['is_done']
    status_color = f"{'\033[92m' if is_done else '\033[91m'}"
    status_txt = f"{status_color}{'выполнено' if target_task['is_done'] else 'не выполнено'}\033[00m"
    print(f"{task_details[2]['caption']}: {status_txt}")


def show_task_by_id():
    target_id = get_user_choice(tasks.keys(), is_option_selection=False)

    target_task = tasks[target_id]
    show_task_details(target_task)

    input("\nНажмите любую клавишу чтобы продолжить...")


def main():

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
                print(f" {'some text'}\033[00m")
            case 5:
                show_task_by_id()
            case _:
                print("Отлично", end='\n\n')

        
        # options[user_choice]




main()