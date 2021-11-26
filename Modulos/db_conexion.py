import mysql.connector


def conexion():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydb"
    )
    mycursor = mydb
    return mycursor