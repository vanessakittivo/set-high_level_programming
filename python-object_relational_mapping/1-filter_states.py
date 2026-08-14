#!/usr/bin/python3
"""List states whose name starts with an uppercase N."""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT id, name FROM states "
        "WHERE BINARY name LIKE 'N%' "
        "ORDER BY id"
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
