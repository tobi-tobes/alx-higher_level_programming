#!/usr/bin/python3
"""
relationship_state.py
This file contains the class definition of a State and an
instance Base = declarative_base()
"""


from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Definition of a class that inherits from Base"""
    __tablename__ = 'states'

    id = Column("id", Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column("name", String(128), nullable=False)
    cities = relationship('City', cascade="all, delete",
                          backref="state")
