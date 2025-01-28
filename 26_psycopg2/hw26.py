from connect import set_connection

# conn = set_connection()
# cursor = conn.cursor()

# query = 'select now()'
# cursor.execute(query)
# print(cursor.fetchone())

def read_queries(query_file):
    with open(query_file, 'r') as f:
        query = f.read()
    return query


def ddl(query, many=False):
    with set_connection() as conn:
        cursor = conn.cursor()

        if many:
            cursor.executemany(query)
        else:
            cursor.execute(query)

        conn.commit()


# задачи 1.1 и 5.1
tables_ddl_queries = read_queries('queries/creates.sql')
ddl(tables_ddl_queries)


def insert_data(table_name, columns, data):
    with set_connection() as conn:
        cursor = conn.cursor()

        query = f"""
            insert into {table_name} ({', '.join(columns)})
            values ({', '.join(['%s' for _ in columns])})
        """

        cursor.executemany(query, data)
        conn.commit()


# задача 1.2
users_list = [
    ('Ron', 'ron@example.com'), 
    ('Harry', 'harry@example.com'), 
    ('Hermiony', 'hermiony@example.com')
]
insert_data(table_name='users', columns=['username', 'email'], data=users_list)

# # задача 2.1
new_users = [
    ('Sheldon', 'sheldon@example.com'),
    ('Leonard', 'leonard@example.com'),
    ('Penny', 'penny@example.com'),
    ('Howard', 'howard@example.com'),
    ('Raj', 'raj@example.com')
]
insert_data(table_name='users', columns=['username', 'email'], data=new_users)

# задача 5.2
orders_list = [
    (1, 450, 'delivered'),
    (2, 760, 'processing'),
    (3, 630, 'canceled')
]
insert_data(table_name='orders', columns=['user_id', 'amount', 'status'], data=orders_list)