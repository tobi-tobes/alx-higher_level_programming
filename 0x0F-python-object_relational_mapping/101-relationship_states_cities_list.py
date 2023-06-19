#!/usr/bin/python3
"""
101-relationship_states_cities_list.py
This file contains a script that lists all State objects, and
corresponding City objects, contained in the database hbtn_0e_101_usa
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

    query = session.query(State).order_by(State.id).all()
    if query:
        for res in query:
            print(f"{res.id}: {res.name}")
            for city in res.cities:
                print(f"    {city.id}: {city.name}")

    session.close()
