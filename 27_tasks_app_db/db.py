import psycopg2
from task import Task
import json


def get_db_params():
    with open('db_secrets.json', 'r') as file:
        return json.load(file)


def set_connection():
    db_params = get_db_params()
    conn = psycopg2.connect(
        dbname=db_params['dbname'], 
        user=db_params['user'], 
        password=db_params['password'], 
        host=db_params['host'],
        port=db_params['port']
    )
    return conn


conn = set_connection()
# conn = psycopg2.connect(dbname="python_db", host="localhost", user="postgres", password="123", port=5432)

conn.autocommit = True
cursor = conn.cursor()

cursor.execute("create schema if not exists tasks_app;")
cursor.execute("set search_path to tasks_app;")


def migrate_tables():
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks
            (
                id          SERIAL PRIMARY KEY,
                title       VARCHAR,
                description TEXT,
                deadline    TIMESTAMP,
                priority    VARCHAR,
                is_done     BOOLEAN DEFAULT false
            );""")
    except Exception as e:
        print(f"Ошибка во время миграции: {e}")


def close_db_conn():
    cursor.close()
    conn.close()


# C - create
def create_task(task):
    try:
        sql_query = """INSERT INTO tasks (title, description, priority)
        VALUES (%s, %s, %s) RETURNING id;"""
        cursor.execute(sql_query, (task.title, task.description, task.priority))
        id_tuple = cursor.fetchone()
        return id_tuple[0]
    except Exception as e:
        print(f"Ошибка во сохранения задачи в бд: {e}")
        return None


def get_all_tasks():
    sql_query = """SELECT id, title, description, deadline, priority, is_done
        FROM tasks;"""

    cursor.execute(sql_query)

    tasksTuple = cursor.fetchall()

    tasks = list()
    for task_tuple in tasksTuple:
        t = Task()
        t.task_id = task_tuple[0]
        t.title = task_tuple[1]
        t.description = task_tuple[2]
        t.deadline = task_tuple[3]
        t.priority = task_tuple[4]
        t.is_done = task_tuple[5]
        tasks.append(t)

    return tasks

def check_if_task_exists(task_id):
    sql_query = """
    select id
    from tasks
    where
        id = %s
    """
    is_in_db = False

    cursor.execute(sql_query, (task_id,))
    task_tuple = cursor.fetchone()
    
    if task_tuple is not None:
        is_in_db = True
    return is_in_db


def get_task_by_id(task_id):
    sql_query = """
    select id, title, priority, description, deadline, is_done
    from tasks
    where
        id = %s
    """

    cursor.execute(sql_query, (task_id,))
    task_tuple = cursor.fetchone()

    # print(task_tuple[2])

    t = Task()
    t.task_id = task_tuple[0]
    t.title = task_tuple[1]
    t.priority = task_tuple[2]
    t.deadline = task_tuple[3]
    t.priority = task_tuple[4]
    t.is_done = task_tuple[5]

    return t


    # print(task_tuple)
    # try:
    #     conn = self.connect()
    #     if conn is None:
    #         return
    #     cursor = conn.cursor()
    #     query = "SELECT * FROM tasks WHERE task_id = %s;"
    #     cursor.execute(query, (task_id,))
    #     result = cursor.fetchone()
    #     if result is None:
    #         print(f"Задача с ID {task_id} не найдена")
    #     else:
    #         task = Task(result[0])
    #         task.title = result[1]
    #         task.description = result[2]
    #         task.deadline = result[3]
    #         task.priority = result[4]
    #         task.is_done = result[5]
    #         cursor.close()
    #         conn.close()
    #         return task
    # except psycopg2.Error as e:
    #     print(f"Ошибка при получении задачи: {e}")
    # finally:
    #     if conn:
    #         conn.close()


# try:
#     conn = self.connect()
#     if conn is None:
#         return
#     cursor = conn.cursor()
#     query = """
#         INSERT INTO tasks (title, description, deadline, priority, is_done)
#         VALUES (%s, %s, %s, %s, %s) RETURNING task_id;
#     """
#     cursor.execute(query, (task.title, task.description, task.deadline, task.priority, task.is_done))
#     task_id = cursor.fetchone()[0]
#     conn.commit()
#     cursor.close()
#     conn.close()
#     return task_id
# except psycopg2.Error as e:
#     print(f"Ошибка при добавлении задачи: {e}")
# finally:
#     if conn:
#         conn.close()


def delete_task():
    pass


def update_task():
    pass
