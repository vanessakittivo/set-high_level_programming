#!/usr/bin/python3
"""Define the State class with a relationship to City."""

from sqlalchemy.orm import relationship
from model_state import Base, State
from relationship_city import City


State.cities = relationship(
    "City",
    cascade="all, delete, delete-orphan",
    backref="state"
)
