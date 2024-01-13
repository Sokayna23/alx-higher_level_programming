#!/usr/bin/python3
"""script that lists all states with a name starting with N"""
import MySQLdb
import sys

if __name__ == "__main__" and len(sys.argv) == 4:
    conn = MySQLdb.connect(host="localhost",
                           user=sys.argv[1],
                           password=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    conn.close()
