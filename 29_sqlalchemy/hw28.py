from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.sql.operators import ilike_op

engine = create_engine("postgresql://postgres:123@localhost:5432/py_course")
metadata = MetaData(schema="tasks_app")

class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=True)


Base.metadata.create_all(bind=engine)
print("Таблица создана")

db = Session(autoflush=False, bind=engine)


def add_user(name, email, age):
    user = Users(name=name, email=email, age=age)
    db.add(user)
    db.commit()


def get_all_users():
    all_users = db.query(Users).all()

    for user in all_users:
        print(f"{user.id}. {user.name} ({user.email}, {user.age})")


def get_user_by_email(email_substring):
    res = db.query(Users).filter(ilike_op(Users.email, f"%{email_substring}%")).all()
    if res:
        for user in res:
            print(f"{user.id}. {user.name} ({user.email}, {user.age})")
    else:
        print("Пользователь не найден")


def update_user_age(email, new_age):
    user = db.query(Users).filter(Users.email == email).first()

    if user:
        user.age = new_age
        db.commit()
    else:
        print('Пользователь не найден')


def delete_user(email):
    user = db.query(Users).filter(Users.email == email).first()

    if user:
        db.delete(user)
        db.commit()
    else:
        print('Пользователь не найден')