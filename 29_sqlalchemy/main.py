from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import create_engine, Column, Integer, String

# from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine("postgresql://postgres:postgres@localhost:5432/python_db")


class Base(DeclarativeBase):
    pass


# создаем модель, объекты которой будут храниться в бд
class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    salary = Column(Integer)


# создаем таблицы
Base.metadata.create_all(bind=engine)

print("таблица создана")

# создаем сессию подключения к бд
with Session(autoflush=False, bind=engine) as db:
    # создаем объект Person для добавления в бд
    # vasya = Person(name="Vasya", age=35, salary=100)
    # bob = Person(name="Bob", age=42)
    # sam = Person(name="Sam", age=25)
    # db.add(vasya)     # добавляем в бд
    # db.add_all([bob, sam])
    # db.commit()     # сохраняем изменения
    # print(bob.id)
    # people = db.query(Person).all()
    # print(people)
    # for p in people:
    #     print(f"{p.id}.{p.name} ({p.age}) | {p.salary}")

    # first_person = db.get(Person, 2)
    # print(f"{first_person.name} - {first_person.age} - {first_person.salary}")

    # people = db.query(Person).filter(Person.age < 30).all()
    # for p in people:
    #     print(f"{p.id}.{p.name} ({p.age})")

    # p = db.query(Person).filter(Person.age < 30).first()
    # print(f"{p.id}.{p.name} ({p.age})")

    # получаем один объект, у которого id=1
    # tom = db.query(Person).filter(Person.id == 1).first()
    # tom = db.get(Person, 1)
    # if tom is not None:
    # print(f"{tom.id}.{tom.name} ({tom.age})")
    # # 1.Tom (38)
    #
    # # изменениям значения
    # tom.name = "Tomassssss"
    # tom.age = 22
    #
    # db.commit()  # сохраняем изменения

    # проверяем, что изменения применены в бд - получаем один объект, у которого имя - Tomas
    # tomas = db.query(Person).filter(Person.id == 1).first()
    # tomas = db.get(Person, 1)
    # print(f"{tomas.id}.{tomas.name} ({tomas.age})")
    # 1.Tomas (22)
    bob = db.get(Person, 1)
    db.delete(bob)  # удаляем объект
    db.commit()  # сохраняем изменения
