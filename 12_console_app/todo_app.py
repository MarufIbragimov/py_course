# import sys

TXT_MAX_LENGTH: int = 50
FILLER_SYMBOL: str = '*'
tasks: dict[int, dict] = {}
info_txt = "Выберите нужную команду введя её номер: "

main_menu: dict[int, str] = {
    1: 'Добавить новую задачу',
    2: 'Вывести список задач',
    3: 'Редактировать задачу',
    4: 'Вывести задачу по ID',
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

menus: dict[int, dict[str, dict[int, str]]] = {
    1: {'caption': 'ГЛАВНОЕ МЕНЮ', 'menu': main_menu},
    2: {'caption': 'МЕНЮ', 'menu': task_addition_submenu}
}


def show_menu(menu_id: int):
    menu_caption = menus[menu_id]['caption']
    menu_caption = f"  {menu_caption}  "
    menu = menus[menu_id]['menu']

    print(f"\n{menu_caption.center(TXT_MAX_LENGTH, FILLER_SYMBOL)}")
    for key, value in menu.items():
        print(f"{key}. {value}")
    print('\n')
    

def validate(user_input, menu_id: int) -> bool:
    user_input = user_input.strip()
    menu = menus[menu_id]['menu']

    is_valid = user_input.isnumeric() and int(user_input) in menu.keys()
    return is_valid
    

def select_action(menu_id: int) -> int:
    show_menu(menu_id)

    valid_choice = False
    while not valid_choice:
        selected_option = input(info_txt)
        valid_choice = validate(selected_option, menu_id)
    
        if not valid_choice:
            warning_txt = "Вы ввели неверную команду. Попробуйте ещё раз."
            print(warning_txt, end='\n\n')
    
    return int(selected_option)


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

    user_choice = select_action(2)
    if user_choice == 1:
        add_task()


def print_tasks():
    print(f"\n{' СПИСОК ВАШИХ ЗАДАЧ '.center(TXT_MAX_LENGTH, FILLER_SYMBOL)}")
    
    if len(tasks) == 0:
        print("Ваш список задач пуст")
    else:
        for key, value in tasks.items():
            print(f"{key}. {value['title']}")    

    input("\nНажмите любую клавишу чтобы продолжить...")


def main():

    print("\nДобро пожаловать в Todo-List-App!", end='\n\n')

    while True:
        user_choice = select_action(1)
        
        match user_choice:
            case 0:
                break
            case 1:
                add_task()
            case 2:
                print_tasks()
            case _:
                print("Отлично", end='\n\n')

        
        # options[user_choice]




main()