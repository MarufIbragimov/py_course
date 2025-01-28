-- Active: 1736707595153@@127.0.0.1@5432@py_course
select *
from users;

/*
Задача 1: Создание данных (CREATE)
1. Вставьте данные в таблицу users:
• Иван Иванов, ivan@example.com.
• Анна Смирнова, anna@example.com.
• Петр Сидоров, petr@example.com.
*/
insert into users(user_name, email)
values
    ('Иван Иванов', 'ivan@example.com')
    , ('Анна Смирнова','anna@example.com')
    , ('Петр Сидоров', 'petr@example.com')
;

/*
Задача 2: Чтение данных (READ)
1. Выведите список всех пользователей из таблицы users.
2. Найдите пользователя с электронной почтой anna@example.com.
3. Найдите всех пользователей, зарегистрированных сегодня.
*/
alter table users
add column registered_at timestamp
;

update users
set registered_at = current_timestamp
;

select *
from users
;

select *
from users
where
    email ilike 'anna%'
;

select *
from users
where
    date(registered_at) = current_date
;

/*
Задача 3: Обновление данных (UPDATE)
1. Измените имя пользователя с электронной почтой ivan@example.com на Иван 
Петров.
2. Обновите дату регистрации пользователя anna@example.com на вчерашнюю 
дату.
*/
update users
set user_name = 'Иван Петров'
where
    email ilike 'ivan%'
; 

update users
set registered_at = registered_at - make_interval(days=>1)
where
    email ilike 'anna%'
;

/*
Задача 4: Удаление данных (DELETE)
1. Удалите пользователя с электронной почтой petr@example.com.
2. Удалите всех пользователей, зарегистрированных до текущей даты.
*/
delete from users
where
    email = 'petr@example.com'
    or date(registered_at) < date(current_timestamp)
;

/*
Задача 5: Работа с таблицей пользователей
1. Добавьте пользователя с именем Елена Королева, email: elena@example.com, 
зарегистрированного 3 дня назад.
2. Найдите всех пользователей, чьи имена начинаются на букву “И”.
3. Обновите имя пользователя с email elena@example.com на Елена Иванова.
4. Удалите всех пользователей, у которых email содержит слово example.
*/
insert into users(user_name, email, registered_at)
values('Елена Королева', 'elena@example.com', date_trunc('day', current_timestamp - make_interval(days=>1)))
;

select *
from users
where
    user_name ilike 'и'
;

update users
set user_name = 'Елена Иванова'
where
    email = 'elena@example.com'
;

delete from users
where
    email like '%example%'
;

/*
Задача 6: Работа с товарами
1. Добавьте в таблицу products следующие товары:
    • Товар: Мышь, Описание: “Игровая мышь”, Цена: 49.99.
    • Товар: Клавиатура, Описание: “Механическая клавиатура”, Цена: 89.99.
    • Товар: Монитор, Описание: “27-дюймовый монитор”, Цена: 299.99.
1. Найдите товары с ценой меньше 100.
2. Увеличьте цену всех товаров на 10%.
3. Удалите товары, у которых цена превышает 500.
*/

insert into products(title, description, price)
values
    ('Мышь', 'Игровая', 49.99)
    , ('Клавиатура', 'Механическая клавиатура', 89.99)
    , ('Монитор', '27-дюймовый монитор', 299.99)
;

select *
from products
where
    price < 100
;

update products
set price = price * 1.1
;

delete from products
where
    price > 500
;

/*
Задача 7: Управление заказами
1. Добавьте в таблицу orders заказы для следующих пользователей:
• Пользователь с ID 1, Дата заказа: сегодня, Сумма: 150.50, Статус: 
“Новый”.
• Пользователь с ID 2, Дата заказа: вчера, Сумма: 300.00, Статус: 
“Завершен”.
1. Найдите все заказы со статусом “Новый”.
2. Обновите статус заказа с суммой 300.00 на “Отменен”.
3. Удалите все заказы со статусом “Отменен”.
*/
create table orders(
    order_id serial
    , user_id integer
    , order_date timestamp default current_timestamp
    , order_sum numeric
    , status varchar(50)
    , primary key(order_id)
    , foreign key(user_id) references users(user_id) on delete cascade
)
;

insert into orders(user_id, order_date, order_sum, status)
values
    (1, current_timestamp, 150.5, 'Новый')
    , (2, current_timestamp - make_interval(days=>1), 300, 'Завершён')
;

select *
from orders
where
    status = 'Новый'
;

update orders
set status = 'Отменен'
where
    order_sum = 300
;

delete from orders
where
    status = 'Отменен'
;

/*
Задача 8: Работа с отзывами
1. Добавьте отзывы для товаров:
• Пользователь с ID 1 оставил отзыв на товар с ID 1: “Отличный 
товар!”, оценка: 5.
• Пользователь с ID 2 оставил отзыв на товар с ID 2: “Среднего 
качества”, оценка: 3.
1. Найдите все отзывы с оценкой 5.
2. Обновите отзыв пользователя с ID 2 на “Хороший товар” и измените оценку 
на 4.
3. Удалите все отзывы, где оценка меньше 3.
*/
create table reviews(
    review_id serial
    , user_id integer
    , product_id integer
    , review text
    , score integer
    , primary key(review_id)
    , foreign key(user_id) references users(user_id) on delete cascade
    , foreign key(product_id) references products(product_id) on delete cascade
)
;

insert into reviews(user_id, product_id, review, score)
values
    (1, 1, 'Отличный товар!', 5)
    , (2, 2, 'Среднего качества', 3)
;

select *
from reviews
where
    score = 5
;

update reviews
set 
    review = 'Хороший товар'
    , score = 4
where
    user_id = 2
;

delete from reviews
where
    score < 3
;

/*
Задача 9: Упрощенная таблица сотрудников
Создайте таблицу employees и выполните CRUD-операции:
1. Создайте таблицу employees со столбцами:
    • employee_id (PK, SERIAL),
    • name (VARCHAR),
    • position (VARCHAR),
    • salary (NUMERIC).
2. Вставьте 3 записи:
• Иван Иванов, Менеджер, 50000.
• Анна Смирнова, Аналитик, 60000.
• Дмитрий Петров, Программист, 70000.
3. Найдите всех сотрудников с зарплатой больше 55000.
4. Обновите позицию “Аналитик” на “Старший аналитик”.
5. Удалите сотрудника с именем Иван Иванов.
*/
create table employees(
    employee_id serial
    , name varchar(100)
    , position varchar(200)
    , salary numeric
    , primary key(employee_id)
)
;

insert into employees(name, position, salary)
values
    ('Иван Иванов', 'Менеджер', 50000)
    , ('Анна Смирнова' , 'Аналитик', 60000)
    , ('Дмитрий Петров', 'Программист', 70000)
;

select *
from employees
where
    salary > 5500
;

update employees
set position = 'Старший аналитик'
where
    position = 'Аналитик'
;

delete from employees
where
    name = 'Иван Иванов'
;

/*
Задача 10: Товары со скидкой
1. Добавьте столбец discount (NUMERIC) в таблицу products, который будет 
хранить процент скидки.
2. Установите скидку 10% для всех товаров с ценой выше 200.
3. Найдите товары, у которых цена со скидкой (цена минус скидка) меньше 100.
4. Удалите товары, у которых скидка превышает 50%.
*/
alter table products
add column discount numeric
;

update products
set discount = .1
where
    price > 200
;

select *
from products
where
    price * (1-discount) < 100
;

delete from products
where
    discount > .5
;
