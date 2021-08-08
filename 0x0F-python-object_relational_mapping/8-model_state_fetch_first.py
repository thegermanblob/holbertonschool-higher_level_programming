#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
""" Module prints the first State object from the database
    take 3 arguments: mysql username, mysql password and database name """

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                          (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).first()
    if states is None:
        print("Nothing")
    else:
        instance = states
        print(str(instance.id) + ": " + instance.name)
