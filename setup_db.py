import mysql.connector

# ho = input("Enter your host: ")
# us = input("Enter your database username: ")
# pw =  input("Enter your database password: ")
# mydb = mysql.connector.connect(
#   host= ho, 
#   user= us,
#   password= pw
# )

# db = input("Enter the name of database you want to create to store domains in: ")

# mycursor = mydb.cursor()

# mycursor.execute(f'CREATE DATABASE {db}')

# print(f'Database {db} created!')

# mydb.close()

# del mycursor

mysqdb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "domain"
)

mycursor = mysqdb.cursor()

# print("Creating TABLE")

# mycursor.execute("CREATE TABLE domains (id INT AUTO_INCREMENT PRIMARY KEY, ip VARCHAR(255), ports VARCHAR(255))") 
# print("LISTING TABLES: ")

# mycursor.execute("SHOW TABLES")

# for table_name in mycursor:
#     print(table_name)

sql = "INSERT INTO domains (ip) VALUES (%s)"
val = "10.10.8.166" #change acording to your ips of domains
# you can change value to a list with values like val = [('ip'),(ip)] etc..
mycursor.execute(sql, val)
# mycursor.executemany(sql, val)  
# uncomment this and comment the next line 
# if you inserting more than one row
mysqdb.commit()

print(mycursor.rowcount, "was inserted.")

mysqdb.close()





