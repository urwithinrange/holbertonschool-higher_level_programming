#!/usr/bin/python3
"""
Write a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from
model_state import Base, State
Your script should connect to a MySQL server running on
localhost at port 3306
Print the new states.id after creation
Your code should not be executed when imported
"""

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import State, Base
    from sqlalchemy import (create_engine)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()  # invokes sessionmaker.__call__()
    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    print(state.id)
