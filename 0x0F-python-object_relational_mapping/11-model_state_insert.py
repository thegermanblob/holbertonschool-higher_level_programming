#!/usr/bin/python3
""" Adds the State object “Louisiana” to the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import postgresql
from sqlalchemy.exc import SQLAlchemyError

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    data = "Louisiana"
    try:
        row = State(name="Louisiana")
        session.add(row)
        session.commit()
    except SQLAlchemyError as e:
        print(e)
    query = session.query(State)
    for row in query:
        print("{}: {}".format(row.id, row.name))

