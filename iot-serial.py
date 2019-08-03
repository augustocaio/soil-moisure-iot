#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import pymysql as mdb
import csv
 
import serial
import datetime
import time


ser = serial.Serial('/dev/ttyUSB0', 9600)

con = mdb.connect(host='localhost',user='isa',password='demoisa',db='moisture')
cur = con.cursor()

columns = "time_stamp, id_plant, description, humidity_level"

def insert_sql(database, table, str_columns, values):
    query = "INSERT INTO "+database+"."+table+" ("+columns+") "
    query += "VALUES ("
    for value in values:
        if values.index(value) == 0:
            query += "\'"+value+"\'"
        else:
            query += ",\'"+value+"\'"
    query += ");"

    print(query)

    cur.execute(query)
    con.commit()



while(1):    
    now = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


    reading = now+"," + ser.readline()
    line_end =  len(reading)-2
    insert_sql("moisture","plants",columns,reading[:line_end].split(","))


    reading = now+"," + ser.readline()
    insert_sql("moisture","plants",columns,reading[:line_end].split(","))


    reading += now+"," + ser.readline()
    insert_sql("moisture","plants",columns,reading[:line_end].split(","))


    tempo = float(ser.readline())/1000
    reading = reading[:len(reading)-2]
    time.sleep(float(tempo))
    print(reading)









    
    
