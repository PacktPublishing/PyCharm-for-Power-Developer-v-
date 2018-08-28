from CreateDB import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///customers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

new_person = Customer(id=1, username='AnitaRita', password='Anita')
session.add(new_person)

new_person_two = Customer(id=2, username='BradChad', password='Brad')
session.add(new_person)


new_address = Address(id=10, zip='12345', customer=new_person)
session.add(new_address)

new_address_two = Address(id=20, zip='54321', customer=new_person_two)
session.add(new_address_two)


session.commit()
