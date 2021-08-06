#!/usr/bin/python3
""" Module shows all states contained in the Db hbtn_0e_0_usa """
import MySQLdb
import sys

user = sys.argv[1]
pswd = sys.argv[2]
dbname = sys.argv[3]

db = MySQLdb.connect("localhost", user, pswd, dbname)

cursor = db.cursor()
sql = "SELECT cities.id, cities.name, states.name \
        FROM cities INNER JOIN states ON cities.state_id = states.id;"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for item in results:
        print(item)
except:
    print(sql)
    print("Failed to fetch data")


db.close()
