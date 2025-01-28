-- ===***************************************************************=== --

-- ПОВТОРЕНИЕ ПРОЙДЕННОГО МАТЕРИАЛА --

-- PostgreSQL
DROP TABLE projects;
DROP TABLE employees; -- Полное удаление таблицы

CREATE TABLE employees (
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор
    first_name VARCHAR(100) NOT NULL, -- Имя (до 100 символов)
    last_name VARCHAR(100) NOT NULL, -- Фамилия (до 100 символов)
    email VARCHAR(320) UNIQUE NOT NULL, -- Электронная почта (максимум 320 символов: 64 символа для локальной части + 1 символ для @ + 255 символов для домена)
    hire_date DATE NOT NULL, -- Дата найма
    salary NUMERIC(10, 2) NOT NULL, -- Зарплата. Максимальное значение: 99999999.99 (8 цифр до запятой и 2 после запятой).
    department VARCHAR(50) NOT NULL DEFAULT 'Unknown', -- Отдел (по умолчанию Unknown)
    is_active BOOLEAN DEFAULT TRUE, -- Статус активности
    created_at TIMESTAMP DEFAULT NOW(), -- Время создания записи
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Время последнего обновления записи
    is_deleted BOOLEAN DEFAULT FALSE, -- Флаг мягкого удаления
    deleted_at TIMESTAMP -- Время мягкого удаления записи
);

-- Добавление тестовых данных
INSERT INTO employees (first_name, last_name, email, hire_date, salary, department)
VALUES
    ('Alice', 'Johnson', 'alice.johnson@example.com', '2023-01-15', 5000.00, 'HR'),
    ('Bob', 'Smith', 'bob.smith@example.com', '2022-05-20', 6000.00, 'Engineering'),
    ('Charlie', 'Brown', 'charlie.brown@example.com', '2021-03-10', 5500.00, 'Finance'),
    ('Diana', 'Prince', 'diana.prince@example.com', '2020-12-01', 7000.00, 'Marketing'),
    ('Evan', 'Taylor', 'evan.taylor@example.com', '2023-06-25', 4800.00, 'IT'),
    ('Fiona', 'Davis', 'fiona.davis@example.com', '2021-08-15', 5300.00, 'HR'),
    ('George', 'Harris', 'george.harris@example.com', '2019-07-30', 6200.00, 'Engineering'),
    ('Hannah', 'Moore', 'hannah.moore@example.com', '2023-02-18', 5900.00, 'Finance'),
    ('Ian', 'Wright', 'ian.wright@example.com', '2022-11-10', 6700.00, 'Marketing'),
    ('Jane', 'Doe', 'jane.doe@example.com', '2021-05-22', 5200.00, 'IT'),
    ('Kevin', 'Clark', 'kevin.clark@example.com', '2020-09-11', 4900.00, 'HR'),
    ('Lara', 'Wilson', 'lara.wilson@example.com', '2023-01-30', 5800.00, 'Engineering'),
    ('Megan', 'Carter', 'megan.carter@example.com', '2022-04-15', 5600.00, 'Finance'),
    ('Nathan', 'Lee', 'nathan.lee@example.com', '2021-10-12', 6500.00, 'Marketing'),
    ('Olivia', 'Hall', 'olivia.hall@example.com', '2020-06-09', 5100.00, 'IT'),
    ('Paul', 'Allen', 'paul.allen@example.com', '2023-03-15', 6300.00, 'HR'),
    ('Quinn', 'Walker', 'quinn.walker@example.com', '2022-07-20', 5400.00, 'Engineering'),
    ('Rachel', 'Young', 'rachel.young@example.com', '2021-12-25', 6100.00, 'Finance'),
    ('Steven', 'King', 'steven.king@example.com', '2020-11-14', 5800.00, 'Marketing'),
    ('Tina', 'Hill', 'tina.hill@example.com', '2023-05-05', 5000.00, 'IT'),
    ('Uma', 'Green', 'uma.green@example.com', '2022-02-10', 5200.00, 'HR'),
    ('Victor', 'Adams', 'victor.adams@example.com', '2021-07-30', 6400.00, 'Engineering'),
    ('Wendy', 'Collins', 'wendy.collins@example.com', '2020-10-18', 5600.00, 'Finance'),
    ('Xavier', 'Bennett', 'xavier.bennett@example.com', '2023-08-25', 6800.00, 'Marketing'),
    ('Yara', 'Ford', 'yara.ford@example.com', '2022-01-11', 4900.00, 'IT'),
    ('Zach', 'Evans', 'zach.evans@example.com', '2021-09-19', 5300.00, 'HR'),
    ('Ava', 'Roberts', 'ava.roberts@example.com', '2023-04-08', 6200.00, 'Engineering'),
    ('Ben', 'Morris', 'ben.morris@example.com', '2022-03-14', 5800.00, 'Finance'),
    ('Chloe', 'Hughes', 'chloe.hughes@example.com', '2021-11-20', 6100.00, 'Marketing'),
    ('David', 'Gray', 'david.gray@example.com', '2020-05-30', 5700.00, 'IT'),
    -- Новые записи с одинаковыми именами, но разными фамилиями
    ('Alice', 'Smith', 'alice.smith@example.com', '2023-02-01', 5100.00, 'HR'),
    ('Bob', 'Jones', 'bob.jones@example.com', '2022-12-01', 6200.00, 'Marketing'),
    ('Bob', 'Ford', 'bob.ford@example.com', '2023-05-20', 6500.00, 'Marketing');

-- Полное удаление записей без сброса автоинкремента (SERIAL)
DELETE FROM employees;

-- Полное удаление записей с сбросом автоинкремента (SERIAL):
TRUNCATE TABLE employees RESTART IDENTITY;

-- Получение всех записей
SELECT * FROM employees;

-- Получение всех записей с упорядочением по зарплате:
SELECT * FROM employees
    ORDER BY salary;
SELECT * FROM employees
    ORDER BY salary DESC;

-- Получение всех записей, зарплата которых больше или равна 5500.00:
SELECT * FROM employees
    WHERE salary >= 6000.00
    ORDER BY salary DESC;

-- Получение всех записей, где зарплата больше или равна 5500 и отдел — 'HR':
SELECT * FROM employees
    WHERE salary >= 5500
    AND department = 'HR';

-- Получение всех записей, где зарплата меньше 5000 или сотрудник работает в отделе 'Finance':
SELECT * FROM employees
    WHERE salary < 5000
    OR department = 'Finance';

-- Получение всех записей, где сотрудник НЕ работает в отделе 'Engineering':
SELECT * FROM employees
    WHERE department <> 'Engineering'
    ORDER BY department;
-- или
SELECT * FROM employees
    WHERE department != 'Engineering'
    ORDER BY department;
-- или
SELECT * FROM employees
    WHERE NOT department = 'Engineering'
    ORDER BY department;

-- Комбинированный запрос с AND, OR и NOT:
SELECT * FROM employees
    WHERE (salary > 6000 AND department = 'Marketing')
    OR NOT is_active
    ORDER BY salary;

-- Получение всех записей с датой найма до 2023 года и отделом 'IT':
SELECT * FROM employees
    WHERE hire_date < '2023-01-01'
    AND department = 'IT'
    ORDER BY hire_date;
SELECT * FROM employees
    WHERE department = 'IT'
    ORDER BY hire_date;

-- Получение всех записей, у которых значение deleted_at установлено (запись удалена):
SELECT * FROM employees
    WHERE deleted_at IS NOT NULL;

-- Получение всех записей, у которых deleted_at равно NULL (запись активна):
SELECT * FROM employees
    WHERE deleted_at IS NULL;


-- Установить флаг is_deleted и дату удаления для определённого сотрудника:
UPDATE employees
    SET is_deleted = TRUE, -- Устанавливаем флаг мягкого удаления
        deleted_at = NOW() -- Добавляем текущую дату и время в поле deleted_at
    WHERE id = 1; -- Указываем ID сотрудника

-- Обновить сразу несколько записей, где отдел равен 'Finance':
UPDATE employees
    SET is_deleted = TRUE, -- Устанавливаем флаг мягкого удаления
        deleted_at = NOW() -- Добавляем текущую дату и время в поле deleted_at
    WHERE department = 'Finance';

-- Мягкое удаление всех записей, у которых зарплата меньше 5000:
UPDATE employees
    SET is_deleted = TRUE, -- Устанавливаем флаг мягкого удаления
        deleted_at = NOW() -- Добавляем текущую дату и время в поле deleted_at
    WHERE salary < 50000;

-- Увеличим зарплату сотрудника с ID 1 на 10%
UPDATE employees
    SET salary = salary * 1.10 -- Увеличиваем зарплату на 10%
    WHERE id = 1;

-- Уменьшим зарплату на 5% для всех сотрудников из отдела 'Marketing'
UPDATE employees
    SET salary = salary * 0.95 -- Уменьшаем зарплату на 5%
    WHERE department = 'Marketing';

-- Установим зарплату 60000 для всех сотрудников, у которых она ниже этого значения
UPDATE employees
    SET salary = 11111 -- Устанавливаем фиксированную зарплату
    WHERE salary < 5000;

-- Удаляем сотрудника с ID 1.
DELETE FROM employees
    WHERE id = 1;

-- Удаление всех сотрудников из отдела 'HR':
DELETE FROM employees
    WHERE department = 'HR';

-- === ********************************************************************* === ---
-- === ********************************************************************* === ---
-- === ********************************************************************* === ---

-- НОВЫЕ ТЕМЫ --

-- Простая выборка данных
SELECT * FROM employees;

-- Порядок сортировки NULL значений
SELECT * FROM employees
    ORDER BY deleted_at NULLS FIRST; -- NULL значения будут в начале
SELECT * FROM employees
    ORDER BY deleted_at NULLS LAST; -- NULL значения будут в конце

-- Выборка конкретных колонок:
SELECT first_name, last_name
    FROM employees;

-- Переименование колонок (AS):
SELECT first_name AS имя, salary AS зарплата
    FROM employees;

-- Поиск NULL-значений:
SELECT first_name AS имя, deleted_at
    FROM employees
    WHERE deleted_at IS NULL;

-- Пример, где применяются базовые математические операции для модификации данных в выборке:
SELECT first_name, salary, salary * 1.5 AS salary_with_bonus
    FROM employees; -- Увеличение зарплаты на 50% в выборке

-- Ограничение количества строк (LIMIT и OFFSET)
-- Вывод 5 записей:
SELECT * FROM employees
    LIMIT 5;

-- Пропуск первых 3 строк и вывод следующих 5:
SELECT * FROM employees
    LIMIT 5 OFFSET 3;

-- Выборка для страниц
SELECT * FROM employees
    LIMIT 10 OFFSET 0;
SELECT * FROM employees
    LIMIT 10 OFFSET 10;
SELECT * FROM employees
    LIMIT 10 OFFSET 20;
-- limit_str = 10
-- offset_str = 0
-- offset_str += limit_str

-- Поиск с использованием LIKE
-- Имена, начинающиеся с буквы 'A':
SELECT * FROM employees
    WHERE first_name LIKE 'A%';
-- Электронная почта с доменом "example.com":
SELECT * FROM employees
    WHERE email LIKE '%@example.com';
-- Поиск всех совпадений:
SELECT * FROM employees
    WHERE email LIKE '%ll%';

-- Пример сравнения строк с учетом регистра (ILIKE для нечувствительности к регистру):
SELECT * FROM employees
    WHERE first_name ILIKE 'a%'; -- Имена, начинающиеся с буквы 'A' (без учета регистра)
SELECT * FROM employees
    WHERE first_name ILIKE '%A'; -- Имена, заканчивающиеся на букву 'A' (без учета регистра)
SELECT * FROM employees
    WHERE first_name ILIKE '%nA%'; -- Имена, содержащие последовательность букв 'nA' (без учета регистра)
SELECT * FROM employees
    WHERE first_name ILIKE '%hA%aH%'; -- Имена, содержащие две последовательности (без учета регистра)
SELECT * FROM employees
    WHERE first_name ILIKE '%LI%E%'; -- Имена, содержащие две последовательности (без учета регистра)

-- Выборка сотрудников, где отдел равен 'HR', 'Finance':
SELECT * FROM employees
    WHERE department IN ('HR', 'Finance');
-- Выборка сотрудников с определёнными ID:
SELECT * FROM employees
    WHERE id IN (1, 2, 3);
-- Выборка сотрудников с зарплатой 5000, 5500 или 6000:
SELECT * FROM employees
    WHERE salary IN (5000, 5500, 6000);

-- Поиск в диапазоне значений (BETWEEN)
-- Сотрудники с зарплатой от 5000 до 7000:
SELECT * FROM employees
    WHERE salary BETWEEN 5000 AND 5200
    ORDER BY SALARY;

-- Работа с датами
-- Сотрудники, нанятые в последние 2 года:
SELECT * FROM employees
    WHERE hire_date > CURRENT_DATE - INTERVAL '2 years';
SELECT * FROM employees
    WHERE hire_date > CURRENT_DATE - INTERVAL '1.5 years';
-- Сотрудники, нанятые в конкретный месяц:
SELECT * FROM employees
    WHERE EXTRACT(MONTH FROM hire_date) = 1; -- Январь
SELECT EXTRACT(MONTH FROM hire_date) FROM employees;
SELECT EXTRACT(YEAR FROM hire_date), first_name, last_name
    FROM employees
    ORDER BY exctract;
SELECT EXTRACT(YEAR FROM hire_date) AS год_найма, first_name, last_name
    FROM employees
    ORDER BY год_найма;

-- Агрегатные функции
-- Подсчёт количества сотрудников:
SELECT COUNT(*) FROM employees;

-- Минимальная, максимальная, средняя зарплата:
SELECT MIN(salary), MAX(salary), AVG(salary)
    FROM employees;
SELECT MIN(salary) AS Минимальная, MAX(salary) AS Максимальная, AVG(salary) AS Средняя
    FROM employees;

-- Общая сумма зарплат:
SELECT SUM(salary)
    FROM employees;
SELECT SUM(salary)
    FROM employees
    WHERE department = 'HR';

-- Группировка данных (GROUP BY)
-- Количество сотрудников в каждом отделе:
SELECT department, COUNT(*)
    FROM employees
    GROUP BY department;

-- Средняя зарплата по отделам:
SELECT department, AVG(salary)
    FROM employees
    GROUP BY department;

-- Фильтрация групп (HAVING)
-- Отделы, где более 3 сотрудников:
SELECT department, COUNT(*) 
    FROM employees 
    GROUP BY department 
    HAVING COUNT(*) > 3;

-- Подзапрос в SELECT
-- Общий доход сотрудников по отделу:
SELECT department, 
       (SELECT SUM(salary) 
        FROM employees e2 
        WHERE e2.department = e1.department) AS total_salary
    FROM employees e1
    GROUP BY department;

-- Подзапрос в WHERE
-- Сотрудники с зарплатой выше средней:
SELECT last_name, first_name, salary FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees)
    ORDER BY salary;
SELECT AVG(salary)
    FROM employees;
-- Сотрудники с максимальной зарплатой в каждом отделе:
SELECT e1.first_name, e1.salary, e1.department
    FROM employees e1
    WHERE salary = (SELECT MAX(e2.salary)
                    FROM employees e2
                    WHERE e2.department = e1.department);

-- Другие полезные операции
-- DISTINCT (удаление дублирующихся значений):
SELECT DISTINCT department FROM employees;
SELECT department FROM employees;

-- CASE (условные выражения):
-- Категоризация зарплат:
SELECT first_name, 
       salary, 
       CASE 
           WHEN salary < 5000 THEN 'Low' -- Когда з/п < 5000, тогда Low
           WHEN salary BETWEEN 5000 AND 6999 THEN 'Medium'
           ELSE 'High'
       END AS salary_category
    FROM employees
    ORDER BY salary DESC;

-- Использование выражения COALESCE
-- Замена NULL значений на значение по умолчанию:
SELECT first_name, COALESCE(deleted_at, 'Не удалено') AS status
    FROM employees;
SELECT first_name, 
    COALESCE(deleted_at, CURRENT_TIMESTAMP) AS status
    FROM employees;
SELECT first_name, 
    COALESCE(TO_CHAR(deleted_at, 'YYYY-MM-DD HH24:MI:SS'), 'Не удалено') AS status
    FROM employees;
-- Альтернатива
SELECT first_name, 
       CASE 
           WHEN deleted_at IS NULL THEN 'Не удалено'
           ELSE TO_CHAR(deleted_at, 'YYYY-MM-DD HH24:MI:SS')
       END AS status
FROM employees;

-- === ********************************************************************* === ---

-- UNION и UNION ALL
-- Используются для объединения результатов нескольких запросов.

-- UNION:
-- Убирает дубликаты в результирующем наборе.
SELECT first_name, department FROM employees
    WHERE department = 'HR'
UNION
SELECT first_name, department FROM employees
    WHERE department = 'Marketing'
ORDER BY first_name;

-- UNION ALL:
-- Сохраняет дубликаты.
SELECT first_name, department FROM employees
    WHERE department = 'HR'
UNION ALL
SELECT first_name, department FROM employees
    WHERE department = 'Marketing'
ORDER BY first_name;

SELECT first_name, last_name, department FROM employees
    WHERE department IN ('HR', 'Marketing')
    ORDER BY first_name, department;

-- INTERSECT:
-- Возвращает только те строки, которые присутствуют во всех запросах.
SELECT first_name, department, salary FROM employees
    WHERE department = 'HR'
INTERSECT
SELECT first_name, department, salary FROM employees
    WHERE salary > 5500;

SELECT first_name, department, salary FROM employees
    WHERE department = 'HR';
SELECT first_name, department, salary FROM employees
    WHERE salary > 5500;

-- EXCEPT:
-- Возвращает строки из первого запроса, которых нет во втором.
SELECT first_name FROM employees
    WHERE department = 'HR'
EXCEPT
SELECT first_name FROM employees
    WHERE salary < 5000;

-- EXCEPT ALL:
-- Возвращает все строки из первого запроса, которых нет во втором.
SELECT first_name, department, salary FROM employees
    WHERE department = 'HR'
EXCEPT ALL
SELECT first_name, department, salary FROM employees
    WHERE salary < 5000;

-- INTERSECT ALL:
-- Возвращает все строки, которые есть в обоих запросах.
SELECT first_name FROM employees
    WHERE department = 'HR'
INTERSECT ALL
SELECT first_name FROM employees
    WHERE salary > 5000;
    
-- === ********************************************************************* === ---
-- === ********************************************************************* === ---
-- === ********************************************************************* === ---

-- Оостаются только JOIN (соединения таблиц). Это включает:

-- INNER JOIN:
-- Только совпадающие записи.

-- LEFT JOIN:
-- Все записи из левой таблицы и совпадающие из правой.

-- RIGHT JOIN:
-- Все записи из правой таблицы и совпадающие из левой.

-- FULL OUTER JOIN:
-- Все записи из обеих таблиц.

-- SELF JOIN:
-- Соединение таблицы с самой собой.

-- CROSS JOIN:
-- Декартово произведение.

-- Неявные соединения:
-- Использование WHERE вместо ON.

-- === *********************************************************************************************************************** === --
-- === *********************************************************************************************************************** === --
-- === *********************************************************************************************************************** === --

-- ---------------- --
-- Домашнее задание --
-- ---------------- --

-- Часть 1: Базовые запросы
-- Выберите всех сотрудников, у которых department равен 'Engineering', и отсортируйте их по зарплате в порядке убывания.
-- Найдите сотрудников, чья зарплата равна 5000 или 6000.
-- Выведите сотрудников, у которых поле deleted_at равно NULL, вместе с их именами и датой найма.
-- Выберите первых 7 сотрудников, пропустив первых 3.

-- Часть 2: Работа с LIKE и ILIKE
-- Найдите всех сотрудников, чьё имя начинается с буквы 'M'.
-- Выберите сотрудников, чьи имена содержат последовательность 'an' (без учёта регистра).
-- Найдите сотрудников, чья электронная почта заканчивается на 'example.com'.

-- Часть 3: Работа с IN и BETWEEN
-- Найдите всех сотрудников, у которых зарплата находится в диапазоне от 5500 до 7000 включительно.
-- Выберите всех сотрудников, чьи ID находятся в диапазоне от 5 до 15.
-- Найдите всех сотрудников, работающих в отделах 'HR', 'Marketing' и 'Finance'.

-- Часть 4: Работа с датами
-- Выберите сотрудников, нанятых за последние 3 года.
-- Найдите сотрудников, нанятых в марте любого года.
-- Выведите год найма, имя и фамилию всех сотрудников, отсортированных по году найма.

-- Часть 5: Агрегатные функции
-- Найдите минимальную, максимальную и среднюю зарплату среди всех сотрудников.
-- Подсчитайте количество сотрудников в каждом отделе.
-- Выведите общую сумму зарплат для сотрудников отдела 'Engineering'.

-- Часть 6: Подзапросы
-- Найдите сотрудников, у которых зарплата выше средней.
-- Для каждого отдела выведите общую сумму зарплат сотрудников.
-- Найдите сотрудников с максимальной зарплатой в каждом отделе.

-- Часть 7: CASE и группировка
-- Разделите всех сотрудников на три категории зарплат:
-- Low (меньше 5000),
-- Medium (от 5000 до 6999),
-- High (7000 и выше). Выведите их имена, зарплату и категорию.
-- Найдите отделы, где работает более 4 сотрудников.
-- Выведите среднюю зарплату для каждого отдела, но только для отделов, где работает более 3 сотрудников.

-- Часть 8: Дополнительные задания
-- Найдите сотрудников, которые были наняты в течение последних 2 лет и чья зарплата выше средней.
-- Для каждого отдела определите процент сотрудников, чья зарплата выше средней по всем сотрудникам.
-- Используя подзапрос, найдите отделы, где средняя зарплата выше 6000, и выведите названия этих отделов вместе с их средней зарплатой.

-- Часть 9: Работа с объединением запросов (UNION, INTERSECT, EXCEPT)
-- Используя UNION, объедините списки сотрудников из отделов 'HR' и 'Finance', исключая дубликаты. Отсортируйте результат по фамилии.
-- Используя UNION ALL, объедините списки сотрудников из отделов 'HR' и 'Marketing', сохранив дубликаты.
-- Используя INTERSECT, найдите сотрудников из отдела 'HR', чья зарплата превышает 5500.
-- Используя EXCEPT, выберите сотрудников из отдела 'Engineering', которые не работают в отделе 'HR'.
-- Используя INTERSECT ALL, найдите сотрудников, работающих в отделе 'Finance', чьи зарплаты превышают 6000.

-- Примечание:
-- Все запросы необходимо проверить с помощью предоставленной таблицы employees.
-- Убедитесь, что вы понимаете, что происходит на каждом этапе выполнения запроса.

-- P.S.
-- В домашнем задании каждая часть содержит несколько заданий.
-- Если не будете успевать, решите хотя бы по 2 задания из каждой части, чтобы охватить основные темы.
-- Если останется время, выполните все оставшиеся задания, чтобы получить более полное представление по каждому разделу.

-- === ************************************************* === --
-- === ************************************************* === --
-- === ************************************************* === --

-- ========================= --
-- Решение домашнего задания --
-- ========================= --
