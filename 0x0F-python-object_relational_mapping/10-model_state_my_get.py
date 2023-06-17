#!/usr/bin/python3
"""
9-model_state_filter_a.py
This file contains a script that lists all State objects
that contain the letter a from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    arg = sys.argv[4]

    engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@localhost/{db}",
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name == arg).\
        order_by(State.id)
    result = query.first()
    if result is None:
        print("Not found")
    else:
        print(f"{result.id}")

    session.close()
