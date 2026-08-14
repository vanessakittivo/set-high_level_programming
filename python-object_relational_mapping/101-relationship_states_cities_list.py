#!/usr/bin/python3
"""List all states and their cities."""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from relationship_state import State


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    with Session(engine) as session:
        states = session.query(State).order_by(State.id).all()

        for state in states:
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("\t{}: {}".format(city.id, city.name))
