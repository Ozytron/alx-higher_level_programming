#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.
Safe from SQL injections.
Usage: ./3-my_safe_filter_states.py <mysql username>
                                     <mysql password>
                                     <database name>
                                     <state name searched>
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost')

    cursor = db.cursor()
    cursor.execute('SELECT * from states WHERE name = %s ORDER BY states.id',
                   (sys.argv[4], ))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
