#!/usr/bin/python3
"""  prints the State object with the name \
    passed as argument from the database """
import sys
from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import postgresql

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    stateName = sys.argv[4]
    try:
        stateNameP = stateName.split(" ", 1)
    except:
        raise ValueError('Incorrect format')
    query = session.query(State).filter(text("name='{}'"
                                        .format(stateNameP[0])))
    state = query.first()
    if state is None:
        print("Not found")
    else:
        print(state.id)
