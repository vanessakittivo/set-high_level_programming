#!/usr/bin/python3
"""Validate the corrected SQLAlchemy ORM query."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from setup_db import City


def validate_ai_query(username, password, db_name):
    """Execute the corrected SQLAlchemy ORM query."""
    engine = create_engine("sqlite:///{}".format(db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).join(City.state).all()

    for city in cities:
        print("{}: {} from {}".format(
            city.id,
            city.name,
            city.state.name
        ))

    session.close()
