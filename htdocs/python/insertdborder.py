#!C:\Program Files\Python38/python.exe
print("Content-Type:text/html\n")

import sys
sys.path.append('c:\\users\\manogna\\appdata\\roaming\\python\\python38\\site-packages')
import cgi, cgitb
import pymysql
cgitb.enable() 
import sys
form=cgi.FieldStorage()

na = form.getvalue('n')
ph = form.getvalue('a')
it1= form.getvalue('i1')
qt1 = form.getvalue('q1')
pr1 = form.getvalue('p1')
it2= form.getvalue('i2')
qt2 = form.getvalue('q2')
pr2 = form.getvalue('p2')
it3= form.getvalue('i3')
qt3 = form.getvalue('q3')
pr3 = form.getvalue('p3')
con=pymysql.connect(user='root',password='',host='localhost',
                                database='nsha')
cur=con.cursor()
sql = "INSERT INTO ord (name,address,item1,quantity1,price1,item2,quantity2,price2,item3,quantity3,price3) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (na, ph, it1, qt1, pr1, it2, qt2, pr2, it3, qt3, pr3)
cur.execute(sql, val)
con.commit()
con.close()
print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            background-image: url('thanku.jpg');
            background-size: cover;
        }
        nav {
    
    height: 20vh;
}
.nav-link {
    text-decoration: none;
    color: aliceblue;
    font-size: 25px;
}



.nav-button{
    display: flex;
    flex: auto;
    background-color: #E8BD0D;
    border: none;
    padding: 5px 40px;
    border-radius: 30px;
    cursor: pointer;
}
.nav-button {
    background-color:#fff ;
    border: 2px solid #6AC47E;
    border-radius: 0.6em;
    color:red;
    font-style: 1rem;
    font-size: 1rem;
    font-weight: 400;
    padding: 1.2em 2.5em;
    cursor: grab;
    text-align: center;
    text-transform: uppercase;
    font-family: "Montserrat";
    font-weight: 900;

}

.nav-button:hover{
    color:black;
    outline: 0;
}
.nav-button{
    transition: box-shadow 300ms ease-in-out, color 300ms ease-in-out;
}

.nav-button:hover{
    box-shadow: 0 0 40px 40px #1FAA59 ;
}
.nav-button{
    width:10%;
    position: left;
}
   
    </style>
</head>
<body>
    <h1 style='font-size:50px;text-align:center;color:#fff'>You have Ordered Successfully</h1>
    <a href="h1.html" target="_self" class="nav-link"><button class="nav-button">Home</button></a>
</body>
</html>''')


