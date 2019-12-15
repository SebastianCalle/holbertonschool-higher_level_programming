#!/usr/bin/python3
"""
Model for cities
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.orm import relationship, backref


class City(Base):
    """
    Class city
    """
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, 
                      ForeignKey('states.id'),
                      nullable=False)
    paretn = relationship("State", backref="cities")
