import mysql.connector

mysqdb = mysql.connector.connect(
    host = "localhost", #change
    user = "root", #change
    password = "password", #change
    database = "domains" #change
)

mycursor = mysqdb.cursor()

print("Creating TABLE")

mycursor.execute("CREATE TABLE domains (id INT AUTO_INCREMENT PRIMARY KEY, ip VARCHAR(255), ports VARCHAR(255))") 
print("LISTING TABLES: ")

mycursor.execute("SHOW TABLES")

for table_name in mycursor:
    print(table_name)

mysqdb.close()

