#importing dependencies
import sqlite3

#creating a connection and also the database or connecting to the database if it exists already
conn = sqlite3.connect('student.db')

#Creating the cursor
c = conn.cursor()

#inserting single values in a database
#c.execute("INSERT INTO students VALUES('Alexander', 'Ofuonyeadi', 'ofuonyeadialexander1997@gmail.com', 'DataScience')")
#c.execute("INSERT INTO students VALUES('Vlad', 'Elofu', 'vladmirelofu7@gmail.com', 'DataScience')")

#inserting many values in a database
students_list = [('Alexander', 'Ofuonyeadi', 'ofuonyeadialexander1997@gmail.com', 'DataScience'),
                ('Alexander', 'Ofuonyeadi', 'ofuonyeadialexander1997@gmail.com', 'DataScience'),
                ('Alexander', 'Ofuonyeadi', 'ofuonyeadialexander1997@gmail.com', 'DataScience'),
                ('Alexander', 'Ofuonyeadi', 'ofuonyeadialexander1997@gmail.com', 'DataScience')
                ]

#Adding data in student_list into the students table in the student.db database
c.executemany("INSERT INTO students VALUES (?, ?, ?, ?)",students_list)
print("Commmand Inserted Successfully")

#commiting the connection/ commit command
conn.commit()

#closing the connection
conn.close()