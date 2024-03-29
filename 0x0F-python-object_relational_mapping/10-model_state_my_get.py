#!/usr/bin/python3
"""
Lists the State object with the name passed as argument
from the database hbtn_0e_6_usa.
Usage: ./10-model_state_my_get.py <mysql username>
                                   <mysql password>
                                   <database name>
                                   <state name searched>
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    InstanceSession = sessionmaker(bind=engine)
    session = InstanceSession()

    state = session.query(State).filter(State.name == argv[4]).first()
    print('Not found' if not state else state.id)
    session.close()
