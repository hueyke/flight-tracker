#!/usr/bin/env python3
import time
import sys
import pandas as pd
import bna as airport
from datetime import datetime


def track(status, flight_type='arrivals'):
    print('[%s] Retrieve %s %s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), airport.getName(), flight_type))
    new_status = airport.getStatus(flight_type)
    if status:
        status = new_status.combine_first(status)
    else:
        status = new_status
    print('[%s] Updated  %s %s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), airport.getName(), flight_type))
    status.to_excel('%s.xlsx' % flight_type)
    print('[%s] Written  %s %s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), airport.getName(), flight_type))


def scheduler(flight_type='arrivals'):
    status = None
    while True:
        try:
            track(status, flight_type)
        except:
            print('[%s] %s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'Exception occured.'))
        time.sleep(300)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        scheduler()
    else:
        scheduler(sys.argv[1])
