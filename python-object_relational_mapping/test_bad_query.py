from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from setup_db import City, State


engine = create_engine("sqlite:///orm_practice.db")

Session = sessionmaker(bind=engine)
session = Session()

bad_query = session.query(City, State).filter(
    State.id == City.state_id
).all()

for city, state in bad_query:
    print("{}: {} from {}".format(
        city.id,
        city.name,
        state.name
    ))

session.close()
