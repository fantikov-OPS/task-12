from new_model import Person, engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()
#session.add_all([Person(firstname = 'Kolya', lastname='Varkalov'), Person(firstname = 'Tolya', lastname='Varkalov')])
#session.commit()
person = session.query(Person).filter(Person.firstname == 'Alex').first()

print(person)
print(person.firstname, person.lastname)