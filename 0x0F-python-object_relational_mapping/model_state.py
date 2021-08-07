#!/usr/bin/python3
""" Module contains the State class """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """ Class represents the table states from Db hbtn_0e_4_usa"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """ Method for string representation """
        return "State: {}, {}".format(self.name, self.id)
