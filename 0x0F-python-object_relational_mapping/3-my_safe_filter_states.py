#!/usr/bin/python3
'''
script that takes in arguments
and displays all values in the states table
but it protected from mysql injections
'''
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %s\
                    ORDER BY states.id ASC", [argv[4]])
    data = cursor.fetchall()
    for list in data:
        print("{}".format(list))
