from sqlalchemy import Column, ForeignKey, Integer, String, Table, create_engine
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

department_employee = Table(
    "department_employee",
    Base.metadata,
    Column("department_id", Integer, ForeignKey("department.id"), primary_key=True),
    Column("employee_id", Integer, ForeignKey("employee.id"), primary_key=True),
)


class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    employees = relationship(
        "Employee", secondary=department_employee, back_populates="departments"
    )


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    departments = relationship(
        "Department", secondary=department_employee, back_populates="employees"
    )


Base.metadata.create_all(engine)

departments = [
    Department(name="IT"),
    Department(name="HR"),
]

employees = [
    Employee(firstname="Иван", lastname="Иванов", departments=[departments[0], departments[1]]),
    Employee(firstname="Анна", lastname="Смирнова", departments=[departments[1]]),
    Employee(firstname="Пётр", lastname="Петров"),
]

with Session(engine) as session:
    session.add_all(departments)
    session.add_all(employees)
    session.commit()
