#!/usr/bin/python3
"""Script that lists all states from a database"""
import MySQLdb
import sys

if __name__ == "__main__" and len(sys.argv) == 4:
    conn = MySQLdb.connect(host="localhost", port=3306, 
            user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
