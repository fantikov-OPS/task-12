from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import registry, Session, declarative_base


engine = create_engine("sqlite:///new.sqlite", echo=True)

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

Base.metadata.create_all(engine)

