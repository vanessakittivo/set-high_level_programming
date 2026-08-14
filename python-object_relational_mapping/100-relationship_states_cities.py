#!/usr/bin/python3
"""Create a State and City using a SQLAlchemy relationship."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from relationship_state import State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Base = State.metadata

    Base.create_all(engine)

    session = Session(engine)

    state = State(name="California")
    city = City(name="San Francisco")

    state.cities.append(city)

    session.add(state)
    session.commit()
    session.close()
