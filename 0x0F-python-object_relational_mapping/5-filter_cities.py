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
    cursor.execute("""SELECT cities.name
    FROM cities INNER JOIN states
    ON cities.state_id = states.id
    WHERE states.name LIKE BINARY %(state)s""", {'state': argv[4]})

    data = cursor.fetchall()
    for list in range(len(data)):
        if list != len(data) - 1:
            print("{}, ".format(data[list][0]), end="")
        else:
            print("{}".format(data[list][0]), end="")
    print()
