#!/usr/bin/python3
'''displays all vaues in the states table'''

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    sql = "SELECT * FROM states WHERE name = '"+argv[4]+"'"
    cursor.execute(sql)
    data = cursor.fetchall()
    for list in data:
        print(list)
