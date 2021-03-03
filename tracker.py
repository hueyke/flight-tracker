#!/usr/bin/env python3
import nature_geoscience as journal
import gmail
import time
from datetime import datetime


def track(previousStatus):
    status = journal.getArticleStatus()
    if status != previousStatus:
        gmail.send(journal.getName(), status)
    return status

def run():
    previousStatus = ''
    while True:
        try:
            status = track(previousStatus)
            print('[%s] %s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), status))
            previousStatus = status
        except:
            print('[%s] %s' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'Exception occured.'))
        time.sleep(300)
if __name__ == '__main__':
    run()
