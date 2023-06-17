#!/usr/bin/python3
"""
0-select_states.py
This file contains a script that lists all states
 from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect("localhost", username, password, database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
