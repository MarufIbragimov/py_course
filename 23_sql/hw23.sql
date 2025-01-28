/*
Задание: 1 (Serge I: 2002-09-30)
Найдите номер модели, скорость и размер жесткого диска для всех ПК стоимостью менее 500 дол. Вывести: model, speed и hd
*/
select
    model
    , speed
    , hd
from pc
where
    price < 500

/*
Задание: 2 (Serge I: 2002-09-21)
Найдите производителей принтеров. Вывести: maker
*/
select distinct maker
from product
where
    type='Printer'

/*
Задание: 3 (Serge I: 2002-09-30)
Найдите номер модели, объем памяти и размеры экранов ПК-блокнотов, цена которых превышает 1000 дол.
*/
select
    model
    , ram
    , screen
from laptop
where
    price > 1000

/*
Задание: 4 (Serge I: 2002-09-21)
Найдите все записи таблицы Printer для цветных принтеров.
*/
select *
from printer
where 
    color = 'y'

/*
Задание: 5 (Serge I: 2002-09-30)
Найдите номер модели, скорость и размер жесткого диска ПК, имеющих 12x или 24x CD и цену менее 600 дол.
*/
select 
    model
    , speed
    , hd
from pc
where 
    cd in ('12x', '24x') 
    and price < 600

