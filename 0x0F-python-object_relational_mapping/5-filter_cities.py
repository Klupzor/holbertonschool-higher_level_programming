#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306)

    cur = db.cursor()
    cur.execute("SELECT id, name FROM cities WHERE state_id =\
            (SELECT id FROM states WHERE name = %s)", (argv[4],))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        cities.append(row[1])
    print(*cities, sep=", ")
