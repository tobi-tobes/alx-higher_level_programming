#!/usr/bin/python3
"""
14-model_city_fetch_by_state.py
This file contains a script that prints all City objects
from the database hbtn_0e_14_usa
"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@localhost/{db}",
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State.name, City.id, City.name).join(State).\
        order_by(City.id)
    result = query.all()
    for res in result:
        print(f"{res[0]}: ({res[1]}) {res[2]}")

    session.close()
