#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import pymysql as mdb
import csv
 
import serial
import datetime
import time
ser = serial.Serial('/dev/ttyUSB0', 9600)
while(1):    
    now = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    reading = now+"," + ser.readline()
    reading += now+"," + ser.readline()
    reading += now+"," + ser.readline()
    tempo = float(ser.readline())/1000
    reading = reading[:len(reading)-2]
    time.sleep(float(tempo))
    print(reading)


    con = mdb.connect('localhost', 'root', '3$Caio%DgM', 'supermercado');


def insert_sql(database, table, str_columns, values):
    query = "INSERT INTO db.?????? (str_columns)"+
    query += "VALUES ("
    for value in values:
        if values.idex(value) == 0:
            query += "\'"+value+"\'"
        else:
            query += ",\'"+value+"\'"
    query += ");"

    cur = con.cursor()
    cur.execute(query)

    
    
