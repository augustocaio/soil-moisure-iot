# import iot_serial
import testmail as tm

import pymysql as mdb
import csv
import serial
import datetime
import time

import smtplib, ssl, html_builder
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import logging



logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )



def select_sql(database, table, cursor):
    query = "SELECT id_plant, ROUND(AVG(humidity_level)) AS avg_humidity_level FROM "+database+"."+table+" "
    query += "WHERE time_stamp BETWEEN date_sub(current_timestamp(), INTERVAL 1000 MINUTE) AND current_timestamp()" 
    query += " GROUP BY id_plant;"

    print(query)
    cursor.execute(query)
    result = cursor.fetchall()

    print(result)
    return result




def read_send_status():
    while(1):
        logging.debug('Starting')
        con = mdb.connect(host='localhost',user='isa',password='demoisa',db='moisture')
        cur = con.cursor()
        db = "moisture"
        tb = "plants"

        plants_status = select_sql(db, tb, cur)
        status = []

        for plant in plants_status :
            if plant[1] > 700:
                status.append(0)
            else:
                status.append(1)

        print(status)



        message = MIMEMultipart("alternative")
        message = tm.attach_images('./images/wet-plant.png', 0 ,message)
        message = tm.attach_images('./images/dry-plant.png', 1 ,message)

        html = html_builder.build(status)
        html_part = MIMEText(html, "html")
        message.attach(html_part)

        tm.send_email(message)
        logging.debug("Sent e-mail!")
        time.sleep(60*5)
    con.close()
    logging.debug('Exiting')

# if __name__ == '__main__':
#     read_send_status()




    

