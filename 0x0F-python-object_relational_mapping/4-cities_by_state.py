#!/usr/bin/python3
"""
Script that lists states that doing match protect SQL injection
"""
import MySQLdb
from sys import argv


def print_states():
    """
    Print states of databease order by id
    """
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    sql = "SELECT cities.id, cities.name, states.name FROM cities\
           INNER JOIN states ON states.id = cities.state_id ORDER BY id;"
    cur = db.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == '__main__':
    print_states()
