import logging
import threading
import time

import iot_serial as ise
import iot_moisture_monitor as imm

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def run():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def my_service():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exiting')


def run_all():
    sread = threading.Thread(name = 'serial_reading', target = ise.run_reading)
    monitor = threading.Thread(name = 'monitor', target = imm.read_send_status)
    sread.start()
    monitor.start()

if __name__ == '__main__':
    run_all()
