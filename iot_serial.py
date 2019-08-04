#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import pymysql as mdb
import csv
 
import serial
import datetime
import time

import logging


logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def insert_sql(database, table, str_columns, values, cursor, connection):
    query = "INSERT INTO "+database+"."+table+" ("+str_columns+") "
    query += "VALUES ("
    for value in values:
        if values.index(value) == 0:
            query += "\'"+value+"\'"
        else:
            query += ",\'"+value+"\'"
    query += ");"

    print(query)

    cursor.execute(query)
    connection.commit()


def run_reading():
    ser = serial.Serial('/dev/ttyUSB0', 9600)

    con = mdb.connect(host='localhost',user='isa',password='demoisa',db='moisture')
    cur = con.cursor()

    columns = "time_stamp, id_plant, description, humidity_level"
    logging.debug('Starting')

    while(1):

        now = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


        reading = now+"," + ser.readline()[:-2].decode("utf-8") 
        logging.debug(reading)
        logging.debug("READING SENSOR 1: "+reading)
        insert_sql("moisture","plants",columns,reading.split(","), cur, con)

        reading = now+"," + ser.readline()[:-2].decode("utf-8") 
        logging.debug(reading)
        logging.debug("READING SENSOR 2: "+reading)
        insert_sql("moisture","plants",columns,reading.split(","), cur, con)
        

        reading = now+"," + ser.readline()[:-2].decode("utf-8") 
        logging.debug(reading)

        logging.debug("READING SENSOR 3: "+reading)
        insert_sql("moisture","plants",columns,reading.split(","), cur, con)

        tempo = float(ser.readline())/1000
        reading = reading[:len(reading)-2]
        time.sleep(float(tempo))
        # print(str(tempo))

    logging.debug('Exiting')










    
    
