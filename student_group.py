from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy_utils import create_database, database_exists

DB_USER = "postgres"
DB_PASSWORD = "123"
DB_NAME = "test"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}",
    echo=True,
)

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()


class Group(Base):
    __tablename__ = "study_group"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    students = relationship("Student", back_populates="group")


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey("study_group.id"), nullable=False)
    group = relationship("Group", back_populates="students")


Base.metadata.create_all(engine)

groups = [
    Group(name="ИТ-21"),
    Group(name="ИТ-22"),
]

students = [
    Student(firstname="Иван", lastname="Иванов", group=groups[0]),
    Student(firstname="Пётр", lastname="Петров", group=groups[0]),
    Student(firstname="Сергей", lastname="Сидоров", group=groups[0]),
    Student(firstname="Анна", lastname="Смирнова", group=groups[1]),
    Student(firstname="Мария", lastname="Козлова", group=groups[1]),
    Student(firstname="Ольга", lastname="Новикова", group=groups[1]),
]

with Session(engine) as session:
    session.add_all(groups)
    session.add_all(students)
    session.commit()
