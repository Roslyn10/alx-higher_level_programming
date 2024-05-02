#!/usr/bin/python3

"""
    Lists all states with a name starting with N from
    the datatbase hbtn_0e_0_usa
    Arguments:
        mysql username
        mysql password
        database name
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = conn.cursor()

    query = """
            SELECT *
            FROM states
            WHERE state_name LIKE 'N%'
            ORDER BY states.id ASC
            """
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.st close()
