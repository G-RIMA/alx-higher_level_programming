#!/usr/bin/python3
 """ List all states from database hbtn_0e_0_usa """

import sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor= db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
