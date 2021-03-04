#!/usr/bin/env python
from __future__ import print_function
import requests
import pandas as pd
from bs4 import BeautifulSoup

def getName():
    return 'BNA'

def getStatus(flight_type='departures'):
    url = 'https://flynashville.com/flights?type=' + flight_type
    with requests.Session() as session:
        res = session.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        raw = soup.find('div', {'id': 'receiving_div_id'}).find('table')
    df = pd.read_html(str(raw))[0]
    df = df.set_index('Flight')
    return df

if __name__ == '__main__':
    print(getStatus('arrivals'))
