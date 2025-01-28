/*
Часть 6: Подзапросы  
Найдите сотрудников, у которых зарплата выше средней.  
Для каждого отдела выведите общую сумму зарплат сотрудников.  
Найдите сотрудников с максимальной зарплатой в каждом отделе.
*/

select *
from employees
where salary > (select avg(salary) from employees);

select 
    department
    , sum(salary) as total_salary
from employees
group by
    department
;

select 
    department
    , max(salary) as max_salary
from employees
group by
    department
;

/*
Часть 7: CASE и группировка  
Разделите всех сотрудников на три категории зарплат:  
-- Low (меньше 5000),  
-- Medium (от 5000 до 6999),  
-- High (7000 и выше). Выведите их имена, зарплату и категорию.  
Найдите отделы, где работает более 4 сотрудников.  
Выведите среднюю зарплату для каждого отдела, но только для отделов, где 
работает более 3 сотрудников.
*/
select
    first_name
    , last_name
    , salary
    , case
        when salary < 5000 then 'Low'
        when salary between 5000 and 6999 then 'Medium'
        else 'High'
    end as salary_category
from employees
;

select
    department
from employees
group by
    department
having 
    count(*) > 4
;

select
    department
    , round(avg(salary), 2) as avg_salary
from employees
group by
    department
having 
    count(*) > 4
;

/*
Часть 9: Работа с объединением запросов (UNION, INTERSECT, EXCEPT)  
Используя UNION, объедините списки сотрудников из отделов 'HR' и 
'Finance', исключая дубликаты. Отсортируйте результат по фамилии.  
Используя UNION ALL, объедините списки сотрудников из отделов 'HR' и 
'Marketing', сохранив дубликаты.  
Используя INTERSECT, найдите сотрудников из отдела 'HR', чья зарплата 
превышает 5500.  
Используя EXCEPT, выберите сотрудников из отдела 'Engineering', которые 
не работают в отделе 'HR'.  
Используя INTERSECT ALL, найдите сотрудников, работающих в отделе 
'Finance', чьи зарплаты превышают 6000
*/
select *
from employees
where 
    department = 'HR'
union
select *
from employees
where 
    department = 'Finance'
order by
    last_name
;

select *
from employees
where 
    department = 'HR'
union all
select *
from employees
where 
    department = 'Marketing'
order by
    last_name
;

select *
from employees
where
    department = 'HR'
intersect
select *
from employees
where
    salary > 5000
;

select *
from employees
where
    department = 'Engineering'
except
select *
from employees
where
    department = 'HR'
;

select *
from employees
where
    department = 'Finance'
intersect all
select *
from employees
where
    salary > 6000