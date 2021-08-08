#!/usr/bin/python3
""" Module contains City class """
from model_state import Base, State
from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class City(Base):
    """ Class represents City table pf database """

    ___tablename___ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'))
