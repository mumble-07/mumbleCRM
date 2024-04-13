import mysql.connector

dataBase = mysql.connector.connect (
  host = 'localhost',
  user = 'root',
  password = 'root'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

#create Database

cursorObject.execute("CREATE DATABASE `mumble-playground`")

print("All done, Master!")