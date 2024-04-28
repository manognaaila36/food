#!C:\Program Files\Python38/python.exe
print("Content-Type:text/html\n")

import sys
sys.path.append('c:\\users\\manogna\\appdata\\roaming\\python\\python38\\site-packages')

import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="",database="nsha")
mycursor=mydb.cursor()

mycursor.execute("select * from ord")
result=mycursor.fetchall()
print("<table border='1'>")
for rows in result:
    print("<tr><td>")
    print(rows)
    print("</td></tr>")
print("</table>")
print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            background-image: url('ordsucc.jpg');
            background-size: cover;
        }
    </style>
</head>
<body>
    <h1>Order History</h1>
</body>
</html>''')
