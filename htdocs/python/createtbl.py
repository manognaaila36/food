#!C:\Program Files\Python38/python.exe
print("Content-Type:text/html\n")

import sys
sys.path.append('c:\\users\\manogna\\appdata\\roaming\\python\\python38\\site-packages')
import pymysql
mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="nsha"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE table2 (name VARCHAR(25),phonenumber  VARCHAR(10), email VARCHAR(25), password VARCHAR(10), confirmpassword VARCHAR(10))")
mydb.commit()
print("table created successfully")
mydb.close()
