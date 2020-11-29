import sqlite3
import csv
import pandas as pd
import numpy as np

#creating a connection and also the database or connecting to the database if it exists already
conn = sqlite3.connect('CarsTest.db')

#Creating the cursor
c = conn.cursor()

#Creating the table with the name cars
import sqlite3
import csv
import pandas as pd
import numpy as np

#creating a connection and also the database or connecting to the database if it exists already
conn = sqlite3.connect('CarsTest.db')

#Creating the cursor
c = conn.cursor()

#Creating the table with the name cars
c.execute("""CREATE TABLE tests(
                                row_ID integer,
                                car_ID integer,
                                symboling integer,
                                CarName text,
                                fueltype text,
                                aspiration text,
                                doornumber text,
                                carbody text,
                                drivewheel text,
                                enginelocation text,
                                wheelbase float,
                                carlength float,
                                carwidth float,
                                carheight float,
                                curbweight integer,
                                enginetype text,
                                cylindernumber text,
                                enginesize integer,
                                fuelsystem text,
                                boreratio float,
                                stroke float,
                                compress float,
                                horsepower integer,
                                peakrpm integer,
                                citympg integer,
                                highwaympg integer
                                )""")

file = open("CarsTest.csv")
test = csv.reader(file)
c.executemany("INSERT INTO  tests VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?, ?)", (test))

c.execute('SELECT * FROM tests')
print(c.fetchmany(6))

#commiting the connection/ commit command
conn.commit()

# Closing the connection
conn.close()
