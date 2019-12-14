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
    val = argv[4]
    sql = "SELECT cities.name, states.id FROM cities\
           INNER JOIN states ON states.id = cities.state_id\
            WHERE states.name = %s ORDER BY id;"
    cur = db.cursor()
    cur.execute(sql, (val, ))
    rows = cur.fetchall()
    for i in range(len(rows)):
        if i == len(rows) - 1:
            print(rows[i][0])
        else:
            print(rows[i][0], end=", ")
    cur.close()
    db.close()

if __name__ == '__main__':
    print_states()
