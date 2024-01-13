#!/usr/bin/python3
"""states Module"""
import MySQLdb
import sys

if __name__ == "__main__" and len(sys.argv) == 5:
    conn = MySQLdb.connect(host="localhost",
                           user=sys.argv[1],
                           password=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)

    arg = sys.argv[4]
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE \
                BINARY '{}' ORDER BY id ASC".format(arg))
    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    conn.close()
