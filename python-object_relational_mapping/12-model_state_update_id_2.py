#!/usr/bin/python3
"""Update the name of the State with id 2."""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    session = Session(engine)

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"

    session.commit()
    session.close()
