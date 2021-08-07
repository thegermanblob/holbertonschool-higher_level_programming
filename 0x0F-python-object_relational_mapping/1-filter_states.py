#!/usr/bin/python3
""" Module shows all states contained in the Db hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pswd = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect("localhost", user, pswd, dbname)

    cursor = db.cursor()
    sql = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id asc;"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for item in results:
            print(item)
    except:
        print("Failed to fetch data")
    db.close()
