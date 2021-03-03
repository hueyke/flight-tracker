#!/usr/bin/env python
from __future__ import print_function
import requests
import json
import auth

def getName():
    return 'Science'

def getArticleStatus():
    with requests.Session() as session:
        payload = {
            'username': auth.getScienceUsername(),
            'password': auth.getSciencePassword()
            }
        res = session.post(
            'https://cts.sciencemag.org/scc/api/security/login', json=payload)
        data = json.loads(res.text)
        res = session.get(
            'https://cts.sciencemag.org/scc/api/article/tasks/external', headers=data)
        data = json.loads(res.text)[0]
        return data['articleStatus']

if __name__ == '__main__':
    print(getArticleStatus())
