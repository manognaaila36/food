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
mycursor.execute("CREATE TABLE ordtable (name VARCHAR(25),address  VARCHAR(20),item1 VARCHAR(25),quantity1 VARCHAR(25),price1 VARCHAR(25),item2 VARCHAR(25),quantity2 VARCHAR(25),price2 VARCHAR(25),item3 VARCHAR(25),quantity3 VARCHAR(25),price3 VARCHAR(25))")
mydb.commit()
print("table created successfully")
mydb.close()

