#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    conection = engine.connect()
    metadata = db.MetaData()
    state = db.Table('states', metadata, autoload=True, autoload_with=engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    obj = session.query(State).filter_by(id=2).all()
    obj[0].name = 'New Mexico'
    session.commit()
