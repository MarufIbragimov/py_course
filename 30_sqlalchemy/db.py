import datetime

import psycopg2
from task import Task
from sqlalchemy import Table, Column, Integer, String, DateTime, Boolean, MetaData, create_engine, text, ForeignKey
from sqlalchemy.schema import CreateSchema
from sqlalchemy.orm import DeclarativeBase, Session, relationship


engine = create_engine("postgresql://postgres:123@localhost:5432/py_course")

schema_name = 'tasks_app'
metadata = MetaData(schema=schema_name)

with engine.connect() as connection:
    connection.execute(CreateSchema(schema_name, if_not_exists=True))
    connection.commit()


class Base(DeclarativeBase):
    metadata = metadata


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    children = relationship("Tasks", back_populates="parent")


class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String)
    description = Column(String)
    deadline = Column(DateTime)
    priority = Column(String)
    is_done = Column(Boolean, default=False)
    deleted_at = Column(DateTime)

    parent = relationship("Users", back_populates="children")


Base.metadata.create_all(bind=engine)
print("Таблица создана")


db = Session(autoflush=False, bind=engine)


def create_task(task):
    try:
        transformed_deadline = datetime.datetime.strptime(task.deadline, "%d-%m-%Y").date()
    except ValueError:
        print("Ошибка: неверный формат даты!")

    try:
        new_task = Tasks(user_id=task.user_id, title=task.title, description=task.description, deadline=transformed_deadline, priority=task.priority)
        db.add(new_task)
        db.commit()

        return new_task.id
    
    except Exception as e:
        print(f"Ошибка во сохранения задачи в бд: {e}")
        return None


def get_task_by_id(task_id, user_id):
    task = db.query(Tasks).filter(Tasks.id == task_id, Tasks.user_id == user_id).first()
    if task:
        t = Task()
        t.task_id = task.id
        t.title = task.title
        t.description = task.description
        t.deadline = task.deadline
        t.priority = task.priority
        t.is_done = task.is_done
        return t
    else:
        return None


def get_all_tasks(user_id):
    all_tasks = db.query(Tasks).filter(Tasks.user_id == user_id, Tasks.deleted_at == None).all()
    return all_tasks


def edit_task(task):
    try:
        transformed_deadline = datetime.datetime.strptime(task.deadline, "%d-%m-%Y").date()
    except ValueError:
        print("Ошибка: неверный формат даты!")

    task_to_edit = db.query(Tasks).filter(Tasks.id == task.task_id).first()
    if task_to_edit:
        task_to_edit.title = task.title
        task_to_edit.description = task.description
        task_to_edit.deadline = transformed_deadline
        task_to_edit.priority = task.priority
        db.commit()


def get_user_by_username_and_password(username, password):
    user = db.query(Users).filter(Users.username == username, Users.password == password).first()
    if user:
        return (user.id, user.full_name)
    else:
        return None
    

def add_user(username, full_name, password):
    try:
        new_user = Users(username=username, full_name=full_name, password=password)
        db.add(new_user)
        db.commit()

        return new_user.id
    except Exception as e:
        print("Ошибка при добавлении нового пользователя в бд:", e)
        return None


####################################################################################################################################################################

def get_all_deleted_tasks(user_id):
    pass
#     sql_query = """SELECT id, title, description, deadline, priority, is_done
#         FROM tasks WHERE deleted_at IS NOT NULL AND user_id = %s ORDER BY id;"""

#     cursor.execute(sql_query, (user_id,))

#     tasks_tuple = cursor.fetchall()

#     tasks = list()
#     for task_tuple in tasks_tuple:
#         t = Task()
#         t.task_id = task_tuple[0]
#         t.title = task_tuple[1]
#         t.description = task_tuple[2]
#         t.deadline = task_tuple[3]
#         t.priority = task_tuple[4]
#         t.is_done = task_tuple[5]
#         tasks.append(t)

#     return tasks


def soft_delete_task(task_id):
    pass
#     sql_query = """UPDATE tasks
#         SET deleted_at = CURRENT_TIMESTAMP
#         WHERE id = %s;"""

#     cursor.execute(sql_query, (task_id,))


def hard_delete_task(task_id):
    pass
#     sql_query = """DELETE FROM tasks WHERE id = %s;"""

#     cursor.execute(sql_query, (task_id,))


def change_task_status(task_id, status):
    pass
#     sql_query = """UPDATE tasks SET is_done = %s WHERE id = %s;"""

#     cursor.execute(sql_query, (status, task_id))


def get_user_by_username(username):
    pass
#     sql_query = """SELECT id, full_name FROM users WHERE username = %s;"""
#     cursor.execute(sql_query, (username,))

#     return cursor.fetchone()

