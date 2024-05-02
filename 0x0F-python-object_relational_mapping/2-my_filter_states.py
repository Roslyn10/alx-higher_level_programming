#!/usr/bin/python3

"""
    Takes in an argument and displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument

    Arguments:
        mysql username
        mysql password
        databasename
        state name searched
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    query = """SELECT * FROM states
            WHERE name = %s
            ORDER BY id ASC""".format(sys.argv[4])

    cursor.execute(query)

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
