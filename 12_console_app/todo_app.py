# import sys

TXT_MAX_LENGTH: int = 50
FILLER_SYMBOL: str = '*'
tasks: dict[int, str] = {}


MAIN_MENU: dict[int, str] = {
    1: 'Добавить новую задачу',
    2: 'Вывести список задач',
    3: 'Редактировать задачу',
    4: 'Вывести задачу по ID',
    0: 'Выход'
}

TASK_DETAILS: dict[int, dict[str, str]] = {
    1: {'option': 'task_id', 'caption': 'id задачи'},
    2: {'option': 'is_done', 'caption': 'статус задачи'},
    3: {'option': 'title', 'caption': 'название задачи'},
    4: {'option': 'description', 'caption': 'описание задачи'},
    5: {'option': 'deadline', 'caption': 'дедлайн задачи'},
    6: {'option': 'priority', 'caption': 'приоритет задачи'},
}


def assign_id() -> int:
    
    new_id = 0

    if len(tasks) == 0:    
        new_id = 1
    else:
        new_id = max(tasks.keys()) + 1

    return new_id


def add_task():
    
    print(f"{'Добавление задачи'.center(TXT_MAX_LENGTH, FILLER_SYMBOL)}")

    new_task = dict()
    task_id = assign_id()
    new_task['task_id'] = task_id
    new_task['is_done'] = False

    task_details_count = len(TASK_DETAILS) 
    for ix in range(3, task_details_count):
        detail = TASK_DETAILS[ix]
        option = detail['option']
        caption = detail['caption']

        value = input(f"Введите {caption}: ")
        new_task[option] = value

    tasks[task_id] = new_task

    print(f"--------------Задача {task_id} успешно  добавлена--------------")



def show_menu():
    print(f"{'Главное меню'.center(TXT_MAX_LENGTH, FILLER_SYMBOL)}")
    print(f"1. {MAIN_MENU[1]}")
    print(f"2. {MAIN_MENU[2]}")
    print(f"3. {MAIN_MENU[3]}")
    print(f"4. {MAIN_MENU[4]}")
    print(f"0. {MAIN_MENU[0]}", end="\n\n") 
    

def validate(user_input) -> bool:
    user_input = user_input.strip()
    is_valid = user_input.isnumeric() and int(user_input) in MAIN_MENU.keys()
    return is_valid
    

def select_action() -> int:
    info_txt = "Выберите нужную команду введя её номер: "
    show_menu()

    valid_choice = False
    while not valid_choice:
        selected_option = input(info_txt)
        valid_choice = validate(selected_option)
    
        if not valid_choice:
            warning_txt = "Вы ввели неверную команду. Попробуйте ещё раз."
            print(warning_txt, end='\n\n')
    
    return int(selected_option)


def main():

    print("\nДобро пожаловать в Todo-List-App!", end='\n\n')

    while True:
        user_choice = select_action()
        
        match user_choice:
            case 0:
                break
            case 1:
                add_task()
            case _:
                print("Отлично", end='\n\n')

        
        # options[user_choice]


main()