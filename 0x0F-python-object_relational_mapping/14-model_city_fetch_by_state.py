#!/usr/bin/python3
""" Module lists all State objects from the database """
import sys
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State, City).join(City)
    for _s, _c in states.all():
        print("{}: ({}) {}".format(_s.name, _c.id, _c.name))
