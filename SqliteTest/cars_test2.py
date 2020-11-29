import sqlite3
import csv
import pandas as pd
import numpy as np

#creating a connection and also the database or connecting to the database if it exists already
conn = sqlite3.connect('CarsTest.db')

#Creating the cursor
c = conn.cursor()

# testdata = pd.read_sql_query("SELECT * from tests", conn)
# print(testdata.head())


# c.execute('SELECT horsepower FROM tests')
# print(c.fetchall())


# c.execute('SELECT horsepower FROM tests')
# print(c.fetchmany(4))

# c.execute('SELECT row_ID, car_ID, horsepower FROM tests')
# a = c.fetchmany(4)
# df = pd.DataFrame(a)
# print(df)

# c.execute('SELECT * FROM tests LIMIT 10')
# a = c.fetchmany(10)
# print(a)

# c.execute('SELECT COUNT (*) FROM tests')
# a = c.fetchmany()
# print(a)

# c.execute('SELECT car_ID, CarName, peakrpm, enginesize, curbweight, horsepower, carwidth FROM tests WHERE car_ID > 150 AND car_ID < 182')
# a = c.fetchall()
# df = pd.DataFrame(a)
# print(df)

c.execute("SELECT CarName, horsepower, curbweight, carlength, carwidth FROM tests WHERE CarName = 'toyota corona'")
test = c.fetchall()
for a in test:
    print(a)



#commiting the connection/ commit command
conn.commit()

# Closing the connection
conn.close()
