import mysql.connector

mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

myhandle = mydatabase.cursor()
myhandle.execute("CREATE DATABASE novia")
