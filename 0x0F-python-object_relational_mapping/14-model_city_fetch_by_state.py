#!/usr/bin/python3
"""
Next, write a script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa:

Your script should take 3 arguments: mysql username, mysql password
and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state
import Base, State
Your script should connect to a MySQL server running on localhost
at port 3306
Results must be sorted in ascending order by cities.id
Results must be display as they are in the example below (<state
name>: (<city id>) <city name>)
Your code should not be executed when imported
"""
if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_city import City
    from model_state import State, Base
    from sqlalchemy import (create_engine)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()  # invokes sessionmaker.__call__()
    CS = session.query(City, State).filter(City.state_id == State.id).all()
    for objc, objs in CS:
            print("{}: ({}) {}".format(objs.name, objc.id, objc.name))
