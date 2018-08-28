from CreateDB import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///customers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
# people = session.query(Customer).all()
people = session.query(Customer).order_by(Customer.username)
for cust in people:
    print('***')
    print(cust.username)
    print(cust.password)
    address = session.query(Address).filter(Address.person_id == cust.id).one()
    print(address.zip)