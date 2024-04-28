#!C:\Program Files\Python38/python.exe
print("Content-Type:text/html\n")

import sys
sys.path.append('c:\\users\\manogna\\appdata\\roaming\\python\\python38\\site-packages')
import pymysql
mydb=pymysql.connect(
	host="localhost",
	user="root",
	password="")

m = mydb.cursor()
m.execute("CREATE DATABASE nsha")
print("database created successfully")
