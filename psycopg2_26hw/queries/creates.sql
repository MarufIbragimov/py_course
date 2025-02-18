/*
Задача 1: Создание таблицы и добавление данных
1. Создайте таблицу users с полями:
• user_id (целое число, автоинкрементируемый ключ),
• username (строка, уникальный),
• email (строка),
• created_at (дата и время).
*/

create table if not exists users (
    user_id serial
    , username varchar(255) unique
    , email varchar(320)
    , created_at timestamp default current_timestamp
    , primary key (user_id)
);

/*
Задача 5: Пример с параметрами
1. Создайте таблицу orders с полями:
• order_id (автоинкрементируемый ключ),
• user_id (ссылается на user_id из таблицы users),
• amount (целое число),
• status (строка).
*/
create table if not exists orders (
    order_id serial
    , user_id integer
    , amount integer
    , status varchar(100)
    , foreign key (user_id) references users(user_id)
);

