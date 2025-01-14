---- Что урок включает:

-- Обновление данных (UPDATE):

-- Увеличение/уменьшение зарплат.
-- Использование условий (WHERE).
-- Примеры мягкого удаления (is_deleted, deleted_at).
-- Удаление данных (DELETE):

-- Удаление записей по условиям.
-- Разница между полным удалением (TRUNCATE) и удалением по фильтрам (DELETE).
-- Работа с логическими операторами:

-- Использование AND, OR, NOT в условиях.
-- Примеры с фильтрацией.

-- ===***************************************************************=== --

-- Пример в MySQL
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Уникальный автоинкрементный идентификатор
    first_name VARCHAR(50) NOT NULL, -- Имя
    last_name VARCHAR(50) NOT NULL -- Фамилия
);

-- PostgreSQL
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

-- SERIAL — это INT + AUTO_INCREMENT
-- SERIAL автоматически создаёт числовой столбец типа INT с автоинкрементом.
-- При добавлении новых записей в таблицу значения для столбца SERIAL генерируются автоматически, начиная с 1 (по умолчанию) и увеличиваются на 1 для каждой новой строки.
-- В фоновом режиме PostgreSQL создаёт последовательность (SEQUENCE) для генерации этих значений.

-- PRIMARY KEY — это уникальность + ограничение NULL
-- Столбец, объявленный как PRIMARY KEY, имеет следующие свойства:
-- Уникальность (UNIQUE): значения в этом столбце не могут повторяться.
-- Не допускаются NULL (NOT NULL): каждый ряд обязан иметь значение в этом столбце.
-- PRIMARY KEY автоматически создаёт уникальный индекс для столбца, что ускоряет поиск по этому полю.

-- Максимальная длина электронного адреса составляет 320 символов.
-- Она определяется стандартами RFC 5321 и RFC 5322 и включает в себя две части:
-- Локальная часть (до символа "@") может иметь максимальную длину 64 символа.
-- Доменная часть (после символа "@") может иметь максимальную длину 255 символов.
-- При объединении локальной и доменной частей максимальная длина полного электронного адреса составляет 320 символов.


-- Числовые типы данных

-- serial: представляет автоинкрементирующееся числовое значение, которое занимает 4 байта и может хранить числа от 1 до 2147483647. Значение данного типа образуется путем автоинкремента значения предыдущей строки. Поэтому, как правило, данный тип используется для определения идентификаторов строки.
-- smallserial: представляет автоинкрементирующееся числовое значение, которое занимает 2 байта и может хранить числа от 1 до 32767. Аналог типа serial для небольших чисел.
-- bigserial: представляет автоинкрементирующееся числовое значение, которое занимает 8 байт и может хранить числа от 1 до 9223372036854775807. Аналог типа serial для больших чисел.

-- integer: хранит числа от -2147483648 до +2147483647. Занимает 4 байта. Имеет псевдонимы int и int4.
-- smallint: хранит числа от -32768 до +32767. Занимает 2 байта. Имеет псевдоним int2.
-- bigint: хранит числа от -9223372036854775808 до +9223372036854775807. Занимает 8 байт. Имеет псевдоним int8.

-- numeric: хранит числа с фиксированной точностью, которые могут иметь до 131072 знаков в целой части и до 16383 знаков после запятой.
    -- Данный тип может принимать два параметра precision и scale: numeric(precision, scale).
    -- Параметр precision указывает на максимальное количество цифр, которые может хранить число.
    -- Параметр scale представляет максимальное количество цифр, которые может содержать число после запятой. Это значение должно находиться в диапазоне от 0 до значения параметра precision. По умолчанию оно равно 0.
    -- Например, для числа 23.5141 precision равно 6, а scale - 4.
-- decimal: хранит числа с фиксированной точностью, которые могут иметь до 131072 знаков в целой части и до 16383 знаков в дробной части. То же самое, что и numeric.

-- real: хранит числа с плавающей точкой из диапазона от 1E-37 до 1E+37. Занимает 4 байта. Имеет псевдоним float4.
-- double precision: хранит числа с плавающей точкой из диапазона от 1E-307 до 1E+308. Занимает 8 байт. Имеет псевдоним float8.


-- Краткая разница между этими типами данных:

-- NUMERIC и DECIMAL:
-- Хранят числа с фиксированной точностью (точно заданное количество знаков до и после запятой).
-- Могут иметь до 131072 цифр в целой части и 16383 цифр в дробной части.
-- Они полностью эквивалентны друг другу в PostgreSQL.
-- Применение: для финансовых и точных расчётов, где критична точность.

-- REAL:
-- Хранит числа с плавающей точкой.
-- Занимает 4 байта.
-- Диапазон: от 1E-37 до 1E+37.
-- Менее точный, но занимает меньше памяти.
-- Применение: для научных расчётов или случаев, где важна производительность, а не точность.
-- SELECT 12345.67890123::REAL;
-- Результат: 12345.679 (часть числа теряется из-за ограничения точности).

-- DOUBLE PRECISION:
-- Хранит числа с плавающей точкой.
-- Занимает 8 байт.
-- Диапазон: от 1E-307 до 1E+308.
-- Обеспечивает более высокую точность по сравнению с REAL.
-- Применение: для расчётов, где требуется баланс между точностью и производительностью.

-- Основное отличие:
-- NUMERIC/DECIMAL: точные числа (без ошибок округления).
-- REAL/DOUBLE PRECISION: приближённые числа (с возможными небольшими ошибками округления), но быстрее.


-- Типы данных для работы с датами и временем в PostgreSQL:

-- 1. DATE:
-- Хранит только дату (без времени).
-- Формат: YYYY-MM-DD (например, 2025-01-13).
-- Используется для хранения дат рождения, дат найма и других событий, где время неважно.
-- 2. TIMESTAMP:
-- Хранит дату и время (без часового пояса).
-- Формат: YYYY-MM-DD HH:MI:SS (например, 2025-01-13 14:30:45).
-- Используется для точного фиксирования времени событий.
-- 3. TIMESTAMP WITH TIME ZONE (TIMESTAMPTZ):
-- Хранит дату и время с учётом часового пояса.
-- PostgreSQL автоматически нормализует значение в UTC.
-- Пример: 2025-01-13 14:30:45+03.
-- Используется, если нужно учитывать часовые пояса (например, для глобальных систем).
-- 4. TIME:
-- Хранит только время (без даты).
-- Формат: HH:MI:SS (например, 14:30:45).
-- Используется для хранения времени открытия или закрытия, расписаний.


-- Функции по умолчанию:

-- NOW():
-- Возвращает текущую дату и время (TIMESTAMP WITH TIME ZONE).
-- Пример: DEFAULT NOW().

-- CURRENT_DATE:
-- Возвращает только текущую дату (DATE).
-- Пример: DEFAULT CURRENT_DATE.

-- CURRENT_TIMESTAMP:
-- Возвращает текущую дату и время, аналогично NOW().
-- Пример: DEFAULT CURRENT_TIMESTAMP.

-- LOCALTIMESTAMP:
-- Возвращает текущую дату и время без учёта часового пояса.
-- Пример: DEFAULT LOCALTIMESTAMP.

CREATE TABLE employees (
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор
    first_name VARCHAR(100) NOT NULL, -- Имя (до 100 символов)
    last_name VARCHAR(100) NOT NULL, -- Фамилия (до 100 символов)
    email VARCHAR(320) UNIQUE NOT NULL, -- Электронная почта (максимум 320 символов: 64 символа для локальной части + 1 символ для @ + 255 символов для домена)
    hire_date DATE NOT NULL, -- Дата найма
    salary NUMERIC(10, 2) NOT NULL, -- Зарплата. Максимальное значение: 99999999.99 (8 цифр до запятой и 2 после запятой).
    department VARCHAR(50) NOT NULL DEFAULT 'Unknown', -- Отдел (по умолчанию Unknown)
    is_active BOOLEAN DEFAULT TRUE -- Статус активности
);
-- -----------------------------------
ALTER TABLE employees
ADD COLUMN created_at TIMESTAMP DEFAULT NOW(); -- Время создания записи
ALTER TABLE employees
ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP; -- Время последнего обновления записи
ALTER TABLE employees
ADD COLUMN is_deleted BOOLEAN DEFAULT FALSE; -- Флаг мягкого удаления
ALTER TABLE employees
ADD COLUMN deleted_at TIMESTAMP; -- Время мягкого удаления записи
-- -----------------------------------
ALTER TABLE employees
DROP COLUMN created_at; -- Удаление времени создания записи
ALTER TABLE employees
DROP COLUMN updated_at; -- Удаление времени последнего обновления записи
ALTER TABLE employees
DROP COLUMN is_deleted; -- Удаление столбца is_deleted
ALTER TABLE employees
DROP COLUMN deleted_at; -- Удаление времени мягкого удаления записи
-- -----------------------------------

-- Больше информации здесь:
-- https://metanit.com/sql/postgresql/2.6.php

-- Полное Руководство по PostgreSQL здесь:
-- https://metanit.com/sql/postgresql/


DROP TABLE employees; -- Полное удаление таблицы


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
('David', 'Gray', 'david.gray@example.com', '2020-05-30', 5700.00, 'IT');

-- Полное удаление записей без сброса автоинкремента (SERIAL)
DELETE FROM employees;

-- Полное удаление записей с сбросом автоинкремента (SERIAL):
TRUNCATE TABLE employees RESTART IDENTITY;

-- INSERT INTO employees (first_name, last_name, email, hire_date, salary, department)
INSERT INTO employees (first_name, last_name, email, hire_date, salary, is_active)
VALUES
('Fred', 'Johnson', 'fred.johnson@example.com', '2023-01-15', 77000.00, FALSE),
('Fred', 'Smith', 'fred.smith@example.com', '2022-05-20', 10200.00, FALSE);

-- Получение всех записей
SELECT * FROM employees;

-- Получение всех записей с упорядочением по зарплате в порядке возрастания:
SELECT * FROM employees
    ORDER BY salary;

-- Получение всех записей с упорядочением по зарплате в порядке убывания:
SELECT * FROM employees
    ORDER BY salary DESC;

-- Получение всех записей, зарплата которых больше или равна 5500.00:
SELECT * FROM employees
    WHERE salary >= 6000.00;

-- Фильтрация. WHERE
-- https://metanit.com/sql/postgresql/3.3.php


-- Примеры с логическими операторами:

-- 1. Получение всех записей, где зарплата больше или равна 55000 и отдел — 'HR':
SELECT * FROM employees
    WHERE salary >= 5500
    AND department = 'HR';

-- 2. Получение всех записей, где зарплата меньше 50000 или сотрудник работает в отделе 'Finance':
SELECT * FROM employees
    WHERE salary < 5000
    OR department = 'Finance';

-- 3. Получение всех записей, где сотрудник не работает в отделе 'Engineering':
SELECT * FROM employees
    WHERE department != 'Engineering';
-- или
SELECT * FROM employees
    WHERE NOT department = 'Engineering';

-- Комбинированный запрос с AND, OR и NOT:
SELECT * FROM employees
    WHERE (salary > 6000 AND department = 'Marketing')
    OR NOT is_active;

-- 5. Получение всех записей с датой найма до 2023 года и отделом 'IT':
SELECT * FROM employees
    WHERE hire_date < '2023-01-01'
    AND department = 'IT';
SELECT * FROM employees
    WHERE department = 'IT';

-- Описание логических операторов:
-- AND: оба условия должны быть истинными.
-- OR: хотя бы одно из условий должно быть истинным.
-- NOT: инвертирует условие, превращая истинное в ложное и наоборот.
-- Комбинирование:
-- Скобки (()) используются для группировки условий.


-- IS NULL: Проверяет, имеет ли значение NULL (отсутствие данных).
-- IS NOT NULL: Проверяет, что значение не NULL (данные присутствуют).
-- Примечание: NULL в SQL означает "нет значения", и его нельзя сравнивать с помощью обычных операторов (например, = или !=).


-- Примеры с IS NULL и IS NOT NULL:

-- 1. Получение всех записей, у которых значение deleted_at установлено (запись удалена):
SELECT * FROM employees
    WHERE deleted_at IS NOT NULL;

-- 2. Получение всех записей, у которых deleted_at равно NULL (запись активна):
SELECT * FROM employees
    WHERE deleted_at IS NULL;


-- Пример команды UPDATE, которая используется для установки флага is_deleted и добавления текущей даты в поле deleted_at:

-- Пример обновления записи:

-- 1. Установить флаг is_deleted и дату удаления для определённого сотрудника:
UPDATE employees
    SET is_deleted = TRUE, -- Устанавливаем флаг мягкого удаления
        deleted_at = NOW() -- Добавляем текущую дату и время в поле deleted_at
    WHERE id = 1; -- Указываем ID сотрудника

-- 2. Обновить сразу несколько записей, где отдел равен 'Finance':
UPDATE employees
    SET is_deleted = TRUE, -- Устанавливаем флаг мягкого удаления
        deleted_at = NOW() -- Добавляем текущую дату и время в поле deleted_at
    WHERE department = 'Finance';

-- 3. Мягкое удаление всех записей, у которых зарплата меньше 5000:
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

-- Обновление данных. Команда UPDATE
-- https://metanit.com/sql/postgresql/3.4.php


-- Удаляем сотрудника с ID 1.
DELETE FROM employees
    WHERE id = 1;

-- Удаление всех сотрудников из отдела 'HR':
DELETE FROM employees
    WHERE department = 'HR';

-- --  Удаление записей, у которых флаг is_deleted = TRUE:
-- DELETE FROM employees
--     WHERE is_deleted = TRUE;

-- Удаление данных. Команда DELETE
-- https://metanit.com/sql/postgresql/3.5.php





-- -- Домашнее задание -- --


-- Часть 1: Работа с командой UPDATE

-- Изменение данных:
-- Увеличьте зарплату всех сотрудников из отдела Engineering на 15%.
-- Уменьшите зарплату сотрудников из отдела HR, если их зарплата больше 6000, на 5%.

-- Мягкое удаление:
-- Пометьте как удалённые (is_deleted = TRUE, deleted_at = NOW()) всех сотрудников, которые были наняты до 2021 года.
-- Обновите поле is_deleted на FALSE для сотрудников, у которых зарплата больше 7000.


-- Часть 2: Работа с командой DELETE

-- Удаление данных:
-- Удалите всех сотрудников из отдела Finance, у которых зарплата меньше 5000.
-- Удалите сотрудников, у которых поле is_deleted равно TRUE.

-- Удаление всех записей:
-- Полностью очистите таблицу с помощью команды TRUNCATE, но только после выполнения всех предыдущих заданий.


-- Часть 3: Дополнительные задания

-- Комбинирование условий:
-- Обновите зарплату сотрудников из отдела Marketing, нанятых после 2022 года, увеличив её на 10%.
-- Удалите всех сотрудников, у которых отдел равен Unknown или зарплата меньше 4500.


-- Творческое задание:

-- Придумайте и выполните 3 команды UPDATE и 3 команды DELETE, чтобы модифицировать и удалить данные в таблице, используя сложные условия (AND, OR, NOT).

-- Примечание:
-- Проверьте результаты выполнения каждой команды с помощью команды
-- SELECT * FROM employees;
