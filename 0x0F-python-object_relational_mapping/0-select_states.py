#!/usr/bin/python3

"""
    Lists all states from the datatbase hbtn_0e_0_usa
    Arguments:
        mysql username
        mysql password
        database name
"""

import sys
import MySQLdb

if __name__ == 'main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursos = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
