#!/usr/bin/python3
"""List states matching a given name."""

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

    query = (
        "SELECT id, name FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY id"
    ).format(sys.argv[4])

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
