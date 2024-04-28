#!C:\Program Files\Python38/python.exe
print("Content-Type:text/html\n")

import sys
sys.path.append('c:\\users\\manogna\\appdata\\roaming\\python\\python38\\site-packages')

import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="",database="nsha")
mycursor=mydb.cursor()

mycursor.execute("select * from table2")
result=mycursor.fetchall()
print("<table border='1'>")
for rows in result:
    print("<tr><td>")
    print(rows)
    print("</td></tr>")
print("</table>")
