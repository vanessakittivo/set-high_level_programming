#!/usr/bin/python3
"""Delete states whose names contain the letter a."""

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

    states = session.query(State).filter(
        State.name.like("%a%")
    ).all()

    for state in states:
        session.delete(state)

    session.commit()
    session.close()
