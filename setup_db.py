import mysql.connector

ho = input("Enter your host: ")
us = input("Enter your mysql username: ")
pw =  input("Enter your mysql password: ")
mydb = mysql.connector.connect(
  host= ho, #change
  user= us, #change
  password= pw #change
)

db = input("Enter the name of database you want to create to store domains in: ")

mycursor = mydb.cursor()

mycursor.execute(f'CREATE DATABASE {db}')

print(f'Database {db} created!')

mydb.close()
