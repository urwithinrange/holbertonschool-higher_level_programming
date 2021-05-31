#!/usr/bin/python3
'''list states'''

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM states"
    cursor.execute(query)

    data = cursor.fetchall()
    for list in data:
        print(list)