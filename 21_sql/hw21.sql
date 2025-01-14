-- -- Домашнее задание -- --

-- Часть 1: Работа с командой UPDATE

-- Изменение данных:
-- Увеличьте зарплату всех сотрудников из отдела Engineering на 15%.
update employees
set salary = salary * 1.15
where
    department = 'Engineering'
;

-- Уменьшите зарплату сотрудников из отдела HR, если их зарплата больше 6000, на 5%.
update employees
set salary = salary * .95
where
    department = 'HR'
    and salary > 6000
;

-- Мягкое удаление:
-- Пометьте как удалённые (is_deleted = TRUE, deleted_at = NOW()) всех сотрудников, которые были наняты до 2021 года.
update employees
set
    is_deleted = True,
    deleted_at = now()
where
    hire_date < date'2021-01-01'
;

-- Обновите поле is_deleted на FALSE для сотрудников, у которых зарплата больше 7000.
update employees
set
    is_deleted = False
where
    salary > 7000
;

-- Часть 2: Работа с командой DELETE

-- Удаление данных:
-- Удалите всех сотрудников из отдела Finance, у которых зарплата меньше 5000.
delete from employees
where
    department = 'Finance'
    and salary < 5000
;

-- Удалите сотрудников, у которых поле is_deleted равно TRUE.
delete from employees
where
    is_deleted = True
;


-- Удаление всех записей:
-- Полностью очистите таблицу с помощью команды TRUNCATE, но только после выполнения всех предыдущих заданий.
truncate employees;


-- Часть 3: Дополнительные задания

-- Комбинирование условий:
-- Обновите зарплату сотрудников из отдела Marketing, нанятых после 2022 года, увеличив её на 10%.
update employees
set
    salary = salary * 1.1
where
    department = 'Marketing'
    and extract('year' from hire_date) > 2022
;

-- Удалите всех сотрудников, у которых отдел равен Unknown или зарплата меньше 4500.
delete from employees
where
    department = 'Unknown'
    or salary < 4500
;


-- Творческое задание:

-- Придумайте и выполните 3 команды UPDATE и 3 команды DELETE, чтобы модифицировать и удалить данные в таблице, используя сложные условия (AND, OR, NOT).

-- ПРОШУ СЧИТАТЬ ЗА 3
update employees
set
    salary = 0,
    is_active = False,
    is_deleted = True,
    deleted_at = current_timestamp
where
    (department = 'IT' or department = 'Engineering') and salary < 5000
;

delete from employees
where
    not hire_date > date'2020-01-01'
;

delete from employees
where
    is_active = False and last_name = 'Taylor'
;

delete from employees
where
    salary > 6500 and first_name != 'Diana'
;

-- Примечание:
-- Проверьте результаты выполнения каждой команды с помощью команды
-- SELECT * FROM employees;
