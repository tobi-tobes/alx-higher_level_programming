#!/usr/bin/python3
"""
102-relationship_cities_states_list.py
This file contains a script that lists all City objects
from the database hbtn_0e_101_usa
"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@localhost/{db}",
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City).join(State, City.state).\
        order_by(City.id).all()
    if query:
        for res in query:
            print(f"{res.id}: {res.name} -> {res.state.name}")

    session.close()
