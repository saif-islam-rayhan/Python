
# Open phpMyAdmin
#pip install mysql-connector-python

import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="myapp"
)

cursor = db.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
)
""")


name = input("Enter your name: ")
email = input("Enter your email: ")


query = "INSERT INTO users (name, email) VALUES (%s, %s)"
cursor.execute(query, (name, email))
db.commit()

print("Data inserted successfully!")


cursor.execute("SELECT * FROM users")
result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()
db.close()
