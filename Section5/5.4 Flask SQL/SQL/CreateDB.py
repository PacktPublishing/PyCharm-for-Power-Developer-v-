from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    zip = Column(String)
    customer = relationship(Customer)
    person_id = Column('person_id', Integer, ForeignKey('customer.id'), primary_key=True)


engine = create_engine('sqlite:///customers.db')
Base.metadata.create_all(engine)
