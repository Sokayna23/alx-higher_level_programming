#!/usr/bin/python3
"""cities moduel"""
import MySQLdb
import sys

if __name__ == "__main__" and len(sys.argv) == 5:
    conn = MySQLdb.connect(host="localhost",
                           user=sys.argv[1],
                           password=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)
    state_name = sys.argv[4]
    cur = conn.cursor()
    query = "SELECT name FROM \
                cities WHERE state_id = (SELECT id FROM states \
                WHERE name LIKE BINARY %s) \
                ORDER BY cities.id ASC"

    cur.execute(query, (state_name,))
    r = cur.fetchall()
    tuples = ()
    for row in r:
        tuples += row
    print(*tuples, sep=", ")

    cur.close()
    conn.close()
