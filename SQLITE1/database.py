#importing dependencies
import sqlite3

#creating a connection and also the database or connecting to the database if it exists already
conn = sqlite3.connect('student.db')

#Creating the cursor
c = conn.cursor()

#creating a table called students
c.execute("""CREATE TABLE students(
        first_name text,
        last_name text,
        email text,
        course text
)""")

#commiting the connection/ commit command
conn.commit()

#closing the connection
conn.close()