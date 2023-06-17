#!/usr/bin/python3
"""
100-relationship_states_cities.py
This file contains a script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa
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

    query = session.query(State).join(City, State.cities).order_by(State.id, City.id).all()
    if query:
        for res in query:
            print(f"{res.id}: {res.name}")
            for city in res.cities:
                print(f"\t{city.id}: {city.name}")

    session.close()
