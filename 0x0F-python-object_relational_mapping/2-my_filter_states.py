#!/usr/bin/python3
"""
2-my_filter_states.py
This file contains a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where name matches
the argument.
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    arg = sys.argv[4]

    db = MySQLdb.connect("localhost", username, password, database)
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name = '{}'\
 ORDER BY id""".format(arg))
    result = cursor.fetchall()
    if result is not None:
        for row in result:
            print(row)

    cursor.close()
    db.close()
