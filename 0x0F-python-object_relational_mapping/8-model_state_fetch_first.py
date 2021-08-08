#!/usr/bin/python3
#take 3 arguments: mysql username, mysql password and database name """
# Usage: ./8-model_state_fetch_first.py <mysql username> /
#                                       <mysql password> /
#                                       <database name>
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.
        argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)
    instance = states[0]
    print(str(instance.id)+ ": "+ instance.name)
