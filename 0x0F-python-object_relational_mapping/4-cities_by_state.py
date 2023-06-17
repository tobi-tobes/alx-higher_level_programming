#!/usr/bin/python3
"""
4-cities_by_state.py
This file contains a script that lists all cities from the
database hbtn_0e_4_usa
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect("localhost", username, password, database)
    cursor = db.cursor()
    query = """SELECT cities.id, cities.name, states.name\
 FROM cities INNER JOIN states ON cities.state_id = states.id\
 ORDER BY cities.id"""
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
