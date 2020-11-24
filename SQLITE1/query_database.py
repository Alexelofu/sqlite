#importing dependencies
import sqlite3

#creating a connection and also the database or connecting to the database if it exists already
conn = sqlite3.connect('student.db')

#Creating the cursor
c = conn.cursor()

#Query the Database 
#Selecting the data
c.execute("SELECT * FROM students")

#Fetching the data
print(c.fetchall())
print(c.fetchmany(3))
print(c.fetchone())

print("Commmand Inserted Successfully")

#commiting the connection/ commit command
conn.commit()

#closing the connection
conn.close()