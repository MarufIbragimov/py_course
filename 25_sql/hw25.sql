/*
1. **INNER JOIN:**
Напишите запрос, который выводит список сотрудников и их отделов.
*/
select 
    e.employee_id
    , e.name
    , d.department_name
from employees e
    left join departments d on e.department_id = d.department_id
;

/*
2. **LEFT JOIN:**
Найдите всех сотрудников, включая тех, кто не привязан к отделу.
*/
select 
    e.employee_id
    , e.name
    , d.department_name
from employees e
    left join departments d on e.department_id = d.department_id
;

/*
3. **RIGHT JOIN:**
Напишите запрос для отображения всех отделов и соответствующих сотрудников, 
включая те отделы, в которых нет сотрудников.
*/
select
    e.employee_id
    , e.name
    , d.department_name
from employees e
    right join departments d on e.department_id = d.department_id
;

/*
0. Привести по 2 примера на виды связей между таблицами: one-to-one, one-to-
many, many-to-many
1. **Один к одному:**
• Создайте таблицы Users и Passports, где каждому пользователю соответствует 
только один паспорт.
• Напишите SQL-запрос для получения имени пользователя и его номера 
паспорта.
*/
create table users (
    user_id serial primary key,
    name varchar(100) not null
)
;

create table passports (
    passport_id serial primary key,
    user_id integer,
    issued_at date,
    issuer text,
    foreign key (user_id) references users(user_id)
)
;


/*
2. **Один ко многим:**
• Создайте таблицы Authors и Books, где каждый автор может написать 
несколько книг.
• Напишите запрос для получения всех книг определённого автора.
*/
create table authors (
    author_id serial,
    name varchar(100) not null,
    primary key (author_id)
)
;

create table books (
    book_id serial,
    title varchar(100) not null,
    author_id integer,
    foreign key (author_id) references authors(author_id)
)


/*
3. **Многие ко многим:**
• Создайте таблицы Teachers, Classes и таблицу-связку teachers_classes, где 
учителя могут вести несколько классов, а классы могут быть привязаны к 
нескольким учителям.
• Напишите запрос для получения списка учителей, которые ведут определённый 
класс.
*/
create table teachers (
    teacher_id serial,
    name varchar(100) not null,   
    primary key (teacher_id)
);

create table classes (
    class_id serial,
    class_name varchar(100) not null,
    primary key (class_id)
);

create table teachers_classes (
    teacher_id integer,
    class_id integer,
    foreign key (teacher_id) references teachers(teacher_id),
    foreign key (class_id) references classes(class_id)
);