#!/usr/bin/python3
"""
model_city.py
This file contains the class definition of a City
"""


from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """Definition of a class that inherits from Base"""
    __tablename__ = 'cities'

    id = Column("id", Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, ForeignKey("states.i\
d"), nullable=False)
    state = relationship("State", back_populates="cities")
