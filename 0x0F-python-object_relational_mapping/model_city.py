#!/usr/bin/python3
""" Module contains City lass """

from model_state import State, Base
from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """ Class represents City table pf database """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
