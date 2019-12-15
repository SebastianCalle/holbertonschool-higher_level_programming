#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

import sqlalchemy as db

if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    conection = engine.connect()
    metadata = db.MetaData()
    state = db.Table('states', metadata, autoload=True, autoload_with=engine)

    query = db.select([state])
    resul = conection.execute(query)
    resulset = resul.fetchall()
    flag = 0
    for state in resulset:
        if state[1] == sys.argv[4]:
            print("{}".format(state[0]))
            flag = 1

    if flag == 0:
        print("Not found")
