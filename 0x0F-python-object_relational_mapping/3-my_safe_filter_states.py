#!/usr/bin/python3
""" Module shows all states contained in the Db hbtn_0e_0_usa """
import MySQLdb
import sys

user = sys.argv[1]
pswd = sys.argv[2]
dbname = sys.argv[3]
stateName = sys.argv[4]
try:
    stateNameP = stateName.split(" ", 1)
except:
    raise ValueError('Incorrect format')

db = MySQLdb.connect("localhost", user, pswd, dbname)

cursor = db.cursor()
sql = "SELECT * FROM states WHERE name LIKE '" + stateNameP[0] + "' ;"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for item in results:
        print(item)
except:
    print(sql)
    print("Failed to fetch data")


db.close()
