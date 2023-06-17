#!/usr/bin/python3
"""
8-model_state_fetch_first.py
This file contains a script that prints the first State object
from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@localhost/{db}",
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id)
    result = query.first()
    if result is None:
        print("Nothing")
    else:
        print(f"{result.id}: {result.name}")

    session.close()
