# import sys

TXT_MAX_LENGTH: int = 50
FILLER_SYMBOL: str = '*'
tasks: dict[int, dict] = {}
info_txt = "Выберите нужную команду введя её номер: "

main_menu: dict[int, str] = {
    1: 'Добавить новую задачу',
    2: 'Вывести список активных задач',
    3: 'Вывести список выполненных задач',
    4: 'Редактировать задачу',
    5: 'Вывести задачу по ID',
    0: 'Выход'
}

task_details: dict[int, dict[str, str]] = {
    1: {'option': 'task_id', 'caption': 'id задачи'},
    2: {'option': 'is_done', 'caption': 'статус задачи'},
    3: {'option': 'title', 'caption': 'название задачи'},
    4: {'option': 'description', 'caption': 'описание задачи'},
    5: {'option': 'deadline', 'caption': 'дедлайн задачи'},
    6: {'option': 'priority', 'caption': 'приоритет задачи'},
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
    

def get_user_choice(ids: list) -> int:

    valid_choice = False
    while not valid_choice:
        user_input = input(info_txt)
        valid_choice = validate(user_input, ids)
    
        if not valid_choice:
            warning_txt = "Вы ввели неверную команду. Попробуйте ещё раз."
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
        detail = task_details[ix]
        option = detail['option']
        caption = detail['caption']

        value = input(f"Введите {caption}: ")
        if value.strip() == '0':
            print("\nДЕЙСТВИЕ БЫЛО ОТМЕНЕНО", end='\n\n')
            return
        
        new_task[option] = value

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
        for key in tasks:
            if tasks[key]['is_done'] == is_done:
                for key, value in tasks.items():
                    print(f"{key}. {value['title']}")    

    input("\nНажмите любую клавишу чтобы продолжить...")


def show_task_by_id():
    pass


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
            case _:
                print("Отлично", end='\n\n')

        
        # options[user_choice]




main()