#!/usr/bin/python3
"""Script that lists all states from a database"""
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, 
            user="root", password="root", db="hbtn_0e_0_usa")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT * FROM states")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
