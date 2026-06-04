from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import registry

engine = create_engine("sqlite:///new.sqlite", echo=True)
metadata = MetaData()

user_table = Table('user', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('firstname', String),
                   Column('lastname', String)
                   )

metadata.create_all(engine)



class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
mapper_registry = registry()
mapper_registry.map_imperatively(User, user_table)

user = User('Alex', 'Varkalov')
