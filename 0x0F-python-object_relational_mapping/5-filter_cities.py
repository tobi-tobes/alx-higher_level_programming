#!/usr/bin/python3
"""
5-filter_cities.py
This file contains a script that takes in the name of a state as an
argument and lists all cities of that state, using the database hbtn_0e_4_usa
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
    query = """SELECT name FROM cities\
 WHERE state_id = (SELECT id FROM states WHERE name = %s) ORDER BY id"""
    cursor.execute(query, (arg,))
    result = cursor.fetchall()
    output = ""
    for i in range(0, len(result)):
        output += result[i][0]
        if i < len(result) - 1:
            output += ", "
    print(output)

    cursor.close()
    db.close()
