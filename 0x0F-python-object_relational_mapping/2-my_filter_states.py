#!/usr/bin/python3
"""
Script that lists states that doing match
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
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name = %s"
    val = (argv[4], )
    cur.execute(sql, val)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == '__main__':
    print_states()
