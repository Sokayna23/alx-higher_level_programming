#!/usr/bin/python3
"""States module"""
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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(query, (arg,))

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    conn.close()
