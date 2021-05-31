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
    sql = "SELECT cities.id, cities.name, states.name\
           FROM cities INNER JOIN states\
           ON cities.state_id = states.id"
    cursor.execute(sql)
    data = cursor.fetchall()
    for list in data:
        print("{}".format(list))
