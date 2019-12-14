#!/usr/bin/python3
"""
Script that lists states that start with N
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
    cur.execute("SELECT * FROM states ORDER BY id;")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()

if __name__ == '__main__':
    print_states()
