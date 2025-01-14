create table users(
	user_id serial
	, user_name varchar(100)
	, email varchar(320),
	primary key(user_id)
);

create table products(
	product_id serial
	, title varchar(100)
	, description text
	, price decimal
);

create table categories(
	category_id serial
	, category varchar(100)
);


